from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []



@app.route('/messages', methods=['POST'])
def send_message():
    data = request.json
    username = data.get('username')
    message = data.get('message')
    if username and message:
        messages.append({'username': username, 'message': message})
        return jsonify({'message': 'Message sent successfully'}), 201
    else:
        return jsonify({'error': 'Invalid request parameters'}), 400

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
