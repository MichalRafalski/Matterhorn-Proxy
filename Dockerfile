# Use a lightweight ARM base image
FROM arm32v7/alpine:latest

# Install Tinyproxy
RUN apk add --no-cache tinyproxy

# Copy the Tinyproxy configuration file
COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf

# Install dependencies: OpenVPN, HAProxy, Python3, and Gunicorn
RUN apk update && \
    apk add --no-cache openvpn python3 py3-pip bash

# Copy OpenVPN configuration and credentials
COPY config.ovpn /etc/openvpn/config.ovpn

# Set up a Python virtual environment
RUN python3 -m venv /venv

# Ensure the virtual environment is used for subsequent commands
ENV PATH="/venv/bin:$PATH"


# Install Flask and Gunicorn for the Python API
RUN pip install Flask requests gunicorn

# Create the app directory and set it as the working directory
WORKDIR /app

# Copy the Python API script
COPY vpn_api.py /app/vpn_api.py

# Expose ports for HAProxy and Flask API
EXPOSE 8888
EXPOSE 2211

# Start Tinyproxy and Gunicorn
CMD ["bash", "-c", "tinyproxy -c /etc/tinyproxy/tinyproxy.conf -d & gunicorn -b 0.0.0.0:2211 vpn_api:app"]
