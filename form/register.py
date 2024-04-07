from flask import Blueprint, request, jsonify 
import sys 

sys.path.append("../")
from genarate_id import id
from database import  db


register_blueprint = Blueprint('register', __name__)

# users columns : id (primary key), f_name , l_name , address , mobile , password

@register_blueprint.route("/register", methods=['POST'])
def register():
    req = request.get_json()
    
    uid = id.gen_user_id()
    f_name = req["f_name"]
    l_name = req["l_name"]
    address = req["address"]
    mobile = req["mobile"]
    user_password = req["password"]

    print(uid,f_name,l_name,address,mobile,user_password)

    query = "INSERT INTO users(id,f_name,l_name,address,mobile,user_password) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (uid,f_name,l_name,address,mobile,user_password)
    obj = db.insert()
    try:
        inser = obj.insert_data(query,values)
        print(inser)

    except  Exception as e:
        print (e)


    return jsonify({"status" : "insert sucessfully"})



@register_blueprint.route("/login", methods=['POST'])
def  login():
    return "hii"
    
