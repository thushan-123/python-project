from flask import Blueprint , request , jsonify,abort
import sys
from datetime import datetime
sys.path.append("../")

from database import db
from jwt_token_validation import is_token_valied
from genarate_id import id

SERECT_KEY="i am king of 21"

artical = Blueprint('add_artical',__name__)

#sent to data in json   token,title,content

@artical.route( "/artical/add", methods=["POST"] )
def add_artical():
    try:
        req = request.get_json()
        art_id = id.gen_art_id()
        token = req["token"]
        valied_tk = is_token_valied(token,SERECT_KEY)
        title = req["title"]
        content = req["content"]
        date = datetime.now()
        user_id =  valied_tk["user_id"]

        #check the valied user
        if valied_tk != False:
            
            query ="INSERT INTO articale(artical_id,title,artical_content,artical_date,id) VALUES (%s,%s,%s,%s,%s)"
            
            values =(art_id,title,content,date,user_id)
            #insert to data to db table articale table
            obj =db.insert()
            result = obj.insert_data(query,values)
            return jsonify({"status":"sucess"})
        
        return jsonify({"error":"Token not valid"}),403        

    except Exception as e:
        abort(404)
        
@artical.route("/artical/all",methods=["GET","POST"])
def get_all_articals():
    try:
        query = "SELECT * FROM  articale ORDER BY artical_date DESC"
        obj = db.retrive()
        result = obj.select_data(query)
        result_set = []

        for x in result:
            # get a count of positive comment in each artical 
            temp_query_p = f"SELECT COUNT(prediction) FROM user_comment WHERE artical_id = '{x[0]}' AND prediction = 'positive'"
            # get a count of negative comment in each artical
            temp_query_n = f"SELECT COUNT(prediction) FROM user_comment WHERE artical_id = '{x[0]}' AND prediction = 'negative'"

            #get all comment in each artical
            c_query = f"SELECT * FROM user_comment WHERE artical_id='{x[0]}' "
            rows_comment = obj.select_data(c_query)
            comment =[]
            for i in rows_comment :
                temp_comment ={"comment_id" : i[0],
                               "content" : i[1],
                               "c_date" : i[2],
                               "user_id" : i[4],
                               "prediction" : i[5]
                               }
                comment.append(temp_comment)
            p_result = obj.select_data(temp_query_p)
            n_result = obj.select_data(temp_query_n)
            temp_result ={
                          "artical_id" : x[0],
                          "title" : x[1],
                          "content" : x[2],
                          "date" : x[3],
                          "user_id" :x[4],
                          "positive" :p_result[0][0],
                          "negative" :n_result[0][0],
                          "comments" : comment,
                          }
            result_set.append(temp_result)
            
        return jsonify(result_set)
    except Exception as e :
        print(str({e}))
        abort(404) 

# get selected artical details    json req artical_id

@artical.route("/artical/select", methods=["POST","GET"])
def get_selected_artical_details():
    try:
        data = request.get_json()
        artical_id = data["artical_id"]
        query = f"SELECT * FROM user_comment WHERE artical_id = '{artical_id}'"
        obj =db.retrive()
        result = obj.select_data(query)
        comments =[]

        if len(result) == 0:
            return jsonify({"status" : "artical not found"})
        
        for x in result:
            temp_result ={
                "comment_id" : x[0],
                "content" : x[1],
                "c_date" : x[2],
                "user_id" : x[4],
                "prediction" : x[5]
            }
            comments.append(temp_result)

        return jsonify(comments)
     
    except Exception as e:
        abort (404)




