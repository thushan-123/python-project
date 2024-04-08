from flask import Blueprint, request, jsonify , abort

import jwt
import sys 

sys.path.append("../")
from genarate_id import id
from database import  db

SERECT_KEY="i am king of 21"



register_blueprint = Blueprint('register', __name__)


# users columns : id (primary key), f_name , l_name , address , mobile , password

@register_blueprint.route("/register", methods=['POST'])
def register():
    req = request.get_json()
    
    uid = id.gen_user_id()
    user_name = req["user_name"]
    f_name = req["f_name"]
    l_name = req["l_name"]
    address = req["address"]
    mobile = req["mobile"]
    user_password = req["password"]

    print(uid,f_name,l_name,address,mobile,user_password,user_name)

    query = "INSERT INTO users(id,f_name,l_name,address,mobile,user_password,user_name) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (uid,f_name,l_name,address,mobile,user_password,user_name)
    obj = db.insert()
    try:
        inser = obj.insert_data(query,values)
        print(inser)

    except  Exception as e:
        print (e)


    return jsonify({"status" : "insert sucessfully"})



@register_blueprint.route("/login", methods=['POST'])
def  login():
    try :
        req = request.get_json()
        user_name = req["user_name"]
        password = req["password"]
        query =f"SELECT * FROM users WHERE  user_name='{user_name}' AND  user_password='{password}'  LIMIT 1"
        obj = db.retrive()
        try :
            data =obj.select_data(query)
            if len(data)>0:
                #print(data[0][0],type(data),data[0][6])
                id = data[0][0]
                user = data[0][6] 
                
                
                
                token = jwt.encode({"user_id":id ,"user_name" : user},SERECT_KEY,algorithm="HS256")
                
                
                return jsonify({"status":"ok","token":token})
            else:
                return jsonify({"status":"error"})
        except :
            return jsonify({"status" : "error"})

    except :
        abort(404)


    
