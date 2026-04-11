from rest_framework.views import APIView
from .services.{{cookiecutter.app_name}}_service import {{cookiecutter.app_name|capitalize}}Service

class {{ cookiecutter.app_name|capitalize }}View(APIView):

    def post(self, request):
        result = {{cookiecutter.app_name|capitalize}}Service.create(request.data)
        return Response(result)
