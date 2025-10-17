from flask import Flask
from controller.products import products_bp
from controller.health import health_bp
from controller.razorpay_controller import payment_bp

app = Flask(__name__)

# Register blueprint
app.register_blueprint(health_bp, url_prefix="/api")
app.register_blueprint(products_bp, url_prefix="/api/products")
app.register_blueprint(payment_bp, url_prefix="/api/payment")

if __name__ == "__main__":
    app.run(debug=True)

# export FLASK_APP=index.py
# flask run -p 5328