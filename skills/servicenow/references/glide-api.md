# Glide API lookup

Select the execution context and class before reading a contract. Search the needed method in one catalogue; do not load every catalogue or the full declaration imports.

## Canonical contracts

| API            | Task guide                                           | Server global contracts                                   | Server scoped distinctions                                                            |
| -------------- | ---------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| GlideRecord    | [Queries, values, and writes](glide-record.md)       | [Global](types/server/glide-record-global.md)             | [Scoped supplement](types/server/glide-record-scoped.md)                              |
| GlideAggregate | [Counts, groups, and trends](glide-aggregate.md)     | [Global](types/server/glide-aggregate-global.md)          | [Scoped supplement](types/server/glide-aggregate-scoped.md)                           |
| GlideElement   | [Fields, permissions, and changes](glide-element.md) | [Global](types/server/glide-element-global.md)            | [Scoped supplement](types/server/glide-element-scoped.md)                             |
| GlideDate      | [Date-only values](glide-date.md)                    | [Global](types/server/glide-date-global.md)               | [Scoped supplement](types/server/glide-date-scoped.md)                                |
| GlideDateTime  | [Timestamps and arithmetic](date-time.md)            | Follow the context-specific source for the needed method. | [Scoped source](sources/api-reference/server-api-reference/glide-date-time-scoped.md) |

Scoped supplements cover additions and differences. Use the scoped source for other methods and overloads.
Global, scoped, client, and server methods can have different contracts.

## Type declarations

Use [server declarations](types/server/glide-server.d.ts) or [client declarations](types/client/glide-client.d.ts) for symbol lookup.
Keep server and client globals in separate execution contexts.
The server declarations mix global and scoped APIs and require external types, including a consumer-provided `Tables` schema.
The client declarations require browser types. Both files contain unresolved dependencies and type errors.
GlideAjax callbacks are incorrectly typed as `string`. Pass a function, as the documented API requires.

## Troubleshooting

For unexpected field values or insert-time change detection, select the matching section of [platform pitfalls](platform-gotchas.md).
For caller-facing record reads, check [record and field access](glide-record.md#choose-the-operation). Standard ACL checks and query ACL checks have different contracts.
For uncertain scope or capability support, use the matching [API source](sources.md).
