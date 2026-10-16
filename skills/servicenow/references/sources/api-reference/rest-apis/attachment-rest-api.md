# Attachment API

The Attachment API provides endpoints that allow you to upload and query file attachments.

You can upload or retrieve a single file with each request.

The Attachment API respects any system limitations on uploaded files, such as maximum file size and allowed attachment types. You can control these settings using the properties **com.glide.attachment.max_size**, 1024MB by default, and **glide.attachment.extensions**.

**Note:** The Attachment API accepts all Content-Type values (`*/*`). Specify the file content type when uploading an attachment. The content type is stored with file metadata allowing other tools to correctly identify and parse the file.

## Attachment API role requirements

To create attachments, the user record used to authenticate the HTTP request with ServiceNow must have any roles required to create Attachment [sys_attachment] records. It must also have any roles required to read and write records on the target table, such as the itil role to add attachments to incident records.

By default there is no single role allowing a user to add attachments. You can create a role to explicitly allow adding attachments, then assign this role to the user account being used to make the request.

## Attachment - DELETE /now/attachment/{sys_id}

Deletes a specified attachment.

### URL format

Versioned URL: `/api/now/v1/attachment/{sys_id}`

Default URL: `/api/now/attachment/{sys_id}`

**Note:** Available versions are specified in the REST API Explorer. For scripted REST APIs there is additional version information on the Scripted REST Service form.

### Supported request parameters

**Path parameters**

| Name   | Description                                                                    |
| ------ | ------------------------------------------------------------------------------ |
| sys_id | Sys_id of the attachment. Data type: String Table: Attachment [sys_attachment] |

| Name | Description |
| ---- | ----------- |
| None |             |

| Name | Description |
| ---- | ----------- |
| None |             |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

| Header | Description |
| ------ | ----------- |
| None   |             |

| Header | Description |
| ------ | ----------- |
| None   |             |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 204         | Indicates the request ran successfully.                                                                                                         |
| 401         | Unauthorized. The user credentials are incorrect or have not been passed.                                                                       |
| 404         | Not found. The requested item wasn't found.                                                                                                     |
| 500         | Internal server error. An unexpected error occurred while processing the request. The response contains additional information about the error. |

### Response body parameters (JSON or XML)

| Name | Description |
| ---- | ----------- |
| None |             |

### cURL request

```
curl "https://instance.servicenow.com/api/now/attachment/615ea769c0a80166001cf5f2367302f5" \
--request DELETE \
--user 'username':'password'

```

```
""
```

## Attachment - DELETE /now/attachment/{sys_id}/attributes

Deletes all attributes for an attachment.

Attributes are deleted from the Attachment Attributes [sys_attachment_attribute] table.

### URL format

Versioned URL: `/api/now/{api_version}/attachment/{sys_id}/attributes`

Default URL: `/api/now/attachment/{sys_id}/attributes`

### Supported request parameters

**Path parameters**

| Name        | Description                                                                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | Optional. Version of the endpoint to access. For example, `v1` or `v2`. Only specify this value to use an endpoint version other than the latest. Data type: String |
| sys_id      | Sys_id of the attachment. Data type: String Table: Attachment [sys_attachment]                                                                                      |

| Name | Description |
| ---- | ----------- |
| None |             |

| Name | Description |
| ---- | ----------- |
| None |             |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

| Header | Description |
| ------ | ----------- |
| None   |             |

| Header | Description |
| ------ | ----------- |
| None   |             |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------ |
| 204         | No Content. The attributes were successfully deleted and no content was returned in the response body. |
| 400         | Bad Request. A bad request type or malformed request was detected.                                     |
| 404         | Not found. The requested item wasn't found.                                                            |

### Response body parameters (JSON or XML)

| Name | Description |
| ---- | ----------- |
| None |             |

### cURL request

This example deletes all attributes from an attachment.

```
curl "https://instance.service-now.com/api/now/attachment/a3af695b0a0006871b657c200acf62e0/attributes" \
--request DELETE \
--user 'username':'password'
```

Response body.

```
""
```

## Attachment - DELETE /now/attachment/{sys_id}/attributes/{attribute_key}

Deletes a specified attribute from an attachment.

Attributes are deleted from the Attachment Attributes [sys_attachment_attribute] table.

### URL format

Versioned URL: `/api/now/{api_version}/attachment/{sys_id}/attributes/{attribute_key}`

Default URL: `/api/now/attachment/{sys_id}/attributes/{attribute_key}`

### Supported request parameters

**Path parameters**

| Name          | Description                                                                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version   | Optional. Version of the endpoint to access. For example, `v1` or `v2`. Only specify this value to use an endpoint version other than the latest. Data type: String |
| sys_id        | Sys_id of the attachment. Data type: String Table: Attachment [sys_attachment]                                                                                      |
| attribute_key | Attribute key. Data type: String Table: Attachment Attributes [sys_attachment_attribute] Column: Key                                                                |

