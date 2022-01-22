## _Installation process_

The application was written in Python 3.7 so in order to make sure it runs properly it will require Python 3.7 or a higher version of Python. The requirement packages have been exported into a requirements.txt file, that allows us to install all the necessary packages with this simple command: 


```sh
pip install -r requirements.txt
```


For running the application from command line the following command should be executed:


```sh
flask run
```


Unit tests can be found and run from the app/test directory.



## _Communication_

The server is currently running on localhost port 5000, which means that the following URL-s can grant access to the server:
-	http://127.0.0.1:5000
-	http://localhost


The server has two active endpoints named append and show, these are available on the following URL-s:
-	http://127.0.0.1:5000/append
-	http://localhost/append
-	http://127.0.0.1:5000/show
-	http://localhost/show
 
 
The webserver sends and receives JSON data, I have included the exported Postman collection in the server’s main directory named TEST.postman_collection.

 

 
