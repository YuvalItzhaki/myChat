import requests
import time
import threading

SERVER_URL = 'http://172.17.0.2:5000/'
def get_messages():
    response = requests.get(f"{SERVER_URL}/messages")
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch messages from server")
        return []


def send_message(username, message):
    data = {'username': username, 'message': message}
    response = requests.post(f"{SERVER_URL}/messages", json=data)
    if response.status_code == 201:
        print("Message sent successfully")
    else:
        print("Failed to send message")


def poll_messages(username):
    while True:
        messages = get_messages()
        for msg in messages:
            print(f"{msg['username']}: {msg['message']}")
        time.sleep(1)


def main():
    username = input("Enter your username: ")

    # Start a separate thread to poll messages continuously
    threading.Thread(target=poll_messages, args=(username,), daemon=True).start()

    # Main loop to send messages
    while True:
        message = input("Enter message: ")
        send_message(username, message)


if __name__ == "__main__":
    main()
