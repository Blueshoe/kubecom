import os
from datetime import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException

from django.views.generic import TemplateView, View


class JobView(View):
    "Triggers the long running task via Kubernetes Job."
    def post(self, request):
        pass


class CustomResourceDefinitionView(View):
    """Triggers the long running task via Kubernetes CRD."""

    def post(self, request):

        namespace = os.getenv("POD_NAMESPACE", "kubecom")
        try:
            config.load_incluster_config()
            app = client.CustomObjectsApi()
        except ConfigException:
            app = None
        try:
            app.create_namespaced_custom_object(
                namespace=namespace,
                body={
                    "apiVersion": "blueshoe.de/v1",
                    "kind": "LongRunningJob",
                    "metadata": {
                        "name": "lo-ru-jo-" + datetime.now().strftime("%Y%m%d%H%M%S"),
                        "namespace": namespace,
                    },
                    "spec": {
                        "args": ["1", "2", "3"],
                        "kwargs": {
                            "foo": "bar"
                        }
                    },
                },
                group="blueshoe.de",
                plural="longrunningjobs",
                version="v1",
            )
            messages.add_message(
                request,
                messages.INFO,
                "The long running job has been triggered. " 
                "This takes a while to complete.",
            )
        except Exception:
            messages.add_message(
                request,
                messages.ERROR,
                "An error occured requesting a longrunning job. "
                "Please consult the log.",
            )

        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/admin/"))


class HomeView(TemplateView):
    template = "kubecom/home.html"
