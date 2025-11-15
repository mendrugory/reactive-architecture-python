# Initial Image
FROM python:3.9-slim

# Dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y gcc && \
    rm -rf /var/lib/apt/lists/*

# Create folders
RUN mkdir -p /opt/reactive-architecture/resources-tracker

# Copy files
ADD ./resources-tracker/ /opt/reactive-architecture/resources-tracker

# Permissions
RUN chmod +x /opt/reactive-architecture/resources-tracker/tracker.py

# Installing dependencies
RUN pip3 install -r /opt/reactive-architecture/resources-tracker/requirements.txt

CMD ["python3", "/opt/reactive-architecture/resources-tracker/tracker.py"]
