---
name: servicenow
description: Use this skill to develop, review, or troubleshoot ServiceNow scripts, Business Rules, Client Scripts, GlideRecord queries, encoded filters, date handling, and ACLs. Also use it for ServiceNow API contract lookup or MCP tool selection, payload construction, and error recovery.
---

# ServiceNow

Read the reference for the current task. Load additional guidance only when the task needs it.

## Select a task

| Task                                                                                                                     | Read when needed                                           |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| MCP calls, record payloads, pagination, preview tokens, or structured errors                                             | [MCP interaction](references/mcp.md)                       |
| Server scripts, Script Includes, JavaScript modes, or error handling                                                     | [Server scripting](references/scripting.md)                |
| Business Rule timing, conditions, recursion, or asynchronous execution                                                   | [Business Rules](references/business-rules.md)             |
| Client Scripts, UI Policies, GlideAjax, or scratchpad                                                                    | [Client scripting](references/client-scripts.md)           |
| Record queries, aggregation, batching, or write side effects                                                             | [GlideRecord patterns](references/gliderecord-patterns.md) |
| Constructing, explaining, or debugging encoded filters                                                                   | [Encoded queries](references/encoded-queries.md)           |
| Exact API signatures, overloads, execution context, or declaration coverage                                              | [API lookup](references/glide-api.md)                      |
| UTC storage, user display, date-only values, or calendar arithmetic                                                      | [Dates and times](references/date-time.md)                 |
| Record and field access, Deny-unless, or Security Data Filters                                                           | [ACL design](references/acl-design.md)                     |
| Boolean coercion, unexpected lookups or writes, query counts, client/session state, date parsing, or attachment failures | [Platform gotchas](references/platform-gotchas.md)         |

For ordinary tool interaction, use the MCP reference only when its protocol guidance helps.
A payload containing scripts, filters, or ACL records does not require the script-authoring workflow.
Load code references when constructing or reviewing that content, or investigating its platform behavior.

For an API lookup, select the class and global, scoped, client, or server context before choosing a method.
Search for the required symbol instead of loading every catalogue or declaration.
Use the [local API sources](references/sources.md) when an overload is missing or contracts conflict.
