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

class user_id :
    def gen_user_id(self):
        retrive_class = db.retrive()
        query = "SELECT MAX(id) FROM users"
        get_last_user_id  = retrive_class.select_data(query)
        user_id = get_last_user_id[0][0]
        number = int(user_id[2:])+1
        new_user_id = "FE" + int_convert_len3_str(number)
        return new_user_id

class articale:
    def gen_art_id(self):
        retrive_class = db.retrive()
        query = "SELECT MAX(artical_id) FROM articale"
        get_last_artical_id  = retrive_class.select_data(query)
        articale_id = get_last_artical_id[0][0]
        number = int(articale_id[2:])+1
        new_articale_id = "AT" + int_convert_len3_str(number)
        return new_articale_id

class comment_id:
    def gen_comm_id(self):
        retrive_class = db.retrive()
        query = "SELECT MAX(comment_id) FROM user_comment"
        get_last_commnet_id= retrive_class.select_data(query)
        commnet_id = int(get_last_commnet_id[0][0])
        new_cmm_id = commnet_id + 1
        return str(new_cmm_id)
        

print(user_id().gen_user_id(),articale().gen_art_id(),comment_id().gen_comm_id())
