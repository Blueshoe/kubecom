from django.views import View


class JobView(View):
    "Triggers the long running task via Kubernetes Job."
    def post(self, request):
        pass


class CustomResourceDefinitionView(View):
    "Triggers the long running task via Kubernetes CRD."
    def post(self, request):
        pass

