from flask import Flask
from routes.data_route import data_blueprint
from routes.eval_route import eval_blueprint

app = Flask(__name__)
app.register_blueprint(data_blueprint, url_prefix="/data")
app.register_blueprint(eval_blueprint, url_prefix="/eval")

if __name__ == "__main__":
    app.run(debug=True)