| Name | Description |
| ---- | ----------- |
| None |             |

| Name | Description |
| ---- | ----------- |
| None |             |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

| Header | Description |
| ------ | ----------- |
| None   |             |

| Header | Description |
| ------ | ----------- |
| None   |             |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                                                          |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| 204         | No Content. The attribute was successfully deleted and no content was returned in the response body. |
| 400         | Bad Request. A bad request type or malformed request was detected.                                   |
| 404         | Not found. The requested item wasn't found.                                                          |

### Response body parameters (JSON or XML)

| Name | Description |
| ---- | ----------- |
| None |             |

### cURL request

This example deletes a specified attribute from an attachment.

```
curl "https://instance.service-now.com/api/now/attachment/a3af695b0a0006871b657c200acf62e0/attributes/example_key" \
--request DELETE \
--user 'username':'password'
```

Response body.

```
""
```

## Attachment - GET /now/attachment

Returns the metadata for multiple attachments.

### URL format

Versioned URL: `api/now/v1/attachment`

Default URL: `api/now/attachment`

**Note:** Available versions are specified in the REST API Explorer. For scripted REST APIs there is additional version information on the Scripted REST Service form.

### Supported request parameters

| Name | Description |
| ---- | ----------- |
| None |             |

**Query parameters**

| Name           | Description                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| sysparm_limit  | Limit to be applied on pagination. **Note:** Unusually large `sysparm_limit` values can impact system performance. Data type: String Default: 1000                                                                                                                                                                                                                 |
| sysparm_offset | Number of records to exclude from the query. Use this parameter to get more records than specified in **sysparm_limit** parameter. For example, if **sysparm_limit** is set to 500, but there are additional records you want to query, you can specify a **sysparm_offset** parameter value of 500 to get the second set of records. Data type: String Default: 0 |
| sysparm_query  | Encoded query. Queries for the Attachment API are relative to the Attachments [sys_attachment] table. For example: **(sysparm_query=file_name=attachment.doc)**                                                                                                                                                                                                    |

**sysparm_query:**

The encoded query provides support for order by. To sort responses based on certain fields, use the ORDERBY and ORDERBYDESC clauses in sysparm_query. For example, `sysparm_query=ORDERBYfile_name^ORDERBYDESCtable_Name` orders the results in ascending order by name first, then in descending order by table name.

Data type: String

| Name | Description |
| ---- | ----------- |
| None |             |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

**Request headers**

| Header | Description                                                                                                                   |
| ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Accept | Data format of the response body. Supported types: **application/json** or **application/xml**. Default: **application/json** |

| Header       | Description                                                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Content-Type | Content type of the response. For metadata requests, this is the content type of the metadata, not the content type of the attachment files. |
| Link         | Links to download the attachments.                                                                                                           |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | Successful. The request was successfully processed.                                                                                             |
| 401         | Unauthorized. The user credentials are incorrect or have not been passed.                                                                       |
| 500         | Internal server error. An unexpected error occurred while processing the request. The response contains additional information about the error. |

### Response body parameters (JSON or XML)

| Name                                                      | Description |
| --------------------------------------------------------- | ----------- |
| Returned information depends on the selected attachments. |             |

### cURL request

```
curl "https://instance.servicenow.com/api/now/attachment?sysparm_limit=1" \
--request GET \
--header "Accept:application/json" \
--user "username":"password"

```

```
{
  "result": [
    {
      "table_sys_id": "5054b6f8c0a800060056addcf551ecf8",
      "size_bytes": "462",
      "download_link": "https://instance.service-now.com/api/now/attachment/615ea769c0a80166001cf5f2367302f5/file",
      "sys_updated_on": "2009-05-21 04:12:21",
      "sys_id": "615ea769c0a80166001cf5f2367302f5",
      "image_height": "",
      "sys_created_on": "2009-05-21 04:12:21",
      "file_name": "blocks.swf",
      "sys_created_by": "glide.maint",
      "compressed": "true",
      "average_image_color": "",
      "sys_updated_by": "glide.maint",
      "sys_tags": "",
      "table_name": "content_block_programmatic",
      "image_width": "",
      "sys_mod_count": "0",
      "content_type": "application/x-shockwave-flash",
      "size_compressed": "485"
    }
  ]
}
```

## Attachment - GET /now/attachment/{sys_id}

Returns the metadata for the attachment file with a specific sys_id value.

### URL format

Versioned URL: `/api/now/v1/attachment/{sys_id}`

Default URL: `/api/now/attachment/{sys_id}`

**Note:** Available versions are specified in the REST API Explorer. For scripted REST APIs there is additional version information on the Scripted REST Service form.

### Supported request parameters

| Name   | Description                                                         |
| ------ | ------------------------------------------------------------------- |
| sys_id | Sys_id of the attachment record for which to retrieve the metadata. |

