import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv(dotenv_path='constants.env')


def get_transaction_interactions(transaction_id):
    account_name = os.getenv("ACCOUNT_NAME")
    app_key = os.getenv("APP_KEY")
    app_token = os.getenv("APP_TOKEN")
    url = f"https://{account_name}.vtexpayments.com.br/api/pvt/transactions/{transaction_id[0]}/interactions"

    headers = {
        "X-VTEX-API-AppKey": app_key,
        "X-VTEX-API-AppToken": app_token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Error al consultar interacciones de transacción {transaction_id}")
        print(f"Status: {response.status_code} - {response.text}")
        return None
