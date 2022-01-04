from django.conf import settings
from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = settings.AZURE_ACCOUNT_NAME
    sas_token = settings.AZURE_SAS_TOKEN_MEDIA
    azure_container = settings.AZURE_STATIC_CONTAINER
    expiration_secs = None
    overwrite_files = True


class AzureStaticStorage(AzureStorage):
    account_name = settings.AZURE_ACCOUNT_NAME
    sas_token = settings.AZURE_SAS_TOKEN
    azure_container = settings.AZURE_STATIC_CONTAINER
    expiration_secs = None