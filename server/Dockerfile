FROM python:3.10

# Install server dependencies and copy server files
WORKDIR /chat/server
COPY server/requirements.txt .
RUN pip install -r requirements.txt
COPY server .

# Expose server port
EXPOSE 5000

# Start the server
CMD ["python", "chat_server.py"]
