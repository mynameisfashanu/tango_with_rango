Tango with django tutorial

### Summary of chapter 1

## Creating a django project
  * django-admin startproject <project_name>

## Creating an app
  * python manage.py startapp <app_name>
  * add app name to project settings file
  * in django project urls.py file, add a mapping to the application
  * in app dir, create a urls.py file, to direct url strings to views
  * create a view to return an HttpResponse object.

## Basic django architecture
  * views take a request and return a response
  * an Http request is sent to a url
  * the url is mapped to a view
  * the view returns a response based on the request.
  * views are mapped to URLs in django.
