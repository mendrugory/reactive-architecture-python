# Initial Image
FROM ubuntu:14.04

# Dependencies
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install python3-pip -y

# Create folders
RUN mkdir -p /opt/reactive-architecture/resources-web

# Copy files
ADD ./resources-web/ /opt/reactive-architecture/resources-web

# Permissions
RUN chmod +x /opt/reactive-architecture/resources-web/web.py

# Installing dependencies
RUN pip3 install -r /opt/reactive-architecture/resources-web/requirements.txt

EXPOSE 8888

CMD /opt/reactive-architecture/resources-web/web.py
