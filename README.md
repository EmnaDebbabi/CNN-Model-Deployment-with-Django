# CNN-Model-Deployment-with-Django

## Tools

We require specialized tools for each type of project before we can build it. In our case to deploy
the CNN model, the first part of the project, We have used python 3.7 as
programming language also tensorflow 2.2 and anaconda as a framework that manages the packages.
Finally, for the deployment part we chose Django as a framework with sqlite3 as a database.

![image](https://user-images.githubusercontent.com/47029962/210519950-253289db-b0fd-4e5b-bcb8-9e9d251957a0.png)


## Deploying steps

We will outline the phases involved in our deployment process, which will use our model to forecast
the desired results:
<ul>
<li> Our models are trained, and then saved locally so we may use them for prediction. </li>
<li> Our prediction code will be integrated into the Django framework to produce web services for
our application later. </li>
</ul>

## Deploying process

Now that the framework possesses the desired characteristics. We need to develop a backend server
to create webservices for our framework.

<ul>
<li> The outer CNN/ root directory: is just a container for our project. </li>
<li> manage.py: A command-line utility that lets us interact with this Django project in various
ways. </li>
<li> The inner CNN/ directory: is the actual Python package for our project. Its name is the
Python package name we will need to use to import anything inside it: for example: urls.py. </li>
<li> CNN/__init__.py: An empty file that tells Python that this directory should be considered
a Python package. </li>
<li> CNN/settings.py: Settings/configuration for the Django project that we will use to add our
app name which is "predict". </li>
<li> CNN/urls.py: The URL declarations for this Django project; a "table of contents" of our
Django-powered site. </li>
<li> CNN/wsgi.py: An entry-point for WSGI-compatible web servers to serve our project. </li>
<li> The inner predict/ directory: is the actual Django app. Each application written in Django
consists of a Python package, that follows a certain convention. </li>
<li> The inner predict/data/: contains the pretrained embeddings used for the model prediction. </li>
<li> The inner predict/templates/: contains the template used for the project. </li>
<li> predict/models.py file: define database models for the object-relational mapping layer (ORM)
provided by Django. </li>
<li> predict/views.py file: to insert the code for getting the prediction and return a JSON re-
sponse. </li>
<li> predict/utils.py file: contains the code for the words embeddings part. </li>
<li> cnn_model_1.h5: contains the saved model on h5 extension ready to predict. </li>
</ul>
![image](https://user-images.githubusercontent.com/47029962/210530729-8dca68ec-5467-4d93-85ef-c69aecf7fa85.png)

First we use the POST method for the prediction calls. We have sentence as mandatory input and
the position1 and position2 of the entities are optional for more precision. Then after getting the
causality relation prediction for a given input, we will stock it into SQLite database. Finally, we will
display the list of the gathered data within the database.

![image](https://user-images.githubusercontent.com/47029962/210530996-1562256b-e6a6-4ce2-912c-794f32fd88ed.png)


![image](https://user-images.githubusercontent.com/47029962/210531071-45354250-fd4a-4393-938b-ea3cce9160a3.png)

![image](https://user-images.githubusercontent.com/47029962/210531154-046b46c6-990c-4b24-959a-0d83b41f769c.png)

![image](https://user-images.githubusercontent.com/47029962/210531210-f21eacee-fffd-45c6-91e6-e0b4aa45dac0.png)

![image](https://user-images.githubusercontent.com/47029962/210531265-e17f9a63-72aa-4639-b8aa-42696dcb445f.png)





