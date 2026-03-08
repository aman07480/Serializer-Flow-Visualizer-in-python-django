from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProductSerializer
from .flow_logger import get_logs, clear_logs


class SerializerTestView(APIView):

    def post(self, request):

        clear_logs()

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():

            data = serializer.save()

            return Response({
                "result": data,
                "flow": get_logs()
            })

        return Response(serializer.errors)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .flow_logger import get_logs, total_steps


@api_view(["GET"])
def last_serializer_flow(request):

    return Response({
        "total_steps": total_steps(),
        "flow": get_logs()
    })

from .flow_logger import log_step

class SerializerTestView(APIView):

    def post(self, request):

        clear_logs()

        log_step("Request Received", request.data)

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():

            data = serializer.save()

            return Response({
                "result": data,
                "flow": get_logs()
            })

        return Response(serializer.errors)