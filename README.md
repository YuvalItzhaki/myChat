Chat 

1. Build the Docker image for the server:

   docker build -t chat-server -f server/Dockerfile .

2. Run the Docker container:

    docker run -p 5000:5000 chat-server

Now your chat server with a REST API should be running inside a Docker container. You can send requests to http://localhost:5000/messages

1. Build the Docker image for the client:

   docker build -t chat-client -f client/Dockerfile .

2. Run client:

   docker run -it chat-client 