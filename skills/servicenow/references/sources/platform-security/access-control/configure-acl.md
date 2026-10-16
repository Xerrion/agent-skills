# Configure an ACL

Configure custom access control lists (ACLs) to secure access to new objects or to change the default security behavior.

## Before you begin

Role required: security_admin

## About this task

To create ACLs, you must elevate privileges to the security_admin role.

For tables that are in a different scope from the ACL record, the types of rules are limited. For Scope Master tables to derive scope and execute scoped ACLs, set the `glide.enforce_security_scope.<scope_name>` property to **true**. This ensures ACLs in the global scope don’t match when there are scope-specific ACLs created on the relevant table. Examples are when securing data within shared application tables in the Global scope, such as sys_attachment or sys_question_answer tables.

## Procedure

1. Elevated privilege roles to the security_admin role.

2. Navigate to **System Security** > **Access Control (ACL)**.

3. Select **New**.

   **Tip:** When creating an ACL, it’s helpful to review the [Deny-Unless ACL](acl-denial-behavior.md).

4. Complete the form.

   | Field             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Type              | Select what kind of object this ACL secures. The type of object determines how the object is named and what operations are available. This field is read only after the ACL is created. If you want to change the type, you must delete the ACL and create one with the correct type.                                                                                                                                                                                                                                                                                                                                                                                                            |
   | Operation         | Select the operation that this ACL secures. Each object type has its own list of operations. An ACL can only secure one operation. To secure multiple operations, create a separate ACL for each. If you’re creating an ACL for a report_view operation, see also Report_view access control.                                                                                                                                                                                                                                                                                                                                                                                                    |
   | Decision Type     | Select the decision type of the ACL. **Allow If** allows access upon successful evaluation. **Deny Unless** denies access unless there’s successful evaluation. See [Deny-Unless ACL](acl-denial-behavior.md) for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | Admin overrides   | Select this check box to have users with the admin role automatically pass the permissions check for this ACL. Admin users pass regardless of what script or role restrictions apply. However, the **nobody** role, which only ServiceNow personnel can assign, takes precedence over the admin override option. If an ACL is assigned the **nobody** role, admin users can’t access the resource even when **Admin overrides** is selected. See Base system roles.                                                                                                                                                                                                                              |
   | Protection Policy | Select this option to set the protection policy on the ACL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | Name              | Enter the name of the object being secured, either the record name or the table and field names. The more specific the name, the more specific the ACL. You can use the wildcard character asterisk (*) in place of a record, table, or field name to select all objects that match a record type, all tables, or all fields. You can’t combine a wildcard character and a text search. For example, `inc*` isn’t a valid ACL name, but `incident.*` and `*.number` are valid ACL names. **Note:** Select the blue triangle to manually enter the record name or the table and field names of the object being secured. Use this option to secure an object that doesn’t appear in the dropdown. |
   | Description       | Enter a description of the object or permissions that this ACL secures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | Applies To        | Select **Add Filter Condition** to create a filter for the table selected in the **Name** field. The ACL applies only to the records matching this filter condition. For example, you could create an ACL for the incident table that applies only to incidents with the Critical priority. **Note:** You must select a table in the **Name** field to use this option. ACLs beginning with * cannot use the **Applies To** filter.                                                                                                                                                                                                                                                              |
   | Active            | Select this check box to enforce this ACL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | Advanced          | Select this check box to display the **Advanced Condition** fields. See step 6.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

   **Admin overrides:**

   Clear this check box if administrators must meet the permissions defined in this ACL to gain access to the secured object. Since administrators always pass role checks (see the description of the **Requires role** field), use the condition builder or **Script** field to create a permissions check that administrators must pass.

5. To narrow the scope of the ACL fill in the **Conditions** fields as necessary.

   | Field                        | Description                                                                                                                                                                                                                                                                                                                                                      |
   | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Requires role                | Use this list to specify the roles a user must have to access the object. If you list multiple roles, a user with any one of the listed roles can access the object. The Requires role list appears as a related list. **Note:** Users with the admin role always pass this permissions check because the admin role automatically grants users all other roles. |
   | Security Attribute Condition | Use this section to define what the user can access based on user and environment criteria. For more information, see Security Attributes Fundamentals and Security Attribute Type. **Note:** The Condition field is case-sensitive.                                                                                                                             |
   | Data Condition               | Use this condition builder to select the fields and values that must be true for users to access the object. **Note:** The Condition field is case-sensitive.                                                                                                                                                                                                    |

6. If the **Advanced** box is checked, fill in the **Advanced Conditions** fields as necessary.

   | Field                    | Description                                                                                                                                                                                                                                                                      |
   | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Controlled by References | Enforces the ACL on related records. See Related record access for more details.                                                                                                                                                                                                 |
   | Script                   | Enter a custom script describing the permissions required to access the object. The script can use the values of the current and previous Global variables in business rules as well as system properties. The script must generate a true or false response in one of two ways: |

   **Script:**

   - return an answer variable set to a value of true or false
   - evaluate to true or false

   In either case, users only gain access to the object when the script evaluates to true and the user meets any conditions the ACL has. Both the conditions and the script must evaluate to true for a user to access the object.

   If there’s script in the **Script** field. This script executes even if the field isn’t displayed on the form.

   **Note:** If the evaluated item is in a related list, **current** points to the item the related list is on, not to the current item the ACL is for. However, If the item you’re evaluating the ACL for isn’t in a related list, **current** points to the actual item.

7. Select and hold (or right-click) the form header and select **Save**.
