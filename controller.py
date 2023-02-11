import json
import pymongo

from flask import Flask, Response, jsonify, request
from flask_cors import CORS, cross_origin  
from mongoConnect import connectToDB
from login import loginUser

db = connectToDB()

app = Flask(__name__)
CORS(app)

#-------------------register-user------------------------
@app.route("/app/saveUser",methods=['post'])
@cross_origin()
def saveUser():
    data=request.data
    data=json.loads(data.decode())
    
    try:
        userCollection = db['users']
        checkUser=userCollection.find_one({"email":data["email"]})
        if(checkUser):
            return Response("user already exist with same email",status=205)
        else:
            userCollection.insert_one(data)
            return jsonify(["registered successfully"])
    except Exception as e:
        print(e)
        return  jsonify(["unable to register, Try after sometime"])

#-----------------------login-user-----------------------------------
@app.route('/app/login', methods =['post'])
@cross_origin()
def login():
    data=request.data
    data=json.loads(data.decode())
    userCollection = db["users"]
    return loginUser(data,userCollection) 


if __name__ == '__main__':
  
    app.run(debug = True)