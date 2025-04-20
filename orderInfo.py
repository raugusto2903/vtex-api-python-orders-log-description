import requests
import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv(dotenv_path='constants.env')


# Acceder a las variables


# Endpoint de órdenes
def get_transaction_ids(order_id):
    account_name = os.getenv("ACCOUNT_NAME")
    environment = os.getenv("ENVIRONMENT")
    app_key = os.getenv("APP_KEY")
    app_token = os.getenv("APP_TOKEN")
    print("accountname : " + account_name)
    url = f"https://{account_name}.{environment}.com.br/api/oms/pvt/orders/{order_id}"

    headers = {
        "X-VTEX-API-AppKey": app_key,
        "X-VTEX-API-AppToken": app_token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Error al consultar orden {order_id}: {response.status_code}")
        return []

    data = response.json()

    transaction_ids = []

    if "paymentData" in data and "transactions" in data["paymentData"]:
        for tx in data["paymentData"]["transactions"]:
            transaction_ids.append(tx.get("transactionId"))
    else:
        print(f"⚠️ Orden {order_id} no contiene 'paymentData.transactions'")

    return transaction_ids
