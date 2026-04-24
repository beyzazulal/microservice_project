from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

orders = {}
next_id = 1

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service:5001")

def user_exists(user_id):
    try:
        response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}", timeout=3)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(list(orders.values()))

@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order)

@app.route("/orders", methods=["POST"])
def create_order():
    global next_id
    data = request.get_json()
    if not data or "user_id" not in data or "product" not in data:
        return jsonify({"error": "user_id and product are required"}), 400
    if not user_exists(data["user_id"]):
        return jsonify({"error": "User not found"}), 404
    order = {
        "id": next_id,
        "user_id": data["user_id"],
        "product": data["product"],
        "status": "pending"
    }
    orders[next_id] = order
    next_id += 1
    return jsonify(order), 201

@app.route("/orders/<int:order_id>/status", methods=["PUT"])
def update_status(order_id):
    if order_id not in orders:
        return jsonify({"error": "Order not found"}), 404
    data = request.get_json()
    if "status" not in data:
        return jsonify({"error": "status is required"}), 400
    orders[order_id]["status"] = data["status"]
    return jsonify(orders[order_id])

@app.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    if order_id not in orders:
        return jsonify({"error": "Order not found"}), 404
    del orders[order_id]
    return jsonify({"message": "Order deleted"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "order-service"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
