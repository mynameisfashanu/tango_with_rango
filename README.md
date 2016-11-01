# Tango with django tutorial

## Summary of chapter 1

### Creating a django project
  * django-admin startproject <project_name>

### Creating an app
  * python manage.py startapp <app_name>
  * add app name to project settings file
  * in django project urls.py file, add a mapping to the application
  * in app dir, create a urls.py file, to direct url strings to views
  * create a view to return an HttpResponse object.

### Basic django architecture
  * views take a request and return a response
  * an Http request is sent to a url
  * the url is mapped to a view
  * the view returns a response based on the request.
  * views are mapped to URLs in django.


## Summary of chapter 2.

### Create template render in view
  * create a templates directory in the django root project
  * create a sub-directory with the name of the app of where templates will be stored
  * In settings create a TEMPLATE_DIR list with the path of the templates dir, using os.path.join
  * Place the TEMPLATE_DIR variable in the DIR list, of the TEMPLATES dictionary setting.
  * render the template in the view by passing the url of the template in the render method.

### Create static files.
  * create a directory named static  in your project workspace.
  * create a STATIC_DIR varibale whose value is the path to the static directory.
  * create a STATICFILES_DIRS list which contains STATIC_DIR.
  * create a STATIC_URL variable and set it to '/static/'

### Create media static files

  * create a MEDIA_DIR variable in settings.py which contains the path to the media file.
  * assign MEDIA_ROOT to the MEDIA_DIR, this tells django where to find the media files on the local machine.
  * create a media_url varible which contains the url where the media file can be accessed, assign it to '/media/'
  * add media context process to context processes in the templates setting, to access media in templates.
