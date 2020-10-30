# Django Channels and Websocket Notes

### (super)user 
* password: none
### (super)user2
* password:
	Es91110291!
## Reccomended Start
 Follow the reccomended start in the site below:
* https://github.com/codingforentrepreneurs/Rapid-ChatXChannels
    
## Installing REDIS
	 sudo apt install redis-tools
    
## Youtube Video Steps
	pip install channels==2.1.2
    
![](image-kgvbhowv.png)
* result after command

### We don't have an ASGI application set 
 ![](image-kgvbo7n6.png)
 
### This is after including channels in "apps"
 
 ![](image-kgvbpvzz.png)
 
 * django channels has taken over runserver command 
 * Set your ASGI application
 	* Create your routing for ASGI
 	* Create 'routing.py'
 	* Follow the rest of this portion

## Creating your first consumer


* Resolve runserver issue


![](image-kgwe7uts.png)

https://stackoverflow.com/questions/53494337/django-channels-websocket-bridge-error-when-trying-to-connect-web-socket

![](image-kgwekkq1.png)

https://stackoverflow.com/questions/53468845/how-to-locate-websocketbridge-js-in-django-using-channels-websocket



Success, connection to the websocket 


![](image-kgwgklvv.png)


Used console to interact with the websocket:
*	document.ws.send("hello")


