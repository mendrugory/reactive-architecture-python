# Initial Image
FROM ubuntu:14.04

# Dependencies
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install python3-pip -y

# Create folders
RUN mkdir -p /opt/reactive-architecture/resources-tracker

# Copy files
ADD ./resources-tracker/ /opt/reactive-architecture/resources-tracker

# Permissions
RUN chmod +x /opt/reactive-architecture/resources-tracker/tracker.py

# Installing dependencies
RUN pip3 install -r /opt/reactive-architecture/resources-tracker/requirements.txt


CMD /opt/reactive-architecture/resources-tracker/tracker.py
