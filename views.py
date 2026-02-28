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