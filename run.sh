clear
docker kill rabbitmq resources-tracker resources-web resources-analyzer
docker rm rabbitmq resources-tracker resources-web resources-analyzer
clear

echo "Running the ecosystem ..."

echo "Running RabbitMQ"
docker run -d --hostname my-rabbit --name rabbitmq rabbitmq:3-management
sleep 10
echo "Visit the RabbitMQ Manager web  -->  http://localhost:15672"

echo "Running Resources Tracker"
docker build -t resources-tracker ./resources-tracker
docker run -d --link=rabbitmq --name resources-tracker resources-tracker

echo "Running Resources Analyzer"
docker build -t resources-analyzer ./resources-analyzer
docker run -d --link=rabbitmq --name resources-analyzer resources-analyzer

echo "Running Resources Web"
docker build -t resources-web ./resources-web
docker run -d --link=rabbitmq -p 8888:8888 --name resources-web resources-web

echo "Visit the web  -->  http://localhost:8888"


