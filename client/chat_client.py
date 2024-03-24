import requests
import time
import threading
from pymongo import MongoClient

SERVER_URL = 'http://127.0.0.1:5000/'


def get_rooms():
    response = requests.get(f"{SERVER_URL}/get_rooms")
    if response.status_code == 200:
        rooms = response.json()
        print("Available Rooms:")
        for room in rooms:
            print(room)
    else:
        print("Failed to fetch rooms from server")
    return

def check_room_exist(room):
    response = requests.get(f"{SERVER_URL}/get_rooms")
    rooms = response.json()
    if room in rooms:
        return True
    else:
        print("Room doesnt exist")
        return False

def choose_room():
    while True:
        room = input("Enter the name of the room: ")
        if check_room_exist(room):
            return room


def get_mongo_client():
    return MongoClient('mongodb://127.0.0.1:27017/')


def get_messages():
    client = get_mongo_client()
    db = client['myChat']
    messages_collection = db['messages']
    messages = list(messages_collection.find({}, {'_id': 0}))
    return messages


def send_message(room, username, message):
    # Retry connecting to MongoDB with a delay
    max_retries = 3
    retry_delay = 1  # seconds
    for attempt in range(max_retries):
        try:
            client = get_mongo_client()
            db = client['myChat']  # Replace 'myChat' with your database name
            messages_collection = db['messages']
            data = {'join_room': room, 'username': username, 'message': message}
            messages_collection.insert_one(data)
            print("Message sent successfully")
            return  # Success, exit retry loop
        except Exception as e:
            print(f"Failed to send message (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries exceeded. Giving up.")
                return


def poll_messages(room, username):
    if True:
        messages = get_messages()
        for msg in messages:
            print(f"{msg['username']}: {msg['message']}")
        time.sleep(1)


def main():
    get_rooms()
    room = choose_room()
    print(f"Chosen room: {room}")
    check_room_exist(room)
    username = input("Enter your username: ")

    # Start a separate thread to poll messages continuously
    threading.Thread(target=poll_messages, args=(room, username,), daemon=True).start()

    # Main loop to send messages
    while True:
        message = input("Enter message: ")
        send_message(room, username, message)


if __name__ == "__main__":
    main()
