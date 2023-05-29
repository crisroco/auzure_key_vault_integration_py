# main.py

from key_vault import create_or_update_secret

secret_name = "newsecretaes256"
secret_value = "3a76c5b456d9f1e028687a4b86c34e29a832d7d9f1e028687a4b86c34e29a832"

response = create_or_update_secret(secret_name, secret_value)
print(response)
