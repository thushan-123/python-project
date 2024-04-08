from flask import Blueprint , request , jsonify,abort
import sys
sys.path.append("../")

from database import db
from jwt_token_validation import is_token_valied
from genarate_id import id

SERECT_KEY="i am king of 21"

artical = Blueprint('add_artical',__name__)

#sent to data in json   token,title,content,date,

@artical.route( "/artical/add", methods=["POST"] )
def add_artical():
    try:
        req = request.get_json()
        art_id = id.gen_art_id()
        token = req["token"]
        valied_tk = is_token_valied(token,SERECT_KEY)
        title = req["title"]
        content = req["content"]
        date = req["date"]
        user_id =  valied_tk["user_id"]

        #check the valied user
        if valied_tk != False:
            
            query ="INSERT INTO articale(artical_id,title,artical_content,artical_date,id) VALUES (%s,%s,%s,%s,%s)"
            
            values =(art_id,title,content,date,user_id)
            #insert to data to db table articale table
            obj =db.insert()
            result = obj.insert_data(query,values)
            return jsonify({"status": result})
        
        return jsonify({"error":"Token not valid"}),403
        
        

    except Exception as e:
       # return jsonify({"error": str(e)}) 
       abort(404)
        
    