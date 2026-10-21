# Local Figma record format

The JSON files in [figma/](../figma/) contain measurements read from original Figma components on 2026-10-21. They are bundled data, not pointers that require Figma access.

Each file covers one component or one product layout. Its `source` identifies the upstream file, page, date, unit, and read-only capture. IDs identify evidence; ordinary implementations do not query them.

For component sets, `properties` preserves actual names, defaults, and available property options. `variants` lists the combinations that actually exist. When `metricColumns` is present, each variant's `values` array follows those columns in order. `defaultTree` records the original default variant and its descendants to the captured depth. `standalone` contains components without a variant set.

`variables` retains bound variable names, alias IDs, and values for every retrieved mode. `collections` maps mode IDs to names. Resolve aliases through this same file. `styles` retains retrieved text or effect style properties. `__MIXED__` means the source has mixed values; it is not a usable CSS value.

Tree depth is deliberately bounded. Absence of a descendant or field does not establish a design rule. Width and height describe the captured content and resizing mode; fixed sample text width is not a universal control width. Root canvas coordinates are not page padding.
Figma Device Size modes are labelled SM (360), MD (840), and LG (1440). These are reference frame sizes. Use the independent [breakpoint tokens](../foundations/breakpoints.md) for CSS transition thresholds.

The local component prose summarizes measured defaults and identifies web adaptations. Raw records preserve inconsistencies rather than silently changing the source. Do not infer missing geometry or interaction rules from those inconsistencies.
