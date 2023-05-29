# key_vault.py

from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from config import TENANT_ID, CLIENT_ID, CLIENT_SECRET, KEY_VAULT_NAME

def get_secret_client():
    credential = ClientSecretCredential(
        tenant_id=TENANT_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )

    key_vault_url = f"https://{KEY_VAULT_NAME}.vault.azure.net"
    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

    return secret_client

def create_or_update_secret(secret_name, secret_value):
    secret_client = get_secret_client()
    secret = secret_client.set_secret(secret_name, secret_value)
    return secret
