# IBM Watson Tone Analysis Microservice

About:
This application is a simple microservice that will accept a text string and pass it on to IBM Watson's tone analysis
service. To use this application you will need to have IBM Bluemix and a Watson Tone Analysis Service setup and
enabled. [We detail
how to create this service in this post here.](http://allengeer.com/part-3-ibm-completely-redeems-itself-building-a-tone-analysis-service-using-ibm-bluemix-and-watson/)

You will need to have the enviornment variables set with the credentials you get from the IBM Watson Bluemix interface.

We have included a Dockerfile and a requirements.txt file to create a base container that serves up this microservice.

[For a discussion on how
to use the files here specifically, view the post here.](http://allengeer.com/part-5-making-watson-microservice-using-python-docker-and-flask/)