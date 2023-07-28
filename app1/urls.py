from django.urls import path
from . import views
urlpatterns=[
    path('app1/',views.htmlexample,name='htmlexample'),
    path('app1/s3',views.s3,name="s3"),
]
