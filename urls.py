from django.urls import path
from .views import SerializerTestView


urlpatterns = [

    path("serializer-flow/", SerializerTestView.as_view()),
    path("api/", include("flow.urls")),

]