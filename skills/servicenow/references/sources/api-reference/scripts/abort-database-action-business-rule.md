# Abort a database action

You can use a before business rule script to cancel or abort the current database action using the current.setAbortAction(true) method.

If the before business rule is executed during an insert action, and a condition in the script calls current.setAbortAction(true), the new record stored in current is not created in the database.

[GlideRecord - setAbortAction(Boolean b)](../server-api-reference/glide-record-global.md)

[Scoped GlideRecord - setAbortAction(Boolean b)](../server-api-reference/glide-record-scoped.md)
