# Reactive Architecture
A proof of concept where we try to build a reactive architecture using Python, RabbitMQ and AngularJS.

The PoC is composed of three projects or modules. The behaviour of the entire system tries to be asynchronous. No data is requested between the modules and getting the information as soon as it is ready:

- [**resources-tracker**] [resources-tracker]: It tracks the resources of the machine and it will send the measures through RabbitMQ.
- [**resources-analyzer**] [resources-analyzer]: It analyzes the received measures, analyze them and send the outcomes through RabbitMQ.
- [**resources-web**] [resources-web]: It shows the analyzed measures which are received through RabbitMQ.

[resources-tracker]:<https://github.com/mendrugory/reactive-architecture-python/tree/master/resources-tracker>
[resources-analyzer]:<https://github.com/mendrugory/reactive-architecture-python/tree/master/resources-analyzer>
[resources-web]:<https://github.com/mendrugory/reactive-architecture-python/tree/master/resources-web>

