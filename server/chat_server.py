from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['myChat']  # Replace 'myChat' with your database name
messages_collection = db['messages']


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    username = data.get('username')
    message = data.get('message')
    if username and message:
        messages_collection.insert_one({'username': username, 'message': message})  # Use insert_one() method
        return jsonify({'message': 'Message sent successfully'}), 201
    else:
        return jsonify({'error': 'Invalid request parameters'}), 400


@app.route('/send_message/<username>', methods=['GET'])
def get_messages(username):
    messages = list(messages_collection.find({'username': username}, {'_id': 0}))  # Exclude '_id' field from the response
    return jsonify(messages)


# active_rooms = set()

active_rooms = ["Room1", "Room2", "Room3"]  # Sample list of active rooms

@app.route('/get_rooms', methods=['GET'])
def get_rooms():
    return jsonify(active_rooms)

@app.route('/join_room', methods=['POST'])
def join_room():
    data = request.json
    room_name = data.get('room_name')

    if room_name in active_rooms:
        # Room exists, allow user to join
        return jsonify({'message': f'Joined room {room_name}'}), 200
    else:
        # Room does not exist, return error
        return jsonify({'error': f'Room {room_name} does not exist'}), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
