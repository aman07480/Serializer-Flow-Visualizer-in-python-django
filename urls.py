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

from .views import (
    flow_dashboard_view,
    flow_replay_view,
    flow_ai_analysis_view,
    flow_timeline_view,
    flow_html_view
)

urlpatterns += [

    path("flow-dashboard/", flow_dashboard_view),
    path("flow-replay/", flow_replay_view),
    path("flow-ai-analysis/", flow_ai_analysis_view),
    path("flow-timeline/", flow_timeline_view),
    path("flow-html/", flow_html_view),

]