# StorageTestPython

Directly deploy to app service and troubleshoot

PRE-REQUISITES:

You need to have a storage account with public access disabled


Mount the storage account to app service - https://docs.microsoft.com/en-us/azure/app-service/configure-connect-to-azure-storage?tabs=portal&pivots=container-linux 


On Appservice, use the mount path as "/home/site/wwwroot/static" or to any other storage path on app service.

If you are using other path than "/home/site/wwwroot/static". Please change the respective path in code too


On Appservice, add app setting to disable collect static [DISABLE_COLLECTSTATIC to true]


