Documentation:
Step-1: Set Up Mosquitto MQTT Broker:
    i)Create a Docker Network(Optional)
     docker network create mqtt-network

    ii)Run the Mosquitto MQTT broker container:
     docker run -d --name mosquitto-broker --network mqtt-network -p 1883:1883 eclipse-mosquitto

Step 2: Create the Python MQTT Client
    i) Install gmqtt:
    pip install gmqtt
    ii)Write the Python script to connect and listen for messages:
        mqtt_reader.py connects to mqtt using gmqtt and listens for messages by subscribing to "/events" topic.

Step 3: Dockerize the Python Application
    Create a Dockerfile for your Python application:
        created Dockerfile for the same.
    Build the Docker image for your Python application using below command:
    docker build -t mqtt-reader .
    Run the Docker container for your Python application:
    Note: Run the container on the same container as the Mosquitoo Broker

Step 4: Manually Publish a Message to the Topic
    Install mosquitto-clients on your system using below command:
    sudo apt-get install mosquitto-clients

    Publish a message to the topic:
    mosquitto_pub -h     -t "/events" -m '{"sensor_value":20.2}'



