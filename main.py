# main.py
import json

from orderInfo import get_transaction_ids
from transacctionInfo import get_transaction_interactions

archivo = r'D:/ramirold/OneDrive - Nalsani S.A.S/Documentos/pruebas postman/prueba2.json'

with open(archivo, 'r', encoding='utf-8') as f:
    data = json.load(f)

ordenes = data.get("list", [])
ordenes_payment_pending = [orden for orden in ordenes if orden.get('status') == 'payment-pending']

print(f"🔎 Órdenes con estado 'payment-pending': {len(ordenes_payment_pending)}\n")
interacciones_por_orden = {}
for orden in ordenes_payment_pending:
    order_id = orden.get("orderId")
    print(f"➡️ Procesando orden: {order_id}")

    transaction_id = get_transaction_ids(order_id)

    print(f"   🔁 Transacción encontrada: {transaction_id}")
    interactions = get_transaction_interactions(transaction_id)

    if interactions:
        print(f"   🧾 Interacciones:")
        for i in interactions:
            print(i)
        interacciones_por_orden[order_id] = interactions
        with open("interacciones.json", "w", encoding="utf-8") as f:
            json.dump(interacciones_por_orden, f, ensure_ascii=False, indent=4)
    else:
        print("   ⚠️ No se encontraron interacciones.")
    print("-" * 60)
