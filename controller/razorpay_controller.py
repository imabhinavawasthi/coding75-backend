from flask import Blueprint, jsonify, request
from models.request.razorpay.CreateOrderRequest import CreateOrderRequest
from clients.razorpay_client import client

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/create-order", methods=["POST"])
def create_order():
    data = request.json
    if not data:
        return jsonify({"error": "Missing request body"}), 400

    # Validate required fields
    required_fields = ["amount", "currency", "receipt"]
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"Missing required field: {field}"}), 400
        
    order_data = CreateOrderRequest(
        amount=data["amount"],
        currency=data["currency"],
        receipt=data["receipt"]
    )
    return jsonify(client.order.create(data=order_data.to_dict())), 200

@payment_bp.route("/get-order/<order_id>", methods=["GET"])
def get_order(order_id):
    try:
        order = client.order.fetch(order_id)
        return jsonify(order), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400