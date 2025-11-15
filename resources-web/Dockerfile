# Initial Image
FROM python:3.9-slim

# Dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y gcc && \
    rm -rf /var/lib/apt/lists/*

# Create folders
RUN mkdir -p /opt/reactive-architecture/resources-web

# Copy files
ADD ./resources-web/ /opt/reactive-architecture/resources-web

# Permissions
RUN chmod +x /opt/reactive-architecture/resources-web/web.py

# Installing dependencies
RUN pip3 install -r /opt/reactive-architecture/resources-web/requirements.txt

EXPOSE 8888

CMD ["python3", "/opt/reactive-architecture/resources-web/web.py"]
