# graphic-drawer Django application
This is simple application for Django wit Rest Framework, AngularJS &amp; Highcharts which draws a graphic from .xls file.

All you need to do is to upload an .xls file with two columns: x & y. Then press "Построить график" button.

For use:
<li>1) This app for django 1.9, the latest version of django-rest-framework and python 3.x

<li>2) Install from requirements using **pip**
<li>3) start a new app in your django project and copy this files inside the created folder with replacing default files. It doesn't matter how your app will be named. It was just "loader" for me.
<li>4) Put **'rest_framework'** and **'your_app_name'** to django-settings **INSTALLED_APPS** list.
<li>5) Include urls from this app to your main urls.py file by:
```python
 from django.conf.urls import include
 from your_app_name import urls as your_app_urls

 urlpatterns = [
    #your existing urls
    url(r'^any_url/', include(your_app_urls))
 ]
```
<li>6) Do your database migrated with something like: 
```
python manage.py makemigrations
```
and then:
```
python manage.py migrate
```
