# GlideForm (g_form) - Client

The GlideForm API provides methods to customize forms.

Only use GlideForm methods on the client. You can use these methods to make custom changes to the form view of records. All validation of examples was done using client scripts.

You can also use some of these methods in other client scripts (such as Catalog Client Scripts or Wizard Client Scripts), but you must first test this to determine whether they will work as expected.

**Note:** The methods getControl(), getHelpTextControl(), getElement(), and getFormElement() are deprecated for mobile devices. For information on using GlideForm for mobile, see Mobile Client GlideForm (g_form) Scripting and Migration.

There is no constructor for the GlideForm class. Access GlideForm methods using the `g_form` global object.

## GlideForm - addDecoration(String fieldName, String icon, String title)

Adds an icon on a field's label.

Adding the same item twice is prevented; however, you can add the same icon with a different title.

**Note:** This method is not supported by Service Catalog.

| Name      | Type   | Description                                                                                                  |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| fieldName | String | Field name.                                                                                                  |
| icon      | String | Name of the icon to show next to the specified field. See [valid decoration icons](#valid-decoration-icons). |
| title     | String | Title for the icon.                                                                                          |

### Valid decoration icons

- icon-add
- icon-alert
- icon-book
- icon-book-open
- icon-calendar
- icon-cards
- icon-cart-full
- icon-catalog
- icon-check-circle
- icon-cog
- icon-comment
- icon-console
- icon-dashboard
- icon-database
- icon-delete
- icon-drawer
- icon-edit
- icon-filter
- icon-folder
- icon-form
- icon-help
- icon-home
- icon-image
- icon-info
- icon-label
- icon-lightbulb
- icon-list
- icon-livefeed
- icon-locked
- icon-mail
- icon-mobile
- icon-new-ticket
- icon-paperclip
- icon-power
- icon-script
- icon-search
- icon-sort-ascending
- icon-star
- icon-star-empty
- icon-tab
- icon-trash
- icon-tree
- icon-tree-right
- icon-user
- icon-user-group
- icon-view

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.addDecoration('caller_id', 'icon-star', 'preferred member');
```

## GlideForm - addDecoration(String fieldName, String icon, String title, String color)

Adds an icon on a field's label.

Adding the same item twice is prevented; however, you can add the same icon with a different title.

**Note:** This method is not supported by Service Catalog.

| Name      | Type   | Description                                                                                                  |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| fieldName | String | Field name.                                                                                                  |
| icon      | String | Name of the icon to show next to the specified field. See [valid decoration icons](#valid-decoration-icons). |
| title     | String | Title for the icon.                                                                                          |
| color     | String | CSS color.                                                                                                   |

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.addDecoration('caller_id', 'icon-star', 'Mark as Favorite', 'color-green');
```

## GlideForm - addErrorMessage(String message)

Displays the specified error message at the top of the form.

This message appears for approximately four seconds and then disappears. This timeout is not configurable at this time.

| Name    | Type   | Description         |
| ------- | ------ | ------------------- |
| message | String | Message to display. |

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.addErrorMessage('This is an error');
```

## GlideForm - addFormMessage(String message, String type, Object options)

Displays a floating form message at the top of the form detail section. The message doesn't cover UI actions.

See also:

- [clearAllFormMessages()](glide-form-client.md)
- [clearFormMessages()](glide-form-client.md)

| Name                       | Type   | Description                                                                                                                                                                                                                                                                                                                         |
| -------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| message                    | String | Message to display.                                                                                                                                                                                                                                                                                                                 |
| type                       | String | Type of message. Valid values: error, info, warning.                                                                                                                                                                                                                                                                                |
| options                    | Object | Optional. Buttons to add to the form message and any metadata needed to handle a button click. See the options example below.                                                                                                                                                                                                       |
| options.buttons            | Array  | List of buttons to add to the form message. See the options.buttons example below.                                                                                                                                                                                                                                                  |
| options.buttons.actionName | String | Name used by the `FORM_MESSAGE_BUTTON_CLICKED` event handlers to determine the button that was clicked. For example, if you add a button with the **actionName** `assign_to_me`, you must create an event handler in UIB on the `FORM_MESSAGE_BUTTON_CLICKED` event that only executes when the **actionName** is `assigned_to_me`. |
| options.buttons.label      | String | Text to display on the button.                                                                                                                                                                                                                                                                                                      |
| options.meta               | Object | Map of any metadata needed to handle the button click formatted as key-value pairs. See the options.meta example below. For example, for an **Assign to me** button the event handler needs the sys_id of the user to assign the record to.                                                                                         |

**options example**

```
{
  buttons: [Array],
  meta: {Object}
}
```

**options.buttons example**

```
buttons: [
  {
    actionName: "String",
    label: "String"
  }
]
```

**options.meta example**

```
meta: {
  'key': 'value'
}
```

| Type | Description |
| ---- | ----------- |
| None |             |

The following example shows how to add form messages of each type.

```
g_form.addFormMessage('info message','info');
g_form.addFormMessage('warning message','warning');
g_form.addFormMessage('error message','error');
g_form.addFormMessage('info2 message','info');
g_form.addFormMessage('warning2 message','warning');
g_form.addFormMessage('error2 message','error');
g_form.addFormMessage('Would you like to reassign this to yourself?', 'info', {buttons: [{label: "Assign to me", actionName: "assign_to_me"}], meta: {'userId': '46d44a23a9fe19810012d100cca80666'}});
```

## GlideForm - addHighMessage(String message)

Displays a high priority message at the top of the form.

This message appears for approximately four seconds and then disappears. This timeout is not configurable at this time.

| Name    | Type   | Description                                   |
| ------- | ------ | --------------------------------------------- |
| message | String | High priority message to display on the form. |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example shows how to display a high priority message at the top of the form.

```
g_form.addHighMessage("This is a high priority message");
```

## GlideForm - addInfoMessage(String message)

Adds the specified informational message to the top of the form.

This message appears for approximately four seconds and then disappears. This timeout is not configurable at this time.

| Name    | Type   | Description         |
| ------- | ------ | ------------------- |
| message | String | Message to display. |

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.addInfoMessage('The top five fields in this form are mandatory');
```

## GlideForm - addLowMessage(String message)

Displays a low priority message at the top of the form.

This message appears for approximately four seconds and then disappears. This timeout is not configurable at this time.

| Name    | Type   | Description                                  |
| ------- | ------ | -------------------------------------------- |
| message | String | Low priority message to display on the form. |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example shows how to display a low priority message at the top of the form.

```
g_form.addLowMessage(“This is a low priority message");
```

## GlideForm - addModerateMessage(String message)

Displays a moderate level priority message at the top of the form.

This message appears for approximately four seconds and then disappears. This timeout is not configurable at this time.

| Name    | Type   | Description                                       |
| ------- | ------ | ------------------------------------------------- |
| message | String | Moderate priority message to display on the form. |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example shows how to display a moderate priority message at the top of the form.

```
g_form.addModerateMessage("This is a moderate priority message");
```

## GlideForm - addOption(String fieldName, String choiceValue, String choiceLabel)

Adds a choice to the end of a specified choice list field.

| Name        | Type   | Description                                                |
| ----------- | ------ | ---------------------------------------------------------- |
| fieldName   | String | Name of the field in which to add the choice field option. |
| choiceValue | String | Value to store in the database.                            |
| choiceLabel | String | Value to display.                                          |

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.addOption('priority', '6', '6 - Really Low');
```

## GlideForm - addOption(String fieldName, String choiceValue, String choiceLabel, Number choiceIndex)

Adds a choice to the list field at the position specified.

**Note:** Duplicate list labels are not supported in Service Portal. For example, items with label text matching another label are ignored and not added to the list.

| Name        | Type   | Description                                                       |
| ----------- | ------ | ----------------------------------------------------------------- |
| fieldName   | String | Name of the field in which to add the choice field option.        |
| choiceValue | String | Value to store in the database.                                   |
| choiceLabel | String | Value to display.                                                 |
| choiceIndex | Number | Order of the choice in the list. The index is a zero-based array. |

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.addOption('priority', '2.5', '2.5 - Moderately High', 3);
```

## GlideForm - addSuccessMessage(String message)

Displays a success message at the top of the form.

This message appears for approximately four seconds and then disappears. This timeout is not configurable at this time.

| Name    | Type   | Description                             |
| ------- | ------ | --------------------------------------- |
| message | String | Success message to display on the form. |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example shows how to display a message confirming a success message at the top of the form.

```
g_form.addSuccessMessage("This is a success message");
```

## GlideForm - clearAllFormMessages()

Removes all form messages of any type.

See also:

- [addFormMessage()](glide-form-client.md)
- [clearFormMessages()](glide-form-client.md)

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example shows how to clear all messages from the form.

```
g_form.clearAllFormMessages();
```

## GlideForm - clearFormMessages(String type)

Removes all form messages of a specified type.

See also:

- [addFormMessage()](glide-form-client.md)
- [clearAllFormMessages()](glide-form-client.md)

| Name | Type   | Description                                          |
| ---- | ------ | ---------------------------------------------------- |
| type | String | Type of message. Valid values: error, info, warning. |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example shows how to clear all error messages from the form.

```
g_form.clearFormMessages('error');
```

## GlideForm - clearMessages()

Removes all informational and error messages from the top of the form.

Removes informational and error messages added with g_form.addInfoMessage() and g_form.addErrorMessage().

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.clearMessages();
```

## GlideForm - clearOptions(String fieldName)

Removes all options from the specified choice list.

| Name      | Type   | Description                                              |
| --------- | ------ | -------------------------------------------------------- |
| fieldName | String | Name of the field for which to clear the choice options. |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - clearValue(String fieldName)

Removes any value(s) from the specified field.

**Note:** This method can't be used to update fields set to strict read only. If this method is called on strict read only fields, the field isn't updated and a warning is logged in the browser console. For more information, see Configuring read-only security options.

| Name      | Type   | Description                 |
| --------- | ------ | --------------------------- |
| fieldName | String | Name of the field to clear. |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - disableAttachments()

Prevents file attachments from being added to the form.

This method is not available on the mobile platform. If this method is run on a mobile platform, no action occurs.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - disableChoice(String fieldName, String choiceValue)

Programmatically turns off a specific choice in the drop-down field, if the choice exists. No changes are made if the choice is already turned off.

| Name        | Type   | Description                                             |
| ----------- | ------ | ------------------------------------------------------- |
| fieldName   | String | Field name of the choice to turn off. Data type: String |
| choiceValue | String | Value of the choice to turn off. Data type: String      |

| Type    | Description                                                                                                                                                                                         |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Boolean | Flag that indicates whether the given choice is turned off or active in the form. Valid values: true: Choice is turned off. false: Option is already turned off or is not found. Data type: Boolean |

The following example calls disableChoice() to turn off the loading_dock choice in the delivery_location form field.

```
if (g_form.getValue('address_type') == 'home') {
	g_form.disableChoice('delivery_location', 'loading_dock');
}

// Only itil_admin users can select the "Closed" option

function onLoad() {
	if (g_user.hasRole('itil_admin')) return;

	if (g_form.getValue('incident_state') != '7')
		g_form.disableChoice('incident_state', 7);

	if (g_form.getValue('state') != '7') {
		g_form.disableChoice('state', 7);
	}

}
```

## GlideForm - enableAttachments()

Allows file attachments to be added to the form. Shows the paper clip icon.

This method is not available on the mobile platform. If this method is run on a mobile platform, no action occurs.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - enableChoice(String fieldName, String choiceValue)

Programmatically enables a specific choice in the drop-down field, if the choice exists. No changes are made if the option is already enabled.

| Name        | Type   | Description                         |
| ----------- | ------ | ----------------------------------- |
| fieldName   | String | Field name of the choice to enable. |
| choiceValue | String | Value of the choice to enable.      |

| Type    | Description                                                                                                                                                                       |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Boolean | Flag that indicates whether the given choice is successfully enabled. Valid values: true: Choice is enabled. false: Choice is already enabled or is not found. Data type: Boolean |

The following example calls enable() to enable a new drop-down choice, `1`, in the `priority` form field.

```
var shortDescription = g_form.getValue('shortDescription');

// Allow priority 1 selection if short description mentions security
if (shortDescription.includes('security')) {
	var p1Choice = g_form.getChoice('priority', '1');
	g_form.enableChoice('priority', '1');
}
```

## GlideForm - flash(String fieldName, String color, Number count)

Use to draw attention to a field. Flashes the specified color for a specified duration of time in the specified field.

This method is not supported by Service Catalog.

This method is not available on the mobile platform. If this method is run on a mobile platform, no action occurs.

| Name      | Type   | Description                                                                |
| --------- | ------ | -------------------------------------------------------------------------- |
| fieldName | String | Field to highlight in the following format: `"<table-name>.<field-name>"`. |
| color     | String | RGB color or acceptable CSS color.                                         |
| count     | Number | How long the label will flash.                                             |

**count:**

Valid values:

- 2: Flashes for 1 second
- 0: Flashes for 2 seconds
- -2: Flashes for 3 seconds
- -4: Flashes for 4 seconds

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.flash("incident.number", "#FFFACD", 0);
```

## GlideForm - getActionName()

Returns the most recent action name, or, for a client script, the sys_id of the UI action clicked.

**Note:** Not available in Wizard client scripts.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type   | Description                                             |
| ------ | ------------------------------------------------------- |
| String | Current action name or sys_id of the UI action clicked. |

```
function onSubmit() {
   var action = g_form.getActionName();
   alert('You pressed ' + action);
}
```

## GlideForm - getAnnotationByName(String name)

Returns a form annotation of a given name.

Annotations are visual separators between form elements, or blocks of colored text used to highlight form elements. Use [GlideForm - getAnnotationByName(String name)](glide-form-client.md) to return all annotations in a form.

| Name | Type   | Description                                                                                        |
| ---- | ------ | -------------------------------------------------------------------------------------------------- |
| name | String | The name of the annotation to return. Table: Form Annotations [sys_ui_annotation], Field: **Name** |

| Property         | Description                                                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Array of Objects | Content of the annotation. Data type: Array of Objects. See the Array of Objects example below.                                                                           |
| array.content    | Text of the returned annotation. Data type: String                                                                                                                        |
| array.name       | Name of the returned annotation. Data type: String. Table location: Form Annotations [sys_ui_annotation], Field: **name**                                                 |
| array.visible    | Flag that indicates whether the annotation is visible on the form. Valid values: true: The annotation is visible. false: The annotation isn't visible. Data type: Boolean |

**Array of Objects example**

```
[{content: "String", name: "String", visible: Boolean}]
```

The following example demonstrates how to use the getAnnotationByName() method to retrieve a form annotation according to its given name, test-annotation-msg-1.

```
   var sampleAnnotation = g_form.getAnnotationByName("test-annotation-msg-1");

   /* returns:
   {
       "name": "test-annotation-msg-1",
       "visible": true,
       "content": "Test<input id=\"make_spacing_ok\" style=\"visibility:hidden; width:0px;\">"
   }
   */
```

## GlideForm - getAnnotations()

Returns a list of all annotations on a form.

Annotations are visual separators between form elements, or blocks of colored text used to highlight form elements. Use [GlideForm - getAnnotationByName(String name)](glide-form-client.md) to return a specific annotation by its name.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Property         | Description                                                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Array of Objects | Content of the annotation. Data type: Array of Objects. See the Array of Objects example below.                                                                           |
| array.content    | Text of the returned annotation. Data type: String                                                                                                                        |
| array.name       | Name of the returned annotation. Data type: String. Table location: Form Annotations [sys_ui_annotation], Field: **name**                                                 |
| array.visible    | Flag that indicates whether the annotation is visible on the form. Valid values: true: The annotation is visible. false: The annotation isn't visible. Data type: Boolean |

**Array of Objects example**

```
[{content: "String", name: "String", visible: Boolean}]
```

The following example first calls getAnnotations() to return all annotations in a form, and then calls hideAnnotation() to hide all annotations in the form.

```
const annotations = getAnnotations();

/* returns:
[
    {
        "name": "test-annotation-msg-1",
        "visible": true,
        "content": "Test<input id=\"make_spacing_ok\" style=\"visibility:hidden; width:0px;\">"
    },
    {
        "name": "test-annotation-msg-2",
        "visible": true,
        "content": "Test 2<input id=\"make_spacing_ok\" style=\"visibility:hidden; width:0px;\">"
    }

]*/
annotations.forEach(function(annotation) {
	g_form.hideAnnotation(annotation.name);
});

// this script hides all annotations on the form.
```

## GlideForm - getBooleanValue(String fieldName)

Returns a Boolean value for the specified field.

| Name      | Type   | Description                                                                |
| --------- | ------ | -------------------------------------------------------------------------- |
| fieldName | String | Field to highlight in the following format: `"<table-name>.<field-name>"`. |

| Type    | Description                                                                     |
| ------- | ------------------------------------------------------------------------------- |
| Boolean | Returns false if the field value is false or undefined; otherwise returns true. |

## GlideForm - getChoice(String fieldName, String choiceValue)

Returns an object with properties representing a given field and choice value.

| Name        | Type   | Description                           |
| ----------- | ------ | ------------------------------------- |
| fieldName   | String | Field name of the choice to retrieve. |
| choiceValue | String | Value of the choice to retrieve.      |

| Property                       | Description                                                                                                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GlideFormChoice object or null | GlideFormChoice object for the specified field and choice value. Returns null if no matching choice exists. Data type: Object. See the GlideFormChoice object or null example below. |
| GlideFormChoice.label          | Read-only display text of the choice. Data type: String                                                                                                                              |
| GlideFormChoice.value          | Read-only value of the choice. Data type: String                                                                                                                                     |
| GlideFormChoice.disabled       | Flag that indicates whether the choice is turned off in the form. Valid values: true: Choice is turned off. false: Choice is enabled. Data type: Boolean                             |
| GlideFormChoice.index          | Indicates the position of the choice in the drop-down. Data type: Number                                                                                                             |

**GlideFormChoice object or null example**

```
("label", "value", "disabled", "index")
```

The following example calls enable() to enable a new drop-down choice, `1`, in the `priority` form field.

```
var shortDescription = g_form.getValue('shortDescription');

// Allow priority 1 selection if short description mentions security
if (shortDescription.includes('security')) {
	var p1Choice = g_form.getChoice('priority', '1');
	g_form.enableChoice('priority', '1');
}
```

## GlideForm - getControl(String fieldName)

Returns the HTML element for the specified field.

Compound fields may contain several HTML elements. This method is generally not necessary as there are built-in methods that use the fields on a form.

If the field is a reference field and the control is a choice list, getControl() may not return a control as expected. In this case, use `sys_select.<table name>.<field name>`.

This method is not available in mobile scripts or Service Portal scripts.

| Name      | Type   | Description                                             |
| --------- | ------ | ------------------------------------------------------- |
| fieldName | String | Name of the field for which to return the HTML element. |

| Type        | Description           |
| ----------- | --------------------- |
| HTMLElement | Field's HTML element. |

## GlideForm - getDecimalValue(String fieldName)

Returns the decimal value of the specified field.

| Name      | Type   | Description                                              |
| --------- | ------ | -------------------------------------------------------- |
| fieldName | String | Name of the field for which to return the decimal value. |

| Type   | Description                           |
| ------ | ------------------------------------- |
| String | Decimal value of the specified field. |

```
function onChange(control, oldValue, newValue, isLoading) {
   alert(g_form.getDecimalValue('percent_complete'));
}
```

## GlideForm - getDisplayBox(String fieldName)

Returns the display value from a form in the core UI.

**Note:** To get a display value from a form in Service Portal, use the [getDisplayValue()](glide-form-client.md) method.

See also:

- [getValue()](glide-form-client.md)
- [Get the display value of a reference variable](https://www.servicenow.com/community/developer-blog/get-display-value-of-reference-variable-service-catalog/ba-p/2287763)

| Name      | Type   | Description |
| --------- | ------ | ----------- |
| fieldName | String |             |

| Type | Description                                                     |
| ---- | --------------------------------------------------------------- |
| None | Name of the field from which to retrieve the value in the form. |

```
var caller = g_form.getDisplayBox('caller_id').value;

var assignee = g_form.getDisplayBox('assigned_to').value;

if (caller == assignee)
{
   alert('in');
}
```

## GlideForm - getDisplayValue(String fieldName)

Returns the display value from a form in Service Portal.

See also:

- [getValue()](glide-form-client.md)
- [Get the display value of a reference variable](https://www.servicenow.com/community/developer-blog/get-display-value-of-reference-variable-service-catalog/ba-p/2287763)

**Note:** In the core UI, calling this method as `g_form.getDisplayValue()` without an argument returns the record display value rather than the display value of an individual field.

| Name      | Type   | Description                                                            |
| --------- | ------ | ---------------------------------------------------------------------- |
| fieldName | String | Name of the field from which you want to retrieve a value in the form. |

| Type   | Description                           |
| ------ | ------------------------------------- |
| String | Display value of the specified field. |

The following example shows how to get the display value of a reference variable in the core UI or Service Portal. The use case for this example is on the [community](https://www.servicenow.com/community/developer-blog/get-display-value-of-reference-variable-service-catalog/ba-p/2287763) site.

```
function onChange(control, oldValue, newValue, isLoading) {
     if (isLoading || newValue == '') {
          return;
     }
     if(window == null){
          var valuePortal = g_form.getDisplayValue('requester');
          alert('Portal->' + valuePortal);
     }
     else{
          var valueNative = g_form.getDisplayBox('requester').value;
          alert('CoreUI->' + valueCoreUI);
     }
     //Type appropriate comment here, and begin script below
}
```

## GlideForm - getElement(String id)

Returns the HTML element specified by the parameter.

Compound fields may contain several HTML elements. This method is generally not necessary as there are built-in methods that use the fields on a form.

This method is not available in mobile scripts or Service Portal scripts.

| Name | Type   | Description |
| ---- | ------ | ----------- |
| id   | String | Field ID.   |

| Type        | Description           |
| ----------- | --------------------- |
| HTMLElement | Field's HTML element. |

## GlideForm - getFormElement()

Returns the HTML element for the form.

This method is not available in mobile scripts or Service Portal scripts.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type            | Description                |
| --------------- | -------------------------- |
| HTMLFormElement | HTML element for the form. |

## GlideForm - getHelpTextControl(String fieldName)

Returns the HTML element of the help text for the specified field.

This method is applicable to service catalog variables only.

| Name      | Type   | Description        |
| --------- | ------ | ------------------ |
| fieldName | String | Name of the field. |

| Type        | Description                     |
| ----------- | ------------------------------- |
| HTMLElement | Help text field's HTML element. |

## GlideForm - getIntValue(String fieldName)

Returns the integer value for the specified field.

| Name      | Type   | Description |
| --------- | ------ | ----------- |
| fieldName | String | Field name. |

| Type   | Description                 |
| ------ | --------------------------- |
| Number | Integer value of the field. |

## GlideForm - getLabelOf(String fieldName)

Returns the plain text value of the field label.

| Name      | Type   | Description |
| --------- | ------ | ----------- |
| fieldName | String | Field name. |

| Type   | Description |
| ------ | ----------- |
| String | Label text. |

```
if (g_user.hasRole('itil')) {
    var oldLabel = g_form.getLabelOf('comments');
    g_form.setLabelOf('comments', oldLabel + ' (Customer visible)');
}
```

## GlideForm - getOption(String fieldName, String choiceValue)

Returns the option element for a selected box named **fieldName** where **choiceValue** matches the option value.

**Note:** This method does not work on read-only fields.

| Name        | Type   | Description          |
| ----------- | ------ | -------------------- |
| fieldName   | String | Name of the field.   |
| choiceValue | String | Value of the option. |

| Type        | Description                                                                       |
| ----------- | --------------------------------------------------------------------------------- |
| HTMLElement | The HTMLElement for the option. Returns null if the field or option is not found. |

The following example shows how to get the label for a choice list value.

```
// Get the label for a choice list value
// fieldName is 'category'

function onChange(control, oldValue, newValue, isLoading) {
var choiceValue = g_form.getValue('category');
var choiceLabel = g_form.getOption('category', choiceValue).text;
}
```

## GlideForm - getOptions(String fieldName)

Returns the available and selected options for a choice or reference field on the form. This method is useful for dynamic forms, catalog variables and variable sets, and integrations needing to inspect or filter field options at runtime.

For example, you can use the g_form.getOptions() to:

- Get and set the name-value pairs in a watch_list field type.
- Search or filter available options by a search term.
- Enable access to the same auto-complete results via a callback.
- Get and set options on choice fields, reference fields, and advanced field types such as watch_list, glide_list, field_list, and slushbucket.

| Name      | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| fieldName | String | The field name of the choice or reference field to retrieve. |

| Property                 | Description                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Array of Objects or null | Read-only array of objects containing the value and label of each selected option. Returns null if the field does not support options. Data type: Array of Objects. See the Array of Objects or null example below.                                                                                                                       |
| array.displayValue       | The choice display value. Data type: String                                                                                                                                                                                                                                                                                               |
| array.value              | The value of the option. Data type: String                                                                                                                                                                                                                                                                                                |
| getAvailable(term)       | Function for returning all available options. A search term can be provided as an argument to filter the options by display value (a case-insensitive sub string match). Returns a Promise of Array of Objects with the matching choice's display value and value. Data type: Array of Objects. See the getAvailable(term) example below. |

**Array of Objects or null example**

```
[{value: "String", displayValue: "String"}]
```

**getAvailable(term) example**

```
[{value: "String", displayValue: "String"}]
```

The following example calls g_form.getOptions() to return all available choices for specified form fields, like state, work_notes_list, and others.

```
g_form.getOptions("state"); //table: incident, field: state, type: integer, choice: Dropdown without --None--
/*
returns [{"value":"1","displayValue":"New"},{"value":"2","displayValue":"In Progress"},{"value":"3","displayValue":"On Hold"},{"value":"6","displayValue":"Resolved"},{"value":"7","displayValue":"Closed"},{"value":"8","displayValue":"Canceled"}]
*/

g_form.getOptions("category"); //table: incident, field: category, type: string, choice: Dropdown with --None--
/*
returns [{"value":"","displayValue":"-- None --"},{"value":"inquiry","displayValue":"Inquiry / Help"},{"value":"software","displayValue":"Software"},{"value":"hardware","displayValue":"Hardware"},{"value":"network","displayValue":"Network"},{"value":"database","displayValue":"Database"}]
*/

g_form.getOptions("work_notes_list") //table: incident, field: work_notes_list, type: glide_list
/*
returns [{"value":"62826bf03710200044e0bfc8bcbe5df1","displayValue":"Abel Tuter"},{"value":"a8f98bb0eb32010045e1a5115206fe3a","displayValue":"Abraham Lincoln"},{"value":"5137153cc611227c000bbd1bd8cd2005","displayValue":"Fred Luddy"},{"value":"6a826bf03710200044e0bfc8bcbe5dec","displayValue":"Alissa Mountjoy"}]
*/

g_form.getOptions("restricted_fields") //table: std_change_properties, field: restricted_fields, type: field_list
/*
[{"value":"activity_due","displayValue":"Activity due"},{"value":"additional_assignee_list","displayValue":"Additional assignee list"},{"value":"comments","displayValue":"Additional comments"},{"value":"assignment_group","displayValue":"Assignment group"},{"value":"backout_plan","displayValue":"Backout plan"},{"value":"business_duration","displayValue":"Business duration"},{"value":"cab_delegate","displayValue":"CAB delegate"},...]
*/

g_form.getOptions('table') //table: sys_script_client, field: table, type: table_name
/*
[{"value":"","displayValue":"-- None --"},{"value":"cmdb_ci_appl_dot_net","displayValue":".NET Application [cmdb_ci_appl_dot_net]"},{"value":"evaluation","displayValue":"A/B Testing Evaluation [evaluation]"},{"value":"evaluation_execution","displayValue":"A/B Testing Evaluation Execution [evaluation_execution]"},{"value":"evaluation_parameter","displayValue":"A/B Testing Evaluation Parameter [evaluation_parameter]"},{"value":"sn_access_analyzer_request","displayValue":"Access Analyzer Query [sn_access_analyzer_request]"},{"value":"sn_access_analyzer_access_comparison_request","displayValue":"Access Comparison Request [sn_access_analyzer_access_comparison_request]"},{"value":"sys_security_acl","displayValue":"Access Control [sys_security_acl]"},...]
*/

g_form.getOptions('mandatory_fields'); //table: kb_knowledge_base, field: mandatory_fields, type: slushbucket
/*
[{"value":"active","displayValue":"Active"},{"value":"article_id","displayValue":"Article ID"},{"value":"displayValue","displayValue":"Article body"},{"value":"article_type","displayValue":"Article type"},{"value":"direct","displayValue":"Attachment link"},{"value":"author","displayValue":"Author"},{"value":"base_version","displayValue":"Base Version"},...]
*/
```

The following example script demonstrates how to call g_form.getOptions() with getAvailable() function.

```
const options = g_form.getOptions('priority');
if (options) {
  console.log('Selected:', options.selected);
  options.getAvailable('high').then(available => {
    console.log('Available matching "high":', available);
  });
}
```

## GlideForm - getReference(String fieldName, Function callBack)

Returns the GlideRecord for a specified field.

If a callback function is present, this routine runs asynchronously. The browser (and script) processing continues normally until the server returns the reference value, at which time, the callback function is invoked. If a callback function is not present, this routine runs synchronously and processing halts (causing the browser to appear to hang) while waiting on a server response.

**Important:** It is strongly recommended that you use a callback function.

Callback function support for ServiceCatalogForm.getReference is available.

**Note:** Using this method requires a call to the server which requires additional time and may introduce latency to your page. Use this method with caution. For additional information, see [Client script design and processing](scripts/client-script-best-practices.md).

| Name      | Type     | Description                     |
| --------- | -------- | ------------------------------- |
| fieldName | String   | Name of the field.              |
| callBack  | Function | Name of the call back function. |

| Type        | Description                                                                                                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GlideRecord | GlideRecord object for the specified field. If the specified reference can't be found, it returns an initialized GlideRecord object where `currentRow = -1` and `rows.length = 0`. |

```
function onChange(control, oldValue, newValue, isLoading) {
    g_form.getReference('caller_id', doAlert); // doAlert is our callback function
}

function doAlert(caller) { // reference is passed into callback as first arguments
   if (caller.getValue('vip') == 'true') {
      alert('Caller is a VIP!');
   }
}
```

## GlideForm - getRelatedListNames()

Returns an array of related list names from the current form.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type             | Description                                                                                                                        |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Array of Strings | List of related list names from the current form. The related list names are listed in the order in which they appear on the form. |

```
var listNames = g_form.getRelatedListNames();

for (var i = 0; i < listNames.length; i++) {
  this.showRelatedList(listNames[i]);
 }
```

## GlideForm - getSectionNames()

Returns all section names, whether visible or not.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type             | Description    |
| ---------------- | -------------- |
| Array of Strings | Section names. |

## GlideForm - getSections()

Returns an array of the form's sections.

This method is not available on the mobile platform. If this method is run on a mobile platform, no action occurs.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type                   | Description      |
| ---------------------- | ---------------- |
| Array of HTML elements | Form's sections. |

```
function onChange(control, oldValue, newValue, isLoading) {
   //this example was run on a form divided into sections (Change form)
   // and hid a section when the "state" field was changed
   var sections = g_form.getSections();
   if (newValue == '2') {
      g_form.setSectionDisplay(sections[1], false);
   } else {
      g_form.setSectionDisplay(sections[1], true);
   }
}
```

## GlideForm - getTableName()

Returns the name of the table to which this record belongs.

On the server side, the table for the current record can be retrieved with current.sys_class_name or current.getTableName().

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type   | Description        |
| ------ | ------------------ |
| String | Name of the table. |

```
function onLoad() {
    if (g_form.isNewRecord()) {
        var tableName = g_form.getTableName(); //Get the table name
    }
}
```

## GlideForm - getUniqueValue()

Returns the sys_id of the record displayed in the form.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type   | Description      |
| ------ | ---------------- |
| String | Record's sys_id. |

```
function onLoad() {
   var incSysid = g_form.getUniqueValue();
   alert(incSysid);
}
```

## GlideForm - getValue(String fieldName)

Returns the value of the specified form field.

This method also supports getting values from a multi-row variable set (MRVS). To obtain data from fields within an MRVS, you must first use `JSON.parse(getValue('<mrvs_field_name>') || '[]')` to obtain the MRVS array, and then use indexing to access the fields within the row objects. For more details, see the code example below.

| Name      | Type   | Description                              |
| --------- | ------ | ---------------------------------------- |
| fieldName | String | Name of the field whose value to return. |

| Type   | Description                   |
| ------ | ----------------------------- |
| String | Value of the specified field. |

The following example shows how to get the short description from the current form.

```
function onChange(control, oldValue, newValue, isLoading) {
   alert(g_form.getValue('short_description'));
}
```

The following example shows how to get values from an MRVS. In this example, salaries are being managed through the Service Catalog. The client script searches all rows within the MRVS for the value entered in the **Job title** and then updates the matching entries within the MRVS with what is entered in the **Salary** field. The MRVS is named "variable_set_1" and contains the following fields within each row object: Employee name [employee_name], Job title [employee_job_title], and Salary [employee_salary]. In addition, the Catalog Item contains: Job title [job_title] and Salary [salary].

```
function onChange(control, oldValue, newValue, isLoading) {
if (isLoading || newValue == '') {
return;
}

// Get the MRVS
var vs1 = g_form.getValue('variable_set_1') || '[]';
var multiRowVariableSet = JSON.parse(vs1);

for (var i = 0; i < multiRowVariableSet.length; i++) {
// Check if the entered job title matches the title in the current MRVS row
  if (multiRowVariableSet[i].employee_job_title == g_form.getValue("job_title")){
    // Update the value of a matching field with the new salary
    multiRowVariableSet[i].employee_salary = newValue;
  }
}

// Update the MRVS
g_form.setValue('variable_set_1', JSON.stringify(multiRowVariableSet));
}
```

## GlideForm - hideAllFieldMsgs()

Hides all field messages.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - hideAllFieldMsgs(String type)

Hides all field messages of the specified type.

| Name | Type   | Description                                 |
| ---- | ------ | ------------------------------------------- |
| type | String | Type of message. Valid values: error, info. |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - hideAnnotation(String name)

Hides an annotation with a given name on the form UI.

Annotations are visual separators between form elements, or blocks of colored text used to highlight form elements. See also:

- [GlideForm - showErrorBox(String name, String message, Boolean scrollForm)](glide-form-client.md) to display a specific annotation on the form.
- [GlideForm - toggleAnnotations()](glide-form-client.md) to toggle annotations on and off with greater flexibility.

| Name | Type   | Description                                                                                              |
| ---- | ------ | -------------------------------------------------------------------------------------------------------- |
| name | String | Name of the annotation to hide in the form. Table: Form Annotations [sys_ui_annotation], Field: **Name** |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example demonstrates how to programmatically hide the annotation named test-annotation-msg-1 on the form field using the hideAnnotation() method.

```
g_form.hideAnnotation('test-annotation-msg-1');
```

## GlideForm - hideErrorBox(String fieldName)

Hides the error message placed by showErrorBox().

Whenever possible, use hideFieldMsg() rather than this method whenever possible.

| Name      | Type   | Description                                               |
| --------- | ------ | --------------------------------------------------------- |
| fieldName | String | Name of the field or control whose error message to hide. |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - hideFieldMsg(String fieldName, Boolean clearAll)

Hides the first message that appears in the specified field on the current form.

Use the [GlideForm - showFieldMsg(String field, String message, String type)](glide-form-client.md) or [GlideForm - showFieldMsg(String field, String message, String type, Boolean scrollForm)](glide-form-client.md) methods to display messages on a form.

For example, the following code snippet shows how to display two messages on the `work_notes` field of a form and then hide the first message:

```
g_form.showFieldMsg('work_notes', 'First message', "error");
g_form.showFieldMsg('work_notes', 'Second message', "error");
g_form.hideFieldMsg('work_notes', false); // This call hides the 'First message'
```

| Name      | Type    | Description                                                                                                                                                                                   |
| --------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fieldName | String  | Name of the field on which to hide the message.                                                                                                                                               |
| clearAll  | Boolean | Optional. Flag that indicates whether to hide all messages for the specified field. Valid values: true: Hide all messages. false: Only hide the first message being displayed. Default: false |

| Type | Description |
| ---- | ----------- |
| void |             |

The following example shows how to clear all messages for a specified form field and then display an encryption error message.

```
function submitEncryptedInputs() {
  return processEncryptedInputs(function(inputName, fieldName) {
    if (!checkEncryptedFieldValue(fieldName)) {
      g_form.hideFieldMsg(fieldName, true); // Hide all messages for the specified field
      g_form.showFieldMsg(fieldName, "Your activity requires an encrypted input.", "error");
      return false;
    }
    return true;
  });
}
```

## GlideForm - hideRelatedLinks()

Hides the Related Links section of a form.

See also:

- [GlideForm - showRelatedLinks()](glide-form-client.md)
- [GlideForm - setRelatedLinksDisplay(Boolean display)](glide-form-client.md)

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example script hides related links in the current form.

```
// Hide related links
g_form.hideRelatedLinks()
```

## GlideForm - hideRelatedList(String listTableName)

Hides the specified related list on the form.

This method is not available on the mobile platform. If this method is run on a mobile platform, no action occurs.

| Name          | Type   | Description                                                                     |
| ------------- | ------ | ------------------------------------------------------------------------------- |
| listTableName | String | Name of the related list. Use the sys_id to hide a list through a relationship. |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - hideRelatedLists()

Hides all related lists on the form.

This method is not available on the mobile platform. If this method is run on a mobile platform, no action occurs.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - hideTemplateBar()

Hides the template bar on the form.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example script hides the Template Bar on the current form.

```
g_form.hideTemplateBar()
```

## GlideForm - isLiveUpdating()

Returns true while a live update is being done on the record the form is showing.

This can be used in an onChange() client script to determine if a change to the record is because of a live update from another session. The client script can then decide what action to take, or not to take. This applies to systems using Core UI with live forms enabled.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type    | Description                                                                     |
| ------- | ------------------------------------------------------------------------------- |
| Boolean | Returns true if a live update is happening on the record displayed by the form. |

## GlideForm - isMandatory(String fieldName)

Returns true if the field is mandatory.

Mandatory fields are visually distinguished by an asterisk next to the field label. The asterisk is red if the field is empty, and black if the field is not empty. The system displays a validation message if a user attempts to save or submit the form without completing those fields. For more information, see Form fields.

| Name      | Type   | Description        |
| --------- | ------ | ------------------ |
| fieldName | String | Name of the field. |

| Type    | Description                                     |
| ------- | ----------------------------------------------- |
| Boolean | True if the field is required, false otherwise. |

## GlideForm - isNewRecord()

Returns true if the record has never been saved.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type    | Description                                                     |
| ------- | --------------------------------------------------------------- |
| Boolean | Returns true if the record has not been saved; otherwise false. |

```
function onLoad() {
   if(g_form.isNewRecord()){
      alert('New Record!');
   }
}
```

## GlideForm - isSectionVisible(String sectionName)

Returns true if the section is visible.

**Important:** The isSectionVisible() function is not supported in Workspace.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type    | Description                                                             |
| ------- | ----------------------------------------------------------------------- |
| Boolean | Returns true when the section is visible; otherwise, false is returned. |

## GlideForm - isVisible(String fieldName)

Determines whether the field associated with the passed-in field name is visible on the current form.

| Name      | Type   | Description                                                           |
| --------- | ------ | --------------------------------------------------------------------- |
| fieldName | String | Name of the field to check whether it is visible on the current form. |

| Type    | Description                                                                                                                                                                  |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Boolean | Flag that indicates whether the specified field is visible on the current form. Possible values: true: Field is visible on the form. false: Field isn't visible on the form. |

The following code example shows how to check if the `user_address` field is visible on the current form.

```
if(g_form.isVisible('user_address')) {
    alert('is visible');
}
else {
    alert('is hidden');
}
```

## GlideForm - onUserChangeValue(Function fn)

Registers a custom event listener that detects when any field in the current form is modified by a user.

When a form field is modified, the event listener calls the function that is passed in when the listener is initially registered. This listener is only triggered when a user makes a change to a field on the form. Changes from client scripts, UI policies, or any other non-user interactions, do not trigger the listener.

**Note:** This method does not work for journal fields or Service Catalog items in the classic environment.

| Name | Type     | Description                                                                                                                                                                                                 |
| ---- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fn   | Function | Function to call when a user changes the value of a field within the current form. This is actually the function code, not just the function name. This function must accept the following three arguments: |

**fn:**

- field name
- original field value
- updated field value

| Type     | Description                                                          |
| -------- | -------------------------------------------------------------------- |
| Function | Function to call to unregister the onUserChangeValue event listener. |

```
var handler = function(fieldname, originalValue, newValue) {
  console.log('The field ('+ fieldname + ') has a new value of: ' + newValue); // function code
}

var unregister = g_form.onUserChangeValue(handler);

// To unregister the event listener
unregister();
```

## GlideForm - refreshSlushbucket(String fieldName)

You can update a list collector variable.

| Name      | Type   | Description               |
| --------- | ------ | ------------------------- |
| fieldName | String | Name of the slush bucket. |

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.refreshSlushbucket('bucket');
```

## GlideForm - removeDecoration(String fieldname, String icon, String title)

Removes the icon from the specified field that matches the specified icon and title.

**Note:** This method isn't supported by Service Catalog.

| Name      | Type   | Description                                     |
| --------- | ------ | ----------------------------------------------- |
| fieldName | String | Field name from which to remove the decoration. |
| icon      | String | Name of the icon to remove.                     |
| title     | String | Icon's text title (name).                       |

| Type | Description |
| ---- | ----------- |
| void |             |

```
function onChange(control, oldValue, newValue, isLoading) {
	// if the caller_id field is not present, then we can't add an icon anywhere
	if (!g_form.hasField('caller_id'))
		return;

	if (!newValue)
		return;

	g_form.getReference('caller_id', function(ref) {
		g_form.removeDecoration('caller_id', 'icon-star', 'VIP');

		if (ref.getValue('vip') == 'true')
			g_form.addDecoration('caller_id', 'icon-star', 'VIP');
	});
}
```

## GlideForm - removeDecoration(String fieldname, String icon, String title, String color)

Removes the icon from the specified field that matches the specified icon, title, and color.

**Note:** This method isn't supported by Service Catalog.

| Name      | Type   | Description                                     |
| --------- | ------ | ----------------------------------------------- |
| fieldName | String | Field name from which to remove the decoration. |
| icon      | String | Name of the icon to remove.                     |
| title     | String | Icon's text title (name).                       |
| color     | String | CSS color to match.                             |

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.removeDecoration('caller_id', 'icon-star', 'VIP', 'blue');
```

## GlideForm - removeOption(String fieldName, String choiceValue)

Removes the specified option from the specified choice list.

| Name        | Type   | Description                                                             |
| ----------- | ------ | ----------------------------------------------------------------------- |
| fieldName   | String | Name of the field from which to remove the option from the choice list. |
| choiceValue | String | Value stored in the database. This is not the label.                    |

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.removeOption('priority', '1');
```

## GlideForm - save()

Saves the record without navigating away (update and stay).

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - setChoiceLabel(String fieldName, String choiceValue, String newLabel)

Updates the label of a specific choice in the drop-down field.

When calling this method, the index position of the updated option in the drop-down remains unchanged. The enabled or turned off state of the option is preserved.

| Name        | Type   | Description                                                             |
| ----------- | ------ | ----------------------------------------------------------------------- |
| fieldName   | String | Field name that contains the choice to update. Data type: String        |
| choiceValue | String | Value of the choice label to update with a new label. Data type: String |
| newLabel    | String | Label name to update the existing choice label to. Data type: String    |

| Type    | Description                                                                                                                                                                                                                                                                                                   |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Boolean | Flag that indicates whether the option label is updated successfully. Valid values: true: Choice label is updated. false: Choice label isn't updated because the specified choice to update may have been read-only or does not exist, or the new label exists and is already associated with another option. |

The following example calls setChoiceLabel() to update the 'bonus' field choices (10, 20, and 30) to new values.

```
// Show the calculated bonus next to the percentage label
var salary = parseInt(g_form.getValue('salary'), 10);
g_form.setChoiceLabel('bonus', '10', '10% ($'+ (salary * .10) +')');
g_form.setChoiceLabel('bonus', '20', '20% ($'+ (salary * .20) +')');
g_form.setChoiceLabel('bonus', '30', '30% ($'+ (salary * .30) +')');
```

## GlideForm - setDisabled(String fieldName, Boolean disable)

Makes the specified field available or unavailable.

| Name      | Type    | Description                                                                                                                                    |
| --------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| fieldName | String  | Name of the field to enable or turn off.                                                                                                       |
| disable   | Boolean | Flag that indicates whether to turn off the specified field. Valid values: true: Turns off the field. false: Enables the field. Default: false |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - setDisplay(String fieldName, Boolean display)

Displays or hides a specified field on the form.

This method can't hide a mandatory field with no value. If the field is hidden, the space is used to display other items. Whenever possible, use a UI policy instead of this method.

| Name      | Type    | Description                                                                                                               |
| --------- | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| fieldName | String  | Name of the field.                                                                                                        |
| display   | Boolean | Flag that indicates whether to display the specified field. Valid values: true: Display the field. false: Hide the field. |

| Type | Description |
| ---- | ----------- |
| void |             |

```
function onChange(control, oldValue, newValue, isLoading, isTemplate) {
   //If the page isn't loading
   if (!isLoading) {
      //If the new value isn't blank
      if (newValue != '') {
         g_form.setDisplay('priority', false);
      }
      else
         g_form.setDisplay('priority', true);
      }
   }
```

## GlideForm - setLabelOf(String fieldName, String label)

Sets the plain text value of the specified field label.

**Note:** This method is not supported by Service Catalog.

| Name      | Type   | Description                                   |
| --------- | ------ | --------------------------------------------- |
| fieldName | String | Name of the field for which to set the label. |
| label     | String | Plain text value to set in the label.         |

| Type | Description |
| ---- | ----------- |
| void |             |

```
if (g_user.hasRole('itil')) {
    var oldLabel = g_form.getLabelOf('comments');
    g_form.setLabelOf('comments', oldLabel + ' (Customer visible)');
}
```

## GlideForm - setMandatory(String fieldName, Boolean mandatory)

Makes the specified field mandatory.

Mandatory fields are visually distinguished by an asterisk next to the field label. The asterisk is red if the field is empty, and black if the field is not empty. The system displays a validation message if a user attempts to save or submit the form without completing those fields. For more information, see Form fields.

**Note:** Whenever possible, use a UI policy rather than this method.

| Name      | Type    | Description                                                                                                                          |
| --------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| fieldName | String  | Name of the field to make mandatory.                                                                                                 |
| mandatory | Boolean | Flag that indicates whether the field is mandatory. Valid values: true: Field is mandatory. false: Field is optional. Default: false |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - setReadOnly(String fieldName, Boolean readOnly)

Makes the specified field read-only or editable.

Whenever possible, use a UI policy instead of this method.

To make a mandatory field read-only, you must first remove the mandatory requirement for that field by using the setMandatory() method.

Once you set a field to read-only, you cannot use the [setValue()](glide-form-client.md) method to update the value of that field. If you need to set the value in this way, you must set the **readOnly** value to `false`.

| Name      | Type    | Description                                                                                                                                             |
| --------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fieldName | String  | Name of the field whose access value to set.                                                                                                            |
| readOnly  | Boolean | Flag that determines whether the associate field is editable or read-only. Valid values: true: Set field to read-only. false: Set field to be editable. |

| Type | Description |
| ---- | ----------- |
| void |             |

The following example shows how set the Variable Editor to read only. To do this in Service Catalog tables, use setVariablesReadOnly().

```
// Create a Client Script on a table (e.g., incident) and paste this script
// Uncheck (set to false) the "isolate script" checkbox (not available by default)
// To add the isolate script checkbox to the form, configure form layout to add the checkbox
function onLoad() {
  $("variable_map").querySelectorAll("item").forEach(function(item){
    var variable = item.getAttribute("qname");
    g_form.setReadOnly("variables."+ variable, true);
  });
}
```

## GlideForm - setRelatedLinksDisplay(Boolean display)

Show or hide the Related Links section in the form UI using Boolean values.

[GlideForm - hideRelatedLinks()](glide-form-client.md) hides related link UI Actions on the form, while [GlideForm - showRelatedLinks()](glide-form-client.md) shows them. The g_form.setRelatedLinksDisplay(boolean: display) method, however, can be used to either show or hide related links with more flexibility in your scripts.

| Name    | Type    | Description                                                                                                                                                                                    |
| ------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| display | Boolean | Flag that indicates whether to show or hide the Related Links section of a form. Valid values: true: Displays related links in the form. false: Hides related links in the form. Default: true |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example demonstrates how to show or hide the Related Links section in a form.

```
// Displays the Related Links section in the UI
g_form.setRelatedLinksDisplay(true);
// Hides the Related Links section in the UI
g_form.setRelatedLinksDisplay(false);
```

## GlideForm - setSectionDisplay(String sectionName, Boolean display)

Shows or hides a specified section in the form.

| Name        | Type    | Description                                                                                                                                                                                                                                                                                                                                   |
| ----------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sectionName | String  | Section name is lower case with an underscore replacing the first space in the name, and with the remaining spaces being removed. For example, "Section Four is Here" becomes "section_fourishere". Other non-alphanumeric characters, such as ampersands (&), are removed. Section names can be found by using the getSectionNames() method. |
| display     | Boolean | Flag that indicates whether to show the section. Valid values: true: Show the section. false: Hide the section.                                                                                                                                                                                                                               |

| Type    | Description                   |
| ------- | ----------------------------- |
| Boolean | Returns true when successful. |

## GlideForm - setValue(String fieldName, String value, String displayValue)

Sets the value of a specified form field to the specified value or the value of a specified display value in a reference record.

To improve performance by preventing a round trip when setting the value for a reference field, use this method, not setValue(fieldName, value). When setting multiple reference values for a list collector field, pass arrays in the **value** and **displayValue** parameters.

This method also supports setting values in a multi-row variable set (MRVS). You must first use `JSON.parse(getValue('<mrvs_field_name>'))` to obtain the MRVS array and then use indexing to update the fields within the row objects. Once all values are updated in the MRVS, use the setValue() method to save the updated MRVS array. For more details, see the code example below.

**Note:** This method can't be used to update fields set to strict read only. If this method is called on strict read only fields, the field isn't updated and a warning is logged in the browser console. For more information, see Configuring read-only security options.

**Note:** The method setValue() can cause a stack overflow when used in an `onchange` client script. This is because every time the value is set, it will register as a change, which may re-trigger the OnChange client script. To prevent this, perform a check that will validate that the new value will be different from the old value. For example, before performing `setValue(shortDesc, newValue.toUpperCase());`, validate that the short description is not already uppercase. This will prevent the client script from applying the toUpperCase() more than once.

| Name         | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fieldName    | String          | Name of the form field to update.                                                                                                                                                                                                                                                                                                                                                                                                 |
| value        | String or Array | Sys_id of the reference record to use to update the field. If the specified field is a GlideList, this parameter can contain an array of sys_ids. In this case, the method performs a lookup of all records specified in the array and those values are used to update the contents of the specified field (related list). **Note:** When defining a value in a choice list, be sure to use a number value rather than the label. |
| displayValue | String or Array | Optional. Field within the specified reference record to use to update the specified field. For example, in the User [sys_user] table it might be userName. If the specified field is a GlideList, this parameter can contain an array of display value names. For additional information on display values, see Display value.                                                                                                   |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example shows how to set the short description in the current form.

```
g_form.setValue('short_description', 'replace this with appropriate text');
```

The following example shows how to set values in an MRVS. In this example, salaries are being managed through the Service Catalog. The client script searches all rows within the MRVS for the value entered in the **Job title** and then updates the matching entries within the MRVS with what is entered in the **Salary** field. The MRVS is named "variable_set_1" and contains the following fields within each row object: Employee name [employee_name], Job title [employee_job_title], and Salary [employee_salary]. In addition, the Catalog Item contains: Job title [job_title] and Salary [salary].

```
function onChange(control, oldValue, newValue, isLoading) {
if (isLoading || newValue == '') {
return;
}

// Get the MRVS
var multiRowVariableSet = JSON.parse(g_form.getValue('variable_set_1'));

for (var i = 0; i < multiRowVariableSet.length; i++) {
// Check if the entered job title matches the title in the current MRVS row
  if (multiRowVariableSet[i].employee_job_title == g_form.getValue("job_title")){
    // Update the value of a matching field with the new salary
    multiRowVariableSet[i].employee_salary = newValue;
  }
}

// Update the MRVS
g_form.setValue('variable_set_1', JSON.stringify(multiRowVariableSet));
}
```

This example shows passing the sys_id of the reference record that contains the userName field to use to update the **assigned_to** form field.

```
g_form.setValue('assigned_to', userSysID, userName);
```

This example shows passing an array of reference record sys_ids and an array of corresponding display value names to use to update the form fields in the GlideList **glide-list_field_name**.

```
g_form.setValue('glide-list_field_name', sysIDArray, displayNameArray);
```

## GlideForm - setVariablesReadOnly(Boolean isReadOnly)

Makes a Service Catalog variable editor read only.

**Note:** This method is only applicable to Service Catalog variable editors in the core UI. This method is not supported in the Service Catalog form.

The method must be placed in the client script of the table in which the variable editor is added, such as Requested Item [sc_req_item], Incident [incident], and so on. To set variables to read only in other tables, use the [setReadOnly()](glide-form-client.md) method.

See also: Service Catalog variable editors

| Name       | Type    | Description                                                                                                                                                                           |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| isReadOnly | Boolean | Flag that determines whether the variable editor is read only. Valid values: true: Sets the variable editor as read-only. false: Sets the variable editor as editable. Default: false |

| Type | Description |
| ---- | ----------- |
| void |             |

Adding the following line to a client script sets the variable editor to read only.

```
g_form.setVariablesReadOnly(true);
```

## GlideForm - setVisible(String fieldName, Boolean display)

Displays or hides the specified field.

On desktop UI, the space is left blank when hidden. On Mobile or Service Portal UI, the space is filled in my other fields when hidden. This method can't hide mandatory fields with no value.

Use UI Policy rather than this method whenever possible.

| Name      | Type    | Description                                                                                                               |
| --------- | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| fieldName | String  | Name of the field to display or hide.                                                                                     |
| display   | Boolean | Flag that indicates whether to display the specified field. Valid values: true: Display the field. false: Hide the field. |

| Type | Description |
| ---- | ----------- |
| void |             |

```
function onChange(control, oldValue, newValue, isLoading, isTemplate) {
   //If the page isn't loading
   if (!isLoading) {
      //If the new value isn't blank
      if(newValue != '') {
         g_form.setVisible('priority', false);
      }
      else
         g_form.setVisible('priority', true);
      }
   }
```

## GlideForm - showAnnotation(String name)

Shows an annotation with a given name on the form UI.

Annotations are visual separators between form elements, or blocks of colored text used to highlight form elements. See also:

- [GlideForm - hideAnnotation(String name)](glide-form-client.md) to hide a specific annotation on the form.
- [GlideForm - toggleAnnotations()](glide-form-client.md) to toggle annotations on and off with greater flexibility.

| Name | Type   | Description                                                                                              |
| ---- | ------ | -------------------------------------------------------------------------------------------------------- |
| name | String | Name of the annotation to show in the form. Table: Form Annotations [sys_ui_annotation], Field: **Name** |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example demonstrates how to programmatically show the annotation named test-annotation-msg on the form field using the showAnnotation() method.

```
g_form.showAnnotation('test-annotation-msg');
```

## GlideForm - showErrorBox(String name, String message, Boolean scrollForm)

Displays an error message under the specified form field (either a control object or the name of the field). If the control or field is currently off the screen and the **scrollForm** parameter is true, the form scrolls to the control or field.

A global property (glide.ui.scroll_to_message_field) is available that controls automatic message scrolling when the form field is off screen (scrolls the form to the control or field). The showFieldMsg() method is a similar method that requires a type parameter.

| Name       | Type    | Description                                                                                                                                                                                                   |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name       | String  | Name of the field or control under which to display the error message.                                                                                                                                        |
| message    | String  | Error message to display.                                                                                                                                                                                     |
| scrollForm | Boolean | Flag that indicates whether to automatically scroll the form to the error message field. Valid values: true: Scroll to the error message field. false: Don't scroll to the error message field. Default: true |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - showErrorBox(String name, String message)

Displays an error message under the specified form field (either a control object or the name of the field). If the control or field is currently off the screen, the form automatically scrolls to the control or field.

A global property (glide.ui.scroll_to_message_field) is available that controls automatic message scrolling when the form field is off screen (scrolls the form to the control or field). The showFieldMsg() method is a similar method that requires a type parameter.

| Name    | Type   | Description                                                            |
| ------- | ------ | ---------------------------------------------------------------------- |
| name    | String | Name of the field or control under which to display the error message. |
| message | String | Error message to display.                                              |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - showFieldMsg(String field, String message, String type)

Displays a message under the specified form field (either a control object or the name of the field). If the control or field is off the screen, the method automatically scrolls the form to that field.

A global property (glide.ui.scroll_to_message_field) is available that controls automatic message scrolling when the form field is off screen (scrolls the form to the control or field).

The showErrorBox() method is a shorthand method that does not require the type parameter.

**Note:** This method does not work with the **journal_field** type field in Core UI.

| Name    | Type   | Description                                                      |
| ------- | ------ | ---------------------------------------------------------------- |
| field   | String | Name of the field or control under which to display the message. |
| message | String | Message to display.                                              |
| type    | String | Type of message. Valid values: error, info, warning.             |

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.showFieldMsg('impact','Low impact response time can be one week','info');
```

## GlideForm - showFieldMsg(String field, String message, String type, Boolean scrollForm)

Displays a message under the specified form field (either a control object or the name of the field). If the control or field is currently off the screen and **scrollForm** is `true`, the method scrolls the form to that field.

A global property (glide.ui.scroll_to_message_field) is available that controls automatic message scrolling when the form field is off screen (scrolls the form to the control or field).

The showErrorBox() method is a shorthand method that does not require the type parameter.

**Note:** This method does not work with the **journal_field** type field in Core UI.

| Name       | Type    | Description                                                                                                                                                                                 |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| field      | String  | Name of the field or control under which to display the message.                                                                                                                            |
| message    | String  | Message to display.                                                                                                                                                                         |
| type       | String  | Type of message. Valid values: error, info, warning.                                                                                                                                        |
| scrollForm | Boolean | Flag that indicates whether to automatically scroll the form to the message field. Valid values: true: Scroll to the message field. false: Don't scroll to the message field. Default: true |

| Type | Description |
| ---- | ----------- |
| void |             |

```
g_form.showFieldMsg('impact','Low impact not allowed with High priority','error',false);
```

## GlideForm - showRelatedLinks()

Displays the Related Links section of a form.

See also:

- [GlideForm - hideRelatedLinks()](glide-form-client.md)
- [GlideForm - setRelatedLinksDisplay(Boolean display)](glide-form-client.md)

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example displays related links in the form UI.

```
// Show related links
g_form.showRelatedLinks()
```

## GlideForm - showRelatedList(String listTableName)

Displays the specified related list on the form.

This method isn't available on the mobile platform. If this method is run on a mobile platform, no action occurs.

| Name          | Type   | Description                          |
| ------------- | ------ | ------------------------------------ |
| listTableName | String | Name of the related list to display. |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - showRelatedLists()

Displays all the form's related lists.

This method isn't available on the mobile platform. If this method is run on a mobile platform, no action occurs.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - showTemplateBar()

If hidden, shows the template bar at the bottom of the form.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example script displays the Template Bar at the bottom of the current form.

```
g_form.showTemplateBar()
```

## GlideForm - submit()

Saves the record.

The user is taken away from the form, returning them to where they were.

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - submit(String verb)

Performs the specified UI action.

| Name | Type   | Description                                                                                    |
| ---- | ------ | ---------------------------------------------------------------------------------------------- |
| verb | String | An action_name from a sys_ui_action record. The action name must be for a visible form button. |

| Type | Description |
| ---- | ----------- |
| void |             |

## GlideForm - toggleAnnotations()

Hides or shows all annotations on the form.

Annotations are visual separators between form elements, or blocks of colored text used to highlight form elements. If annotations are visible on the form, calling toggleAnnotations() hides them. Similarly if annotations are hidden on the form, calling this method displays them.

See also:

- [GlideForm - hideAnnotation(String name)](glide-form-client.md)
- [GlideForm - showAnnotation(String name)](glide-form-client.md)

| Name | Type | Description |
| ---- | ---- | ----------- |
| None |      |             |

| Type | Description |
| ---- | ----------- |
| None |             |

The following example shows how to call toggleAnnotations() to show or hide form annotations. As a result, annotations are hidden or shown depending on their previous state.

```
g_form.toggleAnnotations();
```
