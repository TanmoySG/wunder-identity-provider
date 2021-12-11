import flask
import flask_cors
app = flask.Flask(__name__)
flask_cors.CORS(app)


@app.route("/") 
def hello_world(): 
	return "<p>Hello, World!</p>"