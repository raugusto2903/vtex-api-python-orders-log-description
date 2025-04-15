import requests

# Reemplaza estos valores con los reales
ACCOUNT_NAME = "tottoco"
ENVIRONMENT = "vtexcommercestable"
APP_KEY = "vtexappkey-tottoco-ZLNQHD"
APP_TOKEN = "XZDEBEPNQWJWSFNNMVMWYBKXSJLPAQHNNPSSKNSBWOAAGHBGBPDPODUVOGLRSANZPVJCMVCYDLZKBKRLIFOLMRZKUXDEBAIWBALKXYTGMEMCDKUEOAJNLCNXWYIPRYWD"
ORDEN = "1523910520810-01"
# Endpoint de órdenes
url = f"https://{ACCOUNT_NAME}.{ENVIRONMENT}.com.br/api/oms/pvt/orders/"

headers = {
    "X-VTEX-API-AppKey": APP_KEY,
    "X-VTEX-API-AppToken": APP_TOKEN,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Puedes añadir parámetros como ?f_creationDate=2024-01-01T00:00:00Z
response = requests.get(url, headers=headers)

if response.status_code == 200:
    orders = response.json()
    print("Órdenes encontradas:", orders)
else:
    print("Error al consultar la API:", response.status_code)
    print(response.text)
