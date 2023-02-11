from flask import Response
from flask import jsonify

def loginUser(data,collection):
    userData=collection.find_one({"email":data["email"]})
    if(userData['password']==data['password']):
        return jsonify(['logged in successfully'])
    else:
        return Response(" invalid email/password ",status=205)