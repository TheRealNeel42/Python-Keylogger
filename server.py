from flask import Flask, jsonify, request
import base64

log_file_name = "server_logs.log"
PORT_NUMBER = 4040

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
	return "Server is Live..."

@app.route("/data/<string:_data>", methods=["GET"])
def get_data(_data):
	try:
		print("DATA BEGIN: ")
		d = str(_data)
		decodedBytes = base64.urlsafe_b64decode(d)
		string = str(decodedBytes)
		with open(log_file_name, "a") as f:
			f.write(string)
		f.close()
	except Exception as e:
		print(e)
		pass

	return str(1)

if __name__ == "__main__":
	app.run(port=PORT_NUMBER)