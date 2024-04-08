from flask import Blueprint , request , jsonify,abort
import sys
sys.path.append("../")

from database import db
from jwt_token_validation import is_token_valied
from genarate_id import id
from ai_model import get_into_predicition

SERECT_KEY="i am king of 21"

comment = Blueprint('comment',__name__)

#add a comment  require token,comment,date,user_id,artical_id

@comment.route("/user/comment", methods=[ "POST","GET"])
def  user_comments():
    try :
        req = request.get_json()
        comment_id = id.gen_comm_id()
        token = req["token"]
        comment = req["comment"]
        review = get_into_predicition(comment)
        date = req["date"]
        user_id = req["user_id"]
        artical_id = req["artical_id"]
        valied_token =is_token_valied(token, SERECT_KEY)
        print(comment,review)
        #if valied_token != False:
        return "ok"



    except Exception as e:
        return jsonify({str(e)})