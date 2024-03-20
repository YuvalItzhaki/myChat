FROM python:3.9


# Install server dependencies and copy server files
WORKDIR /chat/server
COPY server/requirements.txt .
RUN pip install -r requirements.txt
COPY server .

# Expose server port
EXPOSE 5000

# Start the server
CMD ["python", "chat_server.py"]

# Install client dependencies and copy client files
WORKDIR /chat/client
COPY client/requirements.txt .
RUN pip install -r requirements.txt
COPY client .



# Start the client
CMD ["python", "chat_client.py"]

