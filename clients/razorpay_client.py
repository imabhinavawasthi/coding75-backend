import os
import razorpay
client = razorpay.Client(auth=(os.getenv("RAZORPAY_API_KEY_ID"), os.getenv("RAZORPAY_API_KEY_SECRET")))
client.set_app_details({"title": "Coding75", "version": "25.10.18"})