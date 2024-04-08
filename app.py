from flask import Flask,session,abort
from flask_session import Session
import sys 
sys.path.append("../")
from form import register_blueprint  
from artical import artical
from comment import comment


app = Flask(__name__)

SESSION_TYPE ="filesystem"
app.config.from_object(__name__)
Session(app)

@app.route('/')
def home():
    abort(404)

app.register_blueprint(register_blueprint)  
app.register_blueprint(artical)
app.register_blueprint(comment)


if __name__ == "__main__":
    app.run(debug=True)

