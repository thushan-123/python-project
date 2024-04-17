import sys
sys.path.append("../")
from database import db

def int_convert_len3_str(number):
    str_num  = str(number)
    if len(str_num) == 3:
        return  str_num 
    else :
        while  len(str_num) < 3:
            str_num = '0'+str_num
        return str_num


# users columns : id (primary key), f_name , l_name , address , mobile , password
# articale  columns : artical_id (primary key), title ,artical_content ,artical_date , id (foreign key from users)
# user_comment columns : comment_id (primary key) , comment_content , c_date , review (bool) ,artical_id(foreign key) ,user_id(foreigen key)

# genarate a user id  for new users.


def gen_user_id():
    retrive_class = db.retrive()
    query = "SELECT MAX(id) FROM users"
    get_last_user_id = retrive_class.select_data(query)
    last_user_id = get_last_user_id[0][0]

    if last_user_id is None or not last_user_id.startswith("FE"):  
        # If no user exists yet or the user ID is not in the expected format
        new_user_id = "FE006"
    else:
        try:
            number = int(last_user_id[2:]) + 1
            new_user_id = "FE" + int_convert_len3_str(number)
        except (TypeError, ValueError):
            # Handle cases where the retrieved user ID is not in the expected format
            # or cannot be converted to an integer
            new_user_id = "FE006"  # Fallback to a default ID

    return new_user_id


def gen_art_id():
        retrive_class = db.retrive()
        query = "SELECT MAX(artical_id) FROM articale"
        get_last_artical_id  = retrive_class.select_data(query)
        articale_id = get_last_artical_id[0][0]
        if articale_id is None or not articale_id.startswith("FE"):  
        # If no user exists yet or the user ID is not in the expected format
            new_artical_id = "AT006"
        else:
            try:
                number = int(articale_id[2:]) + 1
                new_artical_id = "AT" + int_convert_len3_str(number)
            except (TypeError, ValueError):
                # Handle cases where the retrieved user ID is not in the expected format
                # or cannot be converted to an integer
                new_artical_id = "AT006"  # Fallback to a default ID
        return new_artical_id

def gen_comm_id():
        retrive_class = db.retrive()
        query = "SELECT MAX(comment_id) FROM user_comment"
        get_last_commnet_id= retrive_class.select_data(query)
        try:
             commnet_id = int(get_last_commnet_id[0][0])
        except :
             commnet_id = 0
        new_cmm_id = commnet_id + 1
        return new_cmm_id
        


