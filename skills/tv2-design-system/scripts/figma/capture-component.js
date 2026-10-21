const page=await figma.getNodeByIdAsync(PAGE_ID);
if(!page || page.type!=="PAGE") throw new Error("Page unavailable");
await figma.setCurrentPageAsync(page);
const variableIds=new Set(),styleIds=new Set();
function safe(v){ if(typeof v==="symbol") return "__MIXED__"; if(v===undefined)return null; return JSON.parse(JSON.stringify(v)); }
function collect(v){if(!v||typeof v!=="object")return;if(v.type==="VARIABLE_ALIAS")variableIds.add(v.id); for(const x of Object.values(v))collect(x);}
function node(n,depth){
 const out={id:n.id,name:n.name,type:n.type};
 for(const k of ["visible","width","height","x","y","minWidth","maxWidth","minHeight","maxHeight","layoutMode","layoutWrap","layoutSizingHorizontal","layoutSizingVertical","primaryAxisSizingMode","counterAxisSizingMode","primaryAxisAlignItems","counterAxisAlignItems","paddingTop","paddingRight","paddingBottom","paddingLeft","itemSpacing","counterAxisSpacing","cornerRadius","topLeftRadius","topRightRadius","bottomLeftRadius","bottomRightRadius","fills","strokes","strokeWeight","strokeAlign","effects","opacity","boundVariables","explicitVariableModes","resolvedVariableModes","clipsContent","layoutPositioning","constraints","textStyleId","effectStyleId","fillStyleId","strokeStyleId"]){
  if(k in n){out[k]=safe(n[k]);if(k==="boundVariables"||k==="fills"||k==="strokes"||k==="effects")collect(out[k]);if(k.endsWith("StyleId")&&typeof out[k]==="string"&&out[k])styleIds.add(out[k]);}
 }
 if(n.type==="TEXT"){for(const k of ["characters","fontName","fontSize","fontWeight","lineHeight","letterSpacing","textAutoResize","textAlignHorizontal","textAlignVertical"])if(k in n)out[k]=safe(n[k]);}
 if(n.type==="COMPONENT"){out.variantProperties=safe(n.variantProperties);}
 if(n.type==="INSTANCE")out.componentProperties=safe(n.componentProperties);
 if(depth>0&&"children" in n&& !["VECTOR","BOOLEAN_OPERATION"].includes(n.type))out.children=n.children.map(c=>node(c,depth-1));
 return out;
}

function metrics(n){const o={id:n.id,properties:safe(n.variantProperties)};const keys=["width","height","paddingTop","paddingRight","paddingBottom","paddingLeft","itemSpacing","cornerRadius"];o.values=keys.map(k=>k in n?safe(n[k]):null);return o;}
const sets=page.findAllWithCriteria({types:["COMPONENT_SET"]}).map(s=>({id:s.id,name:s.name,description:s.description,defaultVariantId:s.defaultVariant?s.defaultVariant.id:null,properties:safe(s.componentPropertyDefinitions),metricColumns:["width","height","paddingTop","paddingRight","paddingBottom","paddingLeft","itemSpacing","cornerRadius"],variants:s.children.map(metrics),defaultTree:s.defaultVariant?node(s.defaultVariant,CAPTURE_DEPTH):null}));
const standalone=page.findAllWithCriteria({types:["COMPONENT"]}).filter(c=>c.parent&&c.parent.type!=="COMPONENT_SET").map(c=>({properties:safe(c.componentPropertyDefinitions),...node(c,CAPTURE_DEPTH)}));
const variables={},collections={};
for(let pass=0;pass<8;pass++){
 const pending=[...variableIds].filter(id=>!(id in variables));
 if(!pending.length)break;
 const resolved=await Promise.all(pending.map(async id=>{try{const v=await figma.variables.getVariableByIdAsync(id);if(!v)return[id,{unavailable:true}];const data={id:v.id,key:v.key,name:v.name,collectionId:v.variableCollectionId,resolvedType:v.resolvedType,valuesByMode:safe(v.valuesByMode)};collect(data.valuesByMode);return[id,data];}catch(e){return[id,{unavailable:String(e)}];}}));
 for(const [id,v]of resolved)variables[id]=v;
}
const collectionIds=[...new Set(Object.values(variables).map(v=>v.collectionId).filter(Boolean))];
for(const [id,c]of await Promise.all(collectionIds.map(async id=>{try{const c=await figma.variables.getVariableCollectionByIdAsync(id);return[id,c?{id:c.id,key:c.key,name:c.name,defaultModeId:c.defaultModeId,modes:safe(c.modes)}:{unavailable:true}];}catch(e){return[id,{unavailable:String(e)}];}})))collections[id]=c;
const styles={};
for(const [id,s]of await Promise.all([...styleIds].map(async id=>{try{const s=await figma.getStyleByIdAsync(id);if(!s)return[id,{unavailable:true}];const o={id:s.id,name:s.name,type:s.type};for(const k of ["effects","paints","fontName","fontSize","lineHeight","letterSpacing"])if(k in s)o[k]=safe(s[k]);return[id,o];}catch(e){return[id,{unavailable:String(e)}];}})))styles[id]=s;
const result={schemaVersion:1,source:{fileKey:"cjU0zuiL2r8YXsGmnNxxy2",capturedOn:CAPTURED_ON,pageId:page.id,pageName:page.name,kind:"native-component-measurements",unit:"Figma px",readOnly:true},sets,standalone,variables,collections,styles};
if(JSON.stringify(result).length>46000) throw new Error("Capture exceeds the connector response budget; reduce capture depth and retry this page only.");
return result;
