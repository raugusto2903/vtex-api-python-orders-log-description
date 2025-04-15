import requests


# Endpoint de órdenes
def get_transaction_ids(order_id):
    # Reemplaza estos valores con los reales
    ACCOUNT_NAME = "tottoco"
    ENVIRONMENT = "vtexcommercestable"
    APP_KEY = "vtexappkey-tottoco-ZLNQHD"
    APP_TOKEN = "XZDEBEPNQWJWSFNNMVMWYBKXSJLPAQHNNPSSKNSBWOAAGHBGBPDPODUVOGLRSANZPVJCMVCYDLZKBKRLIFOLMRZKUXDEBAIWBALKXYTGMEMCDKUEOAJNLCNXWYIPRYWD"

    url = f"https://{ACCOUNT_NAME}.{ENVIRONMENT}.com.br/api/oms/pvt/orders/{order_id}"

    headers = {
        "X-VTEX-API-AppKey": APP_KEY,
        "X-VTEX-API-AppToken": APP_TOKEN,
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
