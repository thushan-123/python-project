from flask import Flask
import form.register 

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

app.register_blueprint(blueprint)

if __name__ == "__main__" :
    app.run(debug=True)

