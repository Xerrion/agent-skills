# Deny-Unless ACL

Learn details about Deny-Unless ACLs.

Deny-Unless ACLs are evaluated with a "deny-unless" approach. The ACL defines the users that will NOT be denied. Said another way, the user will be denied access **unless** the role, condition, and script requirements are met.

**Important:** Deny-Unless ACLs will take priority against Allow-If ACLs in ACL Evaluation, as it will be evaluated first.

A Deny-Unless ACL produces two outcomes

| Evaluation outcome | Result                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pass               | The defined roles, data conditions, security attributes, and script requirements are met. The ACL proceeds to further evaluation **Important:** Even if a Deny-Unless ACL matches, access is only granted when an Allow-If ACL explicitly permits it. If no Allow-If ACL is matched and the Deny-Unless ACL passes, the system grants access by default. |
| Fail               | The Deny-Unless ACL is marked as failing and access will be denied.                                                                                                                                                                                                                                                                                      |

The following is an explained example of a Deny-Unless ACL:

- ACL has roles `sn_hr_core.manager` and `itil`
- Condition has active = `true`
- script has answer = `gs.isLoggedIn();`

The user is denied access unless all three requirements for this ACL are satisfied. In order for this Deny-Unless ACL to pass, a user needs either the `sn_hr_core.manager` or `itil` roles, be accessing a record that has active field = `true`, and be logged in. The Deny-Unless ACL will fail if any of the three requirements isn't met.
