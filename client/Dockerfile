FROM python:3.10

# Install client dependencies and copy client files
WORKDIR /chat/client
COPY client/requirements.txt .
RUN pip install -r requirements.txt
COPY client .

# Start the client
CMD ["python", "chat_client.py"]
