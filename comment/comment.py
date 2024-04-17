from flask import Blueprint , request , jsonify,abort
from datetime import datetime
import sys
sys.path.append("../")

from database import db
from jwt_token_validation import is_token_valied
from genarate_id import id
from ai_model import get_into_predicition

SERECT_KEY="i am king of 21"

comment = Blueprint('comment',__name__)

#add a comment  require token,comment,artical_id

@comment.route("/user/comment", methods=[ "POST","GET"])
def  user_comments():
    try :
        req = request.get_json()

        comment_id = id.gen_comm_id()
        token = req["token"]
        comment = req["comment"]
        prediction = get_into_predicition(comment)
        date = datetime.now()
        artical_id = req["artical_id"]

        #validate token
        valied_token =is_token_valied(token, SERECT_KEY)
        user_id =valied_token["user_id"]

        print(comment_id,comment,prediction,date,user_id,artical_id)

        if valied_token != False:
            query = "INSERT INTO user_comment(comment_id,comment_content,c_date,artical_id,id,prediction) VALUES (%s,%s,%s,%s,%s,%s) "
            values = (comment_id,comment,date,artical_id,user_id,prediction)
            #call to method in db package
            obj = db.insert()
            result = obj.insert_data(query,values)
            return jsonify({"status" : "sucess"})
        else:
            return jsonify({"error"}),403



    except Exception as e:
        print(str({e}))
        return jsonify({"error" : str(e)})
       # abort(404)