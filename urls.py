# from django.urls import path,include
# from .views import SerializerTestView


# urlpatterns = [

#     path("serializer-flow/", SerializerTestView.as_view()),
#     path("api/", include("flow.urls")),

# ] 

from django.urls import path
from .views import (
    SerializerTestView,
    last_serializer_flow,
    clear_serializer_logs
)

urlpatterns = [

    path("serializer-flow/", SerializerTestView.as_view()),

    path("serializer-flow-last/", last_serializer_flow),

    path("serializer-flow-clear/", clear_serializer_logs),

]

from .views import flow_stats_view, flow_by_id, export_flow_view

urlpatterns += [

    path("flow-stats/", flow_stats_view),

    path("flow/<str:flow_id>/", flow_by_id),

    path("flow-export/", export_flow_view),

]