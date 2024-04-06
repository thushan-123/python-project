from flask import Flask
from form import register_blueprint  

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

app.register_blueprint(register_blueprint)  

if __name__ == "__main__":
    app.run(debug=True)

