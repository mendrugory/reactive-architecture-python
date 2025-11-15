# Initial Image
FROM python:3.9-slim

# Dependencies
RUN apt-get update && apt-get upgrade -y

# Create folders
RUN mkdir -p /opt/reactive-architecture/resources-analyzer

# Copy files
ADD ./resources-analyzer/ /opt/reactive-architecture/resources-analyzer

# Permissions
RUN chmod +x /opt/reactive-architecture/resources-analyzer/analyzer.py

# Installing dependencies
RUN pip3 install -r /opt/reactive-architecture/resources-analyzer/requirements.txt

CMD ["python3", "/opt/reactive-architecture/resources-analyzer/analyzer.py"]
