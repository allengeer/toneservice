# IBM BlueMix/Watson Tone Analysis Microservice

## About

This application is a simple microservice that will accept a text string and pass it on to IBM Watson's tone analysis
service. To use this application you will need to have IBM Bluemix and a Watson Tone Analysis Service setup and
enabled.

You will need to have the enviornment variables set with the credentials you get from the IBM Watson Bluemix interface.

We have included a Dockerfile and a requirements.txt file to create a base container that serves up this microservice.

## Requirements

* Docker
* Python
* Flask
* pip

## Links

[How to create a Tone Analysis service using Watson on IBM Bluemix.](http://allengeer.com/part-3-ibm-completely-redeems-itself-building-a-tone-analysis-service-using-ibm-bluemix-and-watson/)

[Walkthrough of this package and using Docker to run it](http://allengeer.com/part-5-making-watson-microservice-using-python-docker-and-flask/)

## Redis Sidecar