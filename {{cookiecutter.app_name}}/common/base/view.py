from rest_framework.response import Response
from rest_framework import status

class BaseAPIView:
    """
    Standard API response format
    """

    def success_response(self, data=None, message="Success"):
        return Response({
            "status": "success",
            "message": message,
            "data": data
        }, status=status.HTTP_200_OK)

    def error_response(self, message="Error", code=400):
        return Response({
            "status": "error",
            "message": message,
            "data": None
        }, status=code)