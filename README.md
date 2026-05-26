## Step 1: Create Template Repo

```bash
mkdir drf-app-template
cd drf-app-template
git init
```

## Step 2: Install CookieCutter

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
pipx install cookiecutter
source ~/.bashrc
cookiecutter --version
```

## Step 3: Create Core Template Structure

### Structure
```text
drf-app-template
├── cookiecutter.json
└── {{cookiecutter.app_name}}
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── common
    │   ├── __init__.py
    │   ├── base
    │   │   ├── __init__.py
    │   │   ├── selector.py
    │   │   ├── service.py
    │   │   └── view.py
    │   └── mixins
    │       ├── __init__.py
    │       ├── soft_delete.py
    │       └── timestamp.py
    ├── models
    │   └── __init__.py
    ├── selectors
    │   ├── __init__.py
    │   └── {{cookiecutter.app_name}}_selector.py
    ├── serializers
    │   └── __init__.py
    ├── services
    │   ├── __init__.py
    │   └── {{cookiecutter.app_name}}_service.py
    ├── tasks
    │   └── __init__.py
    ├── tests
    │   └── __init__.py
    ├── urls.py
    └── views
        ├── __init__.py
        └── {{cookiecutter.app_name}}_view.py

```
### Commands for making the Structure

```bash
mkdir -p "{{cookiecutter.app_name}}"/{common/{base,mixins},models,migrations,selectors,serializers,services,tasks,tests,views} && \
touch cookiecutter.json "{{cookiecutter.app_name}}"/{__init__.py,admin.py,apps.py,urls.py,common/__init__.py,common/base/{__init__.py,selector.py,service.py,view.py},common/mixins/{__init__.py,soft_delete.py,timestamp.py},migrations/__init__.py,models/__init__.py,selectors/{__init__.py,"{{cookiecutter.app_name}}_selector.py"},serializers/__init__.py,services/{__init__.py,"{{cookiecutter.app_name}}_service.py"},tasks/__init__.py,tests/__init__.py,views/{__init__.py,"{{cookiecutter.app_name}}_view.py"}}
```

## Step 4: Apps Config (Dynamic)

### apps.py
```bash
from django.apps import AppConfig

class {{ cookiecutter.app_name|capitalize }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.{{ cookiecutter.app_name }}'
    verbose_name = '{{ cookiecutter.app_verbose_name }}'
    
```

## Step 5 : Base Classes

### common/base/service.py

```bash
from django.db import transaction

class BaseService:
    """
    Base Service with transaction handling
    """
    @staticmethod
    @transaction.atomic
    def atomic_exceute(func, *args, **kwargs):
        return func(*args, kwargs)

```

### common/base/selector.py

```bash
class BaseSelector:
    """
    Base Selector for query abstraction
    """
    pass

```

### common/base/view.py

```bash
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
```

## Step 6: Mixins ( Reusable Logic)

### common/mixins/timestamp.py

```bash
from django.db import models

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

### common/mixins/soft_delete.py

```bash
from django.db import models

class SoftDeleteMixin:
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

```

## Step 7: Service Layer Example

### services/{{cookiecutter.app_name}}_service.py

```bash
class {{ cookiecutter.app_name|capitalize }}Service:

    @staticmethod
    def create(data):
        """
        Business logic layer
        """
        pass

```

## Step 8: Selector Layer

### selectors/{{cookiecutter.app_name}}_selector.py

```bash
class {{ cookiecutter.app_name|capitalize }}Selector:

    @staticmethod
    def get_all():
        """
        Read/query layer
        """
        pass

```

## Step 9: view Layer (Thin View Pattern)

### views/{{cookiecutter.app_name}}_view.py

```bash
from rest_framework.views import APIView
from .services.{{cookiecutter.app_name}}_service import {{cookiecutter.app_name|capitalize}}Service

class {{ cookiecutter.app_name|capitalize }}View(APIView):

    def post(self, request):
        result = {{cookiecutter.app_name|capitalize}}Service.create(request.data)
        return Response(result)

```

## Step 10: urls

```bash
from django.urls import path

urlpatterns = []
```

## Step 11: Commit and Push

```bash
git add .
git commit -m "Initial DRF app cookiecutter Template"
git remote add origin https://github.com/your-username/drf-app-template.git
git branch -M main
git push -u origin main
```

## Step 12: 

```bash
cookiecutter https://github.com/your-username/drf-app-template.git --output-dir apps
```


## Some commands to know to use modular structure

```bash
python manage.py makemigrations app_name --settings=config.settings.base

python manage.py migrate app_name --settings=config.settings.base

python manage.py runserver --settings=config.settings.base

In Settings Installed apps

INSTALLED_APPS = [
    ...,

    "modules.<app_name>.apps.<app_name>Config",   # Example---> "modules.auth.apps.AuthConfig"
]
```
