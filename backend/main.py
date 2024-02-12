from flask import Flask
from routes.data_route import data_blueprint
from routes.eval_route import eval_blueprint
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.register_blueprint(
    data_blueprint, url_prefix="/data"
)  ## where we handle the data upload
app.register_blueprint(
    eval_blueprint, url_prefix="/eval"
)  ## where we chunk, query GPT, and send back results

if __name__ == "__main__":
    app.run(debug=True)
