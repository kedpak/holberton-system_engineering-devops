# Load Balancer
A load balancer is a device which acts as a reverse proxy and distributes network or application traffic across multiple servers. Increases capacity and reliablity of appliations.
# Description
This project will set up a second web server web-02, which increases redundancy in our system. It allows the system to be more reliable by doubling the number of web servers. web-02 will be identical to web-01. 

# Tasks
* Configure Nginx so that its HTTP response contains a custom header
* The name of the custom HTTP header must be X-Served-By
* The value of the custom HTTP header must be the hostname of the server Nginx is running on
* Using the Bash scripts you built for your web server, write 0-custom_http_response-header so that it configures a brand new Ubuntu machine to the requirements asked in this task
