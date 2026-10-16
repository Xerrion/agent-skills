# Default security filters

Generally data filters are applied after absolute ACLs (also sometimes called table-level ACLs), and after row-level ACLs. They are applied by default, and can be impactful to system behavior if not used carefully.

## Default applied security data filters

Security data filters are applied by default to the following places:

| Category               | Application                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| List and Forms         | UI16, Workspaces, Service Catalog, Service Portal, Mobile.                                  |
| Reports and Dashboards | Reports, Data visualizations, Core UI Dashboards, Platform Analytics experience dashboards. |
| Data Export            | Export XML, CSV, Excel, JSON, PDF.                                                          |
| Flow Engine            | Record Lookup steps                                                                         |
| Search                 | AI Search, Text Search.                                                                     |
| GlideRecord            | GlideRecordSecure, GlideRecordSandbox, GlideAggregateSandbox.                               |
| REST and GraphQL APIs  | REST table API, REST stats API, GraphQL table and stats API equivalent.                     |
