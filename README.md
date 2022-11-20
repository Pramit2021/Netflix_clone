# Django Netflix Clone
This is a clone of a popular video streaming site, Netflix. It has been built using django and uses request library to handle data from TMDB API.

# Getting started with netflix
![Netflix_getstarted](https://user-images.githubusercontent.com/93142399/202911951-b706bd2a-4db5-4bc2-b13a-02d3f24eb886.JPG)

# Netflix on tv
![Netflix_tv](https://user-images.githubusercontent.com/93142399/202912685-28f7cfba-2453-492d-9677-8a72d77e9124.JPG)

# Netflix on mobile
![Netflix_mobile](https://user-images.githubusercontent.com/93142399/202912710-b870152f-c876-422f-b667-93c9473dc2f6.JPG)

# Netflix kids page
![Netflix_kid](https://user-images.githubusercontent.com/93142399/202912608-9a4a476b-141f-4ee7-afa3-fb08d9b2fc9f.JPG)

# Netflix account page
![Netflix_account](https://user-images.githubusercontent.com/93142399/202912653-d0fb6504-ebce-4b44-88a2-e72b69fc5b6b.JPG)


# Requirements
The user can perform the following functions using this clone:
1. A user can view the different movies and TV shows that are available.
2. A user can view a description of the movie and its current rating.
3. A user can watch a trailer of a movie or TV show.

# Installation/Setup instruction
The application requires following installations to operate:

-> pip

-> gunicorn

-> django

-> postgresql

-> requests

# Technology used
Python 3.7.6

# Project Setup Instruction

-> git clone repository

`https://github.com/Pramit2021/Netflix_clone`

-> Set your project directory on command prompt and type the following command for making a virtual environment

`makevirtualenv myapp1`

-> install django using following command

`pip install django`

-> Start creating project using the following command

`django-admin startproject netflixclone`

-> Set the project directory on command prompt using the command

`cd netflixclone`

-> Creat another subsidary of project using the command

`python manage.py startapp core`

-> Make migrations using the command

`python manage.py makemigrations`

-> Migrate DB using the command

`python manage.py migrate`

-> Run the application using the command

`python manage.py runserver`







