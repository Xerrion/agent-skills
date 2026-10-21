const page=await figma.getNodeByIdAsync(PAGE_ID);
if(!page || page.type!=="PAGE") throw new Error("Page unavailable");
await figma.setCurrentPageAsync(page);
const variableIds=new Set(),styleIds=new Set();
function safe(v){ if(typeof v==="symbol") return "__MIXED__"; if(v===undefined)return null; return JSON.parse(JSON.stringify(v)); }
function collect(v){if(!v||typeof v!=="object")return;if(v.type==="VARIABLE_ALIAS")variableIds.add(v.id); for(const x of Object.values(v))collect(x);}

function node(n,depth){const o={id:n.id,name:n.name,type:n.type};for(const k of ["width","height","layoutMode","layoutSizingHorizontal","layoutSizingVertical","primaryAxisAlignItems","counterAxisAlignItems","paddingTop","paddingRight","paddingBottom","paddingLeft","itemSpacing","maxWidth","boundVariables","explicitVariableModes","resolvedVariableModes"]){if(k in n)o[k]=safe(n[k]);}if(o.boundVariables)collect(o.boundVariables);if(depth>0&&"children" in n)o.children=n.children.map(c=>node(c,depth-1));return o;}
const sets=[],standalone=[];
const layouts=await Promise.all(LAYOUT_IDS.map(async id=>{const n=await figma.getNodeByIdAsync(id);if(!n)throw new Error("Registered layout node is unavailable: "+id);return node(n,CAPTURE_DEPTH);}));
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
const result={schemaVersion:1,source:{fileKey:"cjU0zuiL2r8YXsGmnNxxy2",capturedOn:CAPTURED_ON,pageId:page.id,pageName:page.name,kind:"free-layout-measurements",unit:"Figma px",readOnly:true},sets,standalone,layouts,variables,collections,styles};
if(JSON.stringify(result).length>46000) throw new Error("Capture exceeds the connector response budget; reduce capture depth and retry this page only.");
return result;
