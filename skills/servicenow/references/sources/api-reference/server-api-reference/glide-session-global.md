# GlideSession- Global

The GlideSession API provides methods to find information about the current session.

## GlideSession - clearClientData(String paramName)

Clears a session client value previously set with putClientData().

This method is used in a client script to clear data values that were set by a server script using the putClientData() method.

| Name      | Type   | Description                       |
| --------- | ------ | --------------------------------- |
| paramName | String | Name of the client data to clear. |

| Type | Description |
| ---- | ----------- |
| void |             |

```
var session = gs.getSession();
session.putClientData('custName', 'Harry');
var clientData = session.getClientData('custName');
gs.info(clientData);

session.clearClientData('custName');
clientData = session.getClientData('custName');
gs.info(clientData);
```

Output:

```
Harry

null
```

## GlideSession - getClientData(String paramName)

Returns a session client value previously set with putClientData().

This method is used in a client script to retrieve data values that were set by a server script that used the putClientData() method.

| Name      | Type   | Description                          |
| --------- | ------ | ------------------------------------ |
| paramName | String | Name of the client data to retrieve. |

| Type   | Description                  |
| ------ | ---------------------------- |
| String | The client data as a string. |

```
var session = gs.getSession();
session.putClientData('test1', 'Harry');
var clientData = session.getClientData('test1');
gs.info(clientData);
```

Output:

```
Harry
```

### Scoped equivalent

To use the getClientData() method in a scoped application, use the corresponding scoped method: getClientData().

## GlideSession - getLanguage()

Gets the session's language code.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type   | Description                  |
| ------ | ---------------------------- |
| String | The session's language code. |

```
var session = gs.getSession();
var language = session.getLanguage();
gs.info(language);
```

Output:

```
en
```

### Scoped equivalent

To use the getLanguage() method in a scoped application, use the corresponding scoped method: getLanguage().

## GlideSession - getRoles()

Gets a list of roles for the current user.

The list of roles does not reflect any changes made during the current user session. To get the updated list of roles, the user must log out and log back in.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type   | Description                      |
| ------ | -------------------------------- |
| String | A comma separated list of roles. |

```
gs.info(gs.getSession().getRoles());
```

Output:

```
admin,hr_fulfiller,itsa_fulfiller,security_admin
```

## GlideSession - getTimeZoneName()

Gets the name of the session's time zone.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type   | Description                          |
| ------ | ------------------------------------ |
| String | The name of the session's time zone. |

```
var session = gs.getSession();
var zoneName = session.getTimeZoneName();
gs.info(zoneName);
```

Output:

```
US/Pacific
```

### Scoped equivalent

To use the getTimeZoneName() method in a scoped application, use the corresponding scoped method: getTimeZoneName().

## GlideSession - isInteractive()

Determines if the current session is interactive.

An interactive session is one that involves an end-user interacting with a user interface that then retrieves information from a server. An example of this type of session is when a user logs in using the log-in screen or uses a form to query a data store. A non-interactive session is one that only involves programmatic interaction with a server such as a SOAP request to retrieve data.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type    | Description                         |
| ------- | ----------------------------------- |
| Boolean | True if the session is interactive. |

**Note:** The isInteractive() method will always return a false value for all user sessions using the classic or current mobile applications.

```
var interActive = gs.getSession().isInteractive();
gs.info(interActive);
```

Output:

```
false
```

### Scoped equivalent

To use the isInteractive() method in a scoped application, use the corresponding scoped method: isInteractive().

## GlideSession - isLoggedIn()

Determines if the current user is currently logged in.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type    | Description                            |
| ------- | -------------------------------------- |
| Boolean | True if the current user is logged in. |

```
var session = gs.getSession();
var loggedIn = session.isLoggedIn();
gs.info(loggedIn);
```

Output:

```
true
```

### Scoped equivalent

To use the isLoggedIn() method in a scoped application, use the corresponding scoped method: isLoggedIn().

## GlideSession - putClientData(String paramName, String paramValue)

Sets a session client value that can be retrieved with getClientData(). This method is used in a server side script that runs when a form is created.

| Name       | Type   | Description                          |
| ---------- | ------ | ------------------------------------ |
| paramName  | String | Name of the client parameter to set. |
| paramValue | String | Parameter value.                     |

| Type | Description |
| ---- | ----------- |
| void |             |

```
var session = gs.getSession();
session.putClientData('test1', 'Harry');
var clientData = session.getClientData('test1');
gs.info(clientData);
```

Output:

```
Harry
```

### Scoped equivalent

To use the putClientData() method in a scoped application, use the corresponding scoped method: putClientData().