| Name | Description |
| ---- | ----------- |
| None |             |

| Name | Description |
| ---- | ----------- |
| None |             |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

**Request headers**

| Header | Description                                                                                                                   |
| ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Accept | Data format of the response body. Supported types: **application/json** or **application/xml**. Default: **application/json** |

| Header       | Description                                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Content-Type | The content type of the response. For metadata requests, this is the content type of the metadata, not the content type of the attachment files. |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | Successful. The request was successfully processed.                                                                                             |
| 401         | Unauthorized. The user credentials are incorrect or have not been passed.                                                                       |
| 404         | Indicates the specified attachment does not exist, or the current user cannot access it.                                                        |
| 500         | Internal server error. An unexpected error occurred while processing the request. The response contains additional information about the error. |

### Response body parameters (JSON or XML)

| Name                                           | Description |
| ---------------------------------------------- | ----------- |
| Metadata specific to the specified attachment. |             |

### cURL request

```
curl "https://instance.servicenow.com/api/now/attachment/615ea769c0a80166001cf5f2367302f5" \
--request GET \
--header "Accept:application/json" \
--user "username":"password"
```

```
{
  "result": {
    "table_sys_id": "5054b6f8c0a800060056addcf551ecf8",
    "size_bytes": "462",
    "download_link": "https://instance.service-now.com/api/now/attachment/615ea769c0a80166001cf5f2367302f5/file",
    "sys_updated_on": "2009-05-21 04:12:21",
    "sys_id": "615ea769c0a80166001cf5f2367302f5",
    "image_height": "",
    "sys_created_on": "2009-05-21 04:12:21",
    "file_name": "blocks.swf",
    "sys_created_by": "glide.maint",
    "compressed": "true",
    "average_image_color": "",
    "sys_updated_by": "glide.maint",
    "sys_tags": "",
    "table_name": "content_block_programmatic",
    "image_width": "",
    "sys_mod_count": "0",
    "content_type": "application/x-shockwave-flash",
    "size_compressed": "485"
  }
}
```

## Attachment - GET /now/attachment/{sys_id}/attributes

Retrieves all attributes for an attachment.

Attributes are retrieved from the Attachment Attributes [sys_attachment_attribute] table.

### URL format

Versioned URL: `/api/now/{api_version}/attachment/{sys_id}/attributes`

Default URL: `/api/now/attachment/{sys_id}/attributes`

### Supported request parameters

**Path parameters**

| Name        | Description                                                                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | Optional. Version of the endpoint to access. For example, `v1` or `v2`. Only specify this value to use an endpoint version other than the latest. Data type: String |
| sys_id      | Sys_id of the attachment. Data type: String Table: Attachment [sys_attachment]                                                                                      |

| Name | Description |
| ---- | ----------- |
| None |             |

| Name | Description |
| ---- | ----------- |
| None |             |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

**Request headers**

| Header | Description                                                                                                                   |
| ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Accept | Data format of the response body. Supported types: **application/json** or **application/xml**. Default: **application/json** |

| Header | Description |
| ------ | ----------- |
| None   |             |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                        |
| ----------- | ------------------------------------------------------------------ |
| 200         | Successful. The request was successfully processed.                |
| 400         | Bad Request. A bad request type or malformed request was detected. |
| 404         | Not found. The requested item wasn't found.                        |

### Response body parameters (JSON or XML)

| Name         | Description                                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| result       | Array of objects containing a key-value pair for each attribute. Data type: Array. See the result example below. |
| result.key   | Attribute key. Data type: String Table: Attachment Attributes [sys_attachment_attribute] Column: Key             |
| result.value | Attribute value. Data type: String Table: Attachment Attributes [sys_attachment_attribute] Column: Value         |

**result example**

```
"result": [
  {
    "key": "example_key",
    "value": "example_value"
  }
]
```

### cURL request

This example retrieves all attributes for the specified attachment.

```
curl "https://instance.service-now.com/api/now/attachment/a3af695b0a0006871b657c200acf62e0/attributes" \
--request GET \
--header "Accept:application/json" \
--user 'username':'password'
```

Response body.

```
{
  "result": [
    {
      "key": "example_key",
      "value": "example_value"
    },
    {
      "key": "another_key",
      "value": "another_value"
    }
  ]
}
```

## Attachment - GET /now/attachment/{sys_id}/attributes/{attribute_key}

Retrieves a specified attribute from an attachment.

Attributes are retrieved from the Attachment Attributes [sys_attachment_attribute] table.

### URL format

Versioned URL: `/api/now/{api_version}/attachment/{sys_id}/attributes/{attribute_key}`

Default URL: `/api/now/attachment/{sys_id}/attributes/{attribute_key}`

### Supported request parameters

**Path parameters**

| Name          | Description                                                                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version   | Optional. Version of the endpoint to access. For example, `v1` or `v2`. Only specify this value to use an endpoint version other than the latest. Data type: String |
| sys_id        | Sys_id of the attachment. Data type: String Table: Attachment [sys_attachment]                                                                                      |
| attribute_key | Attribute key. Data type: String Table: Attachment Attributes [sys_attachment_attribute] Column: Key                                                                |

| Name | Description |
| ---- | ----------- |
| None |             |

| Name | Description |
| ---- | ----------- |
| None |             |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

**Request headers**

| Header | Description                                                                                                                   |
| ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Accept | Data format of the response body. Supported types: **application/json** or **application/xml**. Default: **application/json** |

| Header | Description |
| ------ | ----------- |
| None   |             |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                        |
| ----------- | ------------------------------------------------------------------ |
| 200         | Successful. The request was successfully processed.                |
| 400         | Bad Request. A bad request type or malformed request was detected. |
| 404         | Not found. The requested item wasn't found.                        |

### Response body parameters (JSON or XML)

| Name         | Description                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------- |
| result       | Object containing the key-value pair for the attribute. Data type: Object. See the result example below. |
| result.key   | Attribute key. Data type: String Table: Attachment Attributes [sys_attachment_attribute] Column: Key     |
| result.value | Attribute value. Data type: String Table: Attachment Attributes [sys_attachment_attribute] Column: Value |

**result example**

```
"result": {
   "key": "String",
   "value": "String"
}
```

### cURL request

This example retrieves a specified attribute from an attachment.

```
curl "https://instance.service-now.com/api/now/attachment/a3af695b0a0006871b657c200acf62e0/attributes/example_key" \
--request GET \
--header "Accept:application/json" \
--user 'username':'password'
```

Response body.

```
{
  "result": {
    "key": "example_key",
    "value": "example_value"
  }
}
```

## Attachment - GET /now/attachment/{sys_id}/file

Returns the binary file attachment with a specific sys_id value.

### URL format

Versioned URL: `/api/now/v1/attachment/{sys_id}/file`

Default URL: `/api/now/attachment/{sys_id}/file`

**Note:** Available versions are specified in the REST API Explorer. For scripted REST APIs there is additional version information on the Scripted REST Service form.

### Supported request parameters

| Name   | Description                                                       |
| ------ | ----------------------------------------------------------------- |
| sys_id | Sys_id of the attachment record from which to return binary data. |

| Name | Description |
| ---- | ----------- |
| None |             |

| Name | Description |
| ---- | ----------- |
| None |             |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

**Request headers**

| Header | Description                                                                                                                                                                                                                     |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accept | Data format of the response body. For example, use `image/jpeg` or `image/png` to accept JPEG or PNG image files exclusively. To allow all image types, specify `image/*`; to allow any file type, specify `*/*`.Default: `*/*` |

| Header                | Description                                                          |
| --------------------- | -------------------------------------------------------------------- |
| X-Attachment-Metadata | Metadata about the returned file, such as size, name, and file type. |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | Successful. The request was successfully processed.                                                                                             |
| 400         | Bad Request. A bad request type or malformed request was detected.                                                                              |
| 401         | Unauthorized. The user credentials are incorrect or have not been passed.                                                                       |
| 500         | Internal server error. An unexpected error occurred while processing the request. The response contains additional information about the error. |

### Response body parameters (JSON or XML)

| Name                   | Description |
| ---------------------- | ----------- |
| Binary file attachment |             |

### cURL request

```
curl "https://instance.servicenow.com/api/now/attachment/615ea769c0a80166001cf5f2367302f5/file" \
--request GET \
--header "Accept:*/*" \
--user "username":"password"
```

```
Binary response not shown.
```

## Attachment - PATCH /now/attachment/{sys_id}

Renames an attachment.

### URL format

Versioned URL: `/api/now/{api_version}/attachment/{sys_id}`

Default URL: `/api/now/attachment/{sys_id}`

### Supported request parameters

**Path parameters**

| Name        | Description                                                                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | Optional. Version of the endpoint to access. For example, `v1` or `v2`. Only specify this value to use an endpoint version other than the latest. Data type: String |
| sys_id      | Sys_id of the attachment. Table: Attachment [sys_attachment] Data type: String                                                                                      |

| Name | Description |
| ---- | ----------- |
| None |             |

**Request body**

| Name      | Description                                              |
| --------- | -------------------------------------------------------- |
| file_name | Required. New name for the attachment. Data type: String |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

**Request headers**

| Header       | Description                                                                                                                   |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Accept       | Data format of the response body. Supported types: **application/json** or **application/xml**. Default: **application/json** |
| Content-Type | Data format of the request body. Supported types: **application/json** or **application/xml**. Default: **application/json**  |

| Header | Description |
| ------ | ----------- |
| None   |             |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                                                           |
| ----------- | ----------------------------------------------------------------------------------------------------- |
| 204         | No Content. The attachment was successfully renamed and no content was returned in the response body. |
| 400         | Bad Request. A bad request type or malformed request was detected.                                    |
| 401         | Unauthorized. The user credentials are incorrect or have not been passed.                             |

### Response body parameters (JSON or XML)

| Name          | Description                                                                                                                                 |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| error         | Error information. This parameter is only returned if the request failed. Data type: Object. See the error example below.                   |
| error.detail  | Additional details about why the request failed. Data type: String                                                                          |
| error.message | Error message containing the reason the request failed. Data type: String                                                                   |
| status        | Status of the API request. This parameter is only returned if the request failed so the only possible value is `failure`. Data type: String |

**error example**

```
"error": {
   "detail": "String",
   "message": "String"
}
```

### cURL request

This example renames an attachment.

```
curl "https://instance.service-now.com/api/now/attachment/a3af695b0a0006871b657c200acf62e0" \
--request PATCH \
--header "Accept:application/json" \
--header "Content-Type:application/json" \
--data "{
  \"file_name\": \"new_attachment_name\"
}" \
--user 'username':'password'
```

Response body.

```
""
```

## Attachment - POST /now/attachment/{sys_id}/attributes

Adds an attribute to a specified attachment.

Attributes are added in the Attachment Attributes [sys_attachment_attribute] table.

This endpoint can be used to add alt text to an attachment.

### URL format

Versioned URL: `/api/now/{api_version}/attachment/{sys_id}/attributes`

Default URL: `/api/now/attachment/{sys_id}/attributes`

### Supported request parameters

**Path parameters**

| Name        | Description                                                                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version | Optional. Version of the endpoint to access. For example, `v1` or `v2`. Only specify this value to use an endpoint version other than the latest. Data type: String |
| sys_id      | Sys_id of the attachment. Data type: String Table: Attachment [sys_attachment]                                                                                      |

| Name | Description |
| ---- | ----------- |
| None |             |

**Request body**

| Name  | Description                                                 |
| ----- | ----------------------------------------------------------- |
| key   | Required. Key to use for the attribute. Data type: String   |
| value | Required. Value to use for the attribute. Data type: String |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

**Request headers**

| Header       | Description                                                                                                                   |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Accept       | Data format of the response body. Supported types: **application/json** or **application/xml**. Default: **application/json** |
| Content-Type | Data format of the request body. Supported types: **application/json** or **application/xml**. Default: **application/json**  |

| Header | Description |
| ------ | ----------- |
| None   |             |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                        |
| ----------- | ------------------------------------------------------------------ |
| 201         | Created. The attribute was successfully created.                   |
| 400         | Bad Request. A bad request type or malformed request was detected. |
| 404         | Not found. The requested item wasn't found.                        |

### Response body parameters (JSON or XML)

| Name         | Description                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------- |
| result       | Object containing the key-value pair for the attribute. Data type: Object. See the result example below. |
| result.key   | Attribute key. Data type: String Table: Attachment Attributes [sys_attachment_attribute] Column: Key     |
| result.value | Attribute value. Data type: String Table: Attachment Attributes [sys_attachment_attribute] Column: Value |

**result example**

```
"result": {
   "key": "String",
   "value": "String"
}
```

### cURL request

This example adds an attribute to an attachment.

```
curl "https://instance.service-now.com/api/now/attachment/a3af695b0a0006871b657c200acf62e0/attributes" \
--request POST \
--header "Accept:application/json" \
--header "Content-Type:application/json" \
--data "{
  \"key\": \"example_key\",
  \"value\": \"example_value\"
}" \
--user 'username':'password'
```

Response body.

```
{
  "result": {
    "key": "example_key",
    "value": "example_value"
  }
}
```

## Attachment - POST /now/attachment/file

Uploads a specified binary file as an attachment to a specified record.

**Note:** The file to attach must be specified after the last parameter in the passed-in request parameter list.

### URL format

Versioned URL: `/api/now/v1/attachment/file`

Default URL: `/api/now/attachment/file`

**Note:** Available versions are specified in the REST API Explorer. For scripted REST APIs there is additional version information on the Scripted REST Service form.

### Supported request parameters

| Name | Description |
| ---- | ----------- |
| None |             |

**Query parameters**

| Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| creation_time      | Creation date and time of the attachment. Use this parameter to capture attachment creation times when the Now Mobile app is offline and the attachment is uploaded to a record at a later time. Data type: String Default: The current date and time.                                                                                                                                                     |
| encryption_context | Sys_id of an encryption context record. Specify this parameter to allow only users with the specified encryption context to access the attachment. For additional information on encryption context records, see Field Encryption. Data type: String Default: File is encrypted using encryption context accessible to the user, otherwise the attached file is not encrypted with any encryption context. |
| file_name          | Required. Name to give the attachment. Data type: String                                                                                                                                                                                                                                                                                                                                                   |
| table_name         | Required. Name of the table to attach the file to. Data type: String                                                                                                                                                                                                                                                                                                                                       |
| table_sys_id       | Required. Sys_id of the record in the table specified in **table_name** that you want to attach the file to. Data type: String                                                                                                                                                                                                                                                                             |

| Name       | Description                                                |
| ---------- | ---------------------------------------------------------- |
| `<String>` | Path to the binary file to attach to the specified record. |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

**Request headers**

| Header       | Description                                                                                                                   |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Accept       | Data format of the response body. Supported types: **application/json** or **application/xml**. Default: **application/json** |
| Content-Type | Content type of the file to attach, such as `image/jpeg` or `*/*`. This header is mandatory to post file attachments.         |

| Header   | Description                |
| -------- | -------------------------- |
| Location | URL of the new attachment. |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 201         | Indicates the query ran successfully.                                                                                                           |
| 400         | Indicates that one or more mandatory parameters were missing from the request.                                                                  |
| 404         | Indicates the record specified by the **table_name** and **table_sys_id** parameters does not exist or is not accessible to the current user.   |
| 500         | Internal server error. An unexpected error occurred while processing the request. The response contains additional information about the error. |

### Response body parameters (JSON or XML)

| Element                    | Description                                                                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| result                     | Metadata of the requested attachment. Data type: Object. See the result example below.                                                                                       |
| result.average_image_color | If the attachment is an image, the sum of all colors. Data type: String Unit: RGB or number of pixels.                                                                       |
| result.compressed          | Flag that indicates whether the attachment file has been compressed. Possible values: true: File has been compressed. false: File has not been compressed. Data type: String |
| result.content_type        | Content-type of the associated attachment file, such as image or jpeg or application/x-shockwave-flash. Data type: String                                                    |
| result.created_by_name     | Full name of entity that originally created the attachment file. Data type: String                                                                                           |
| result.download_link       | Download URL of the attachment on the ServiceNow instance. Data type: String                                                                                                 |
| result.file_name           | File name of the attachment. Data type: String                                                                                                                               |
| result.image_height        | If an image file, the height of the image. Data type: String Unit: Pixels                                                                                                    |
| result.image_width         | If an image file, the width of the image. Data type: String Unit: Pixels                                                                                                     |
| result.size_bytes          | Size of the attachment. Data type: String Unit: Bytes                                                                                                                        |
| result.size_compressed     | Size of the compressed attachment file. If the file is not compressed, empty. Data type: String Unit: Bytes                                                                  |
| result.sys_created_by      | Entity that originally created the attachment file. Data type: String                                                                                                        |
| result.sys_created_on      | Date and time that the attachment file was initially saved to the instance. Data type: String                                                                                |
| result.sys_id              | Sys_id of the attachment file. Data type: String                                                                                                                             |
| result.sys_mod_count       | Number of times the attachment file has been modified (uploaded to the instance). Data type: String                                                                          |
| result.sys_tags            | Any system tags associated with the attachment file. Data type: String                                                                                                       |
| result.sys_updated_by      | Entity that last updated the attachment file. Data type: String                                                                                                              |
| result.sys_updated_on      | Date and time that the attachment file was last updated. Data type: String                                                                                                   |
| result.table_name          | Name of the table to which the attachment is associated. Data type: String                                                                                                   |
| result.table_sys_id        | Sys_id of the table associated with the attachment. Data type: String                                                                                                        |
| result.updated_by_name     | Full name of entity that last updated the attachment file. Data type: String                                                                                                 |

**result example**

```
"result": {
  "average_image_color": "String",
  "compressed": "String",
  "content_type": "String",
  "created_by_name": "String",
  "download_link": "String",
  "file_name": "String",
  "image_height": "String",
  "image_width": "String",
  "size_bytes": "String",
  "size_compressed": "String",
  "sys_created_by": "String",
  "sys_created_on": "String",
  "sys_id": "String",
  "sys_mod_count": "String",
  "sys_tags": "String",
  "sys_updated_by": "String",
  "sys_updated_on": "String",
  "table_name": "String",
  "table_sys_id": "String",
  "updated_by_name": "String"
}
```

### cURL request

```
curl "https://instance.servicenow.com/api/now/attachment/file?table_name=incident&table_sys_id=d71f7935c0a8016700802b64c67c11c6&file_name=Issue_screenshot" \
--request POST \
--header "Accept:application/json" \
--header "Content-Type: image/jpeg" \
--user "username":"password" \
--data-binary "@ location of the file on file system"
```

```
{
  "result": {
    "table_sys_id": "d71f7935c0a8016700802b64c67c11c6",
    "size_bytes": "36597",
    "download_link": "https://instance.servicenow.com/api/now/attachment/6ea10fe64f411200adf9f8e18110c739/file",
    "sys_updated_on": "2016-01-22 15:14:07",
    "sys_id": "6ea10fe64f411200adf9f8e18110c739",
    "image_height": "",
    "sys_created_on": "2016-01-22 15:14:07",
    "file_name": "Issue_screenshot",
    "sys_created_by": "admin",
    "compressed": "true",
    "average_image_color": "",
    "sys_updated_by": "admin",
    "sys_tags": "",
    "table_name": "incident",
    "image_width": "",
    "sys_mod_count": "0",
    "content_type": "image/jpeg",
    "size_compressed": "25130"
  }
}
```

## Attachment - POST /now/attachment/upload

Uploads a multipart file attachment.

The multipart POST method does not accept any parameters. You must specify the table name and record sys_id values within the form body. See the cURL example for a sample of a multipart/form-data request.

**Important:** When using multipart POST, ensure that the file content is contained in the final part of the message only. Earlier parts should contain only metadata such as table name and record sys_id.

### URL format

Versioned URL: `/api/now/v1/attachment/upload`

Default URL: `/api/now/attachment/upload`

**Note:** Available versions are specified in the REST API Explorer. For scripted REST APIs there is additional version information on the Scripted REST Service form.

### Supported request parameters

| Name | Description |
| ---- | ----------- |
| None |             |

| Name | Description |
| ---- | ----------- |
| None |             |

| Name | Description |
| ---- | ----------- |
| None |             |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

**Request headers**

| Header       | Description                                                                                                                   |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Accept       | Data format of the response body. Supported types: **application/json** or **application/xml**. Default: **application/json** |
| Content-Type | Content type of the request. Set this value to multipart/form-data when using the multipart POST method.                      |

| Header   | Description                |
| -------- | -------------------------- |
| Location | URL of the new attachment. |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 201         | Indicates the query ran successfully.                                                                                                           |
| 400         | Bad Request. A bad request type or malformed request was detected.                                                                              |
| 401         | Unauthorized. The user credentials are incorrect or have not been passed.                                                                       |
| 404         | Not found. The requested item wasn't found.                                                                                                     |
| 500         | Internal server error. An unexpected error occurred while processing the request. The response contains additional information about the error. |

### Response body parameters (JSON or XML)

| Element                    | Description                                                                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| result                     | Metadata of the requested attachment. Data type: Object. See the result example below.                                                                                       |
| result.average_image_color | If the attachment is an image, the sum of all colors. Data type: String Unit: RGB or number of pixels.                                                                       |
| result.compressed          | Flag that indicates whether the attachment file has been compressed. Possible values: true: File has been compressed. false: File has not been compressed. Data type: String |
| result.content_type        | Content-type of the associated attachment file, such as image or jpeg or application/x-shockwave-flash. Data type: String                                                    |
| result.created_by_name     | Full name of entity that originally created the attachment file. Data type: String                                                                                           |
| result.download_link       | Download URL of the attachment on the ServiceNow instance. Data type: String                                                                                                 |
| result.file_name           | File name of the attachment. Data type: String                                                                                                                               |
| result.image_height        | If an image file, the height of the image. Data type: String Unit: Pixels                                                                                                    |
| result.image_width         | If an image file, the width of the image. Data type: String Unit: Pixels                                                                                                     |
| result.size_bytes          | Size of the attachment. Data type: String Unit: Bytes                                                                                                                        |
| result.size_compressed     | Size of the compressed attachment file. If the file is not compressed, empty. Data type: String Unit: Bytes                                                                  |
| result.sys_created_by      | Entity that originally created the attachment file. Data type: String                                                                                                        |
| result.sys_created_on      | Date and time that the attachment file was initially saved to the instance. Data type: String                                                                                |
| result.sys_id              | Sys_id of the attachment file. Data type: String                                                                                                                             |
| result.sys_mod_count       | Number of times the attachment file has been modified (uploaded to the instance). Data type: String                                                                          |
| result.sys_tags            | Any system tags associated with the attachment file. Data type: String                                                                                                       |
| result.sys_updated_by      | Entity that last updated the attachment file. Data type: String                                                                                                              |
| result.sys_updated_on      | Date and time that the attachment file was last updated. Data type: String                                                                                                   |
| result.table_name          | Name of the table to which the attachment is associated. Data type: String                                                                                                   |
| result.table_sys_id        | Sys_id of the table associated with the attachment. Data type: String                                                                                                        |
| result.updated_by_name     | Full name of entity that last updated the attachment file. Data type: String                                                                                                 |

**result example**

```
"result": {
  "average_image_color": "String",
  "compressed": "String",
  "content_type": "String",
  "created_by_name": "String",
  "download_link": "String",
  "file_name": "String",
  "image_height": "String",
  "image_width": "String",
  "size_bytes": "String",
  "size_compressed": "String",
  "sys_created_by": "String",
  "sys_created_on": "String",
  "sys_id": "String",
  "sys_mod_count": "String",
  "sys_tags": "String",
  "sys_updated_by": "String",
  "sys_updated_on": "String",
  "table_name": "String",
  "table_sys_id": "String",
  "updated_by_name": "String"
}
```

### POST multipart mandatory values

When sending a multipart POST request to upload a file attachment, include attachment data in the message body, not in the URL parameters. You must specify these values in the message body:

| Value        | Description                                                                                                                                                                                                                                                                                    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content-Type | Content-Type of the file, included in the message body for multipart uploads. **Note:** The Content-Type must be defined within the file portion of the POST message, not within the form data. See the sample POST multipart message for an example of a multipart message. Data type: String |
| table_name   | Name of the table to which you want to attach the file. Data type: String                                                                                                                                                                                                                      |
| table_sys_id | Sys_id of the record on the specified table to which you want to attach the file. Data type: String                                                                                                                                                                                            |

### cURL request

```
curl "https://instance.servicenow.com/api/now/attachment/upload" \
--request POST \
--header "Accept:application/json"\
--user "username":"password"\
--header "Content-Type:multipart/form-data"\
 -F 'table_name=incident' \
 -F 'table_sys_id=d71f7935c0a8016700802b64c67c11c6'\
 -F 'uploadFile=@ location of the file on file system'
\
```

```
{
  "result": {
    "table_sys_id": "d71f7935c0a8016700802b64c67c11c6",
    "size_bytes": "36597",
    "download_link": "https://instance.service-now.com/api/now/attachment/994adbc64f511200adf9f8e18110c796/file",
    "sys_updated_on": "2016-02-02 14:00:21",
    "sys_id": "994adbc64f511200adf9f8e18110c796",
    "image_height": "",
    "sys_created_on": "2016-02-02 14:00:21",
    "file_name": "banner-CS0001345_v1_1.jpeg",
    "sys_created_by": "admin",
    "compressed": "true",
    "average_image_color": "",
    "sys_updated_by": "admin",
    "sys_tags": "",
    "table_name": "incident",
    "image_width": "",
    "sys_mod_count": "0",
    "content_type": "image/jpeg",
    "size_compressed": "25130"
  }
}
```

## Attachment - PUT /now/attachment/{sys_id}/attributes/{attribute_key}

Updates the value of an existing attribute for an attachment.

Attributes are updated in the Attachment Attributes [sys_attachment_attribute] table.

### URL format

Versioned URL: `/api/now/{api_version}/attachment/{sys_id}/attributes/{attribute_key}`

Default URL: `/api/now/attachment/{sys_id}/attributes/{attribute_key}`

### Supported request parameters

**Path parameters**

| Name          | Description                                                                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_version   | Optional. Version of the endpoint to access. For example, `v1` or `v2`. Only specify this value to use an endpoint version other than the latest. Data type: String |
| sys_id        | Sys_id of the attachment. Data type: String Table: Attachment [sys_attachment]                                                                                      |
| attribute_key | Attribute key. Data type: String Table: Attachment Attributes [sys_attachment_attribute] Column: Key                                                                |

| Name | Description |
| ---- | ----------- |
| None |             |

**Request body**

| Name  | Description                                              |
| ----- | -------------------------------------------------------- |
| value | Required. New value for the attribute. Data type: String |

### Headers

These request and response headers apply only to this HTTP action or behave differently for this action.

**Request headers**

| Header       | Description                                                                                                                   |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Accept       | Data format of the response body. Supported types: **application/json** or **application/xml**. Default: **application/json** |
| Content-Type | Data format of the request body. Supported types: **application/json** or **application/xml**. Default: **application/json**  |

| Header | Description |
| ------ | ----------- |
| None   |             |

### Status codes

Selected status codes for this HTTP action:

| Status code | Description                                                        |
| ----------- | ------------------------------------------------------------------ |
| 200         | Successful. The request was successfully processed.                |
| 400         | Bad Request. A bad request type or malformed request was detected. |
| 404         | Not found. The requested item wasn't found.                        |

### Response body parameters (JSON or XML)

| Name         | Description                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------- |
| result       | Object containing the key-value pair for the attribute. Data type: Object. See the result example below. |
| result.key   | Attribute key. Data type: String Table: Attachment Attributes [sys_attachment_attribute] Column: Key     |
| result.value | Attribute value. Data type: String Table: Attachment Attributes [sys_attachment_attribute] Column: Value |

**result example**

```
"result": {
   "key": "String",
   "value": "String"
}
```

### cURL request

This example updates the value of the `example_key` attribute for the specified attachment.

```
curl "https://instance.service-now.com/api/now/attachment/a3af695b0a0006871b657c200acf62e0/attributes/example_key" \
--request PUT \
--header "Accept:application/json" \
--header "Content-Type:application/json" \
--data "{
  \"value\": \"new_value\"
}" \
--user 'username':'password'
```

Response body.

```
{
  "result": {
    "key": "example_key",
    "value": "new_value"
  }
}
```
