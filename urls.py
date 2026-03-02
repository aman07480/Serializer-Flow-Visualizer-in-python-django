from django.urls import path,include
from .views import SerializerTestView


urlpatterns = [

    path("serializer-flow/", SerializerTestView.as_view()),
    path("api/", include("flow.urls")),

]