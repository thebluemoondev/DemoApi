from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/demo', methods=['GET'])
def get_status():
    return jsonify({
        "status": "Online",
        "message": "Smart Gym Server is running on Raspberry Pi!",
        "user": "Thành"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)