from flask import Flask, request, jsonify, redirect, url_for
import os
import json
import requests
import traceback
import base64
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
 
app = Flask(__name__)

@app.route("/lyra_payin",methods=['GET','POST'])
def lyra_payin():
    request_data = {
              "orderId": "It-23920DK-1",
              "orderInfo": "Shopping cart with #1 item 23920DK",
              "currency": "INR",
              "amount": 100,
              "customer": {
                "name": "swathi",
                "emailId": "swathi@gmail.com",
                "phone": "+1234567890"
              },
              "webhook": {
                "url": "http://18.188.39.218/api/frontend/lyra_testing_callback"
              }
            }
      
    headers ={
        "Content-Type": "application/json",
        "Accept": "application/json",
        }
    
    url = "https://api.in.lyra.com/pg/rest/v1/charge"
    username = "20753740"
    password = "testpassword_j98abAdPr1sUznplPZksKwKlhxq8WAIG0GkEeUPUXppeH"
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    headers["Authorization"] = f"Basic {encoded_credentials}"
    
    try:
        lyraresponse = requests.post(url, json=request_data, headers=headers)
        lyraCreatePaymentResponseData = json.loads(lyraresponse.text)
        return jsonify(lyraCreatePaymentResponseData), 200
    
    except Exception as e:
        print("Internal Server Error",e)
        return jsonify({"error":"Internal Server Error"}), 500


@app.route("/lyra_payin_status",methods=['GET','POST'])
def lyra_payin_status():
    uuid= "718ba70c1f834436afc387cc4c4304c5"
    headers ={
        "Content-Type": "application/json",
        "Accept": "application/json",
        }
    
    url = f"https://api.in.lyra.com/pg/rest/v1/charge/{uuid}"
    username = "20753740"
    password = "testpassword_j98abAdPr1sUznplPZksKwKlhxq8WAIG0GkEeUPUXppeH"
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    headers["Authorization"] = f"Basic {encoded_credentials}"

    try:
        lyraresponsestatus = requests.get(url,headers=headers)
        lyraCreatePaymentResponseData = json.loads(lyraresponsestatus.text)
        return jsonify(lyraCreatePaymentResponseData), 200
    
    except Exception as e:
        print("Internal Server Error",e)
        return jsonify({"error":"Internal Server Error"}), 500
    

@app.route("/lyra_testing_callback",methods=["POST"])
def lyra_testing_callback():
    data_status = {"responseStatus":1, "result": "success"}
    print(request.json,"lyra card check term request.json")
    print(request.data,"lyra card check term request.data")
    print(request.form,"lyra card check term request.form")
    print("(((((((((((((((((lyra card check term Response Data)))))))))))))))))")
    return 

if __name__ == '__main__':
    app.run(debug=True)