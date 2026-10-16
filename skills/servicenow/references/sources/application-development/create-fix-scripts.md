# Create a fix script

Create fix scripts to ensure the system installs or updates an application properly.

## Before you begin

Role required: script_fix_admin or admin

## About this task

Use fix scripts to add, update, and delete data, including rules, scripts, and property settings.

## Procedure

1. Navigate to **All** > **System Definition** > **Fix Scripts**.

2. Click **New**.

3. Define the fix script by filling in the fields on the form.

   | Field               | Description                                                                                                                         |
   | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
   | Name                | Unique, descriptive name for the fix script.                                                                                        |
   | Unloadable          | Option to create Customer Update records [sys_update_xml] when the fix script runs. Fix script tests enforce the Unloadable option. |
   | Before              | Option to run the fix script before installing or upgrading the application.                                                        |
   | Record for rollback | Option to record execution of the script so that it can be reverted if needed.                                                      |
   | Description         | Description of the fix script.                                                                                                      |
   | Script              | Code for the fix script.                                                                                                            |

4. Click **Submit**.

5. Test the fix script and make any necessary changes.
