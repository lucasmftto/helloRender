from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def receive_event():
    return jsonify({"status": "success", "message": "Hello Bruno API"}), 200


if __name__ == '__main__':
    # Run the app on the local network, accessible on port 5000
    app.run(host='0.0.0.0', port=2999)
