from django.urls import path

from apps.kubecom.views import CustomResourceDefinitionView, HomeView, JobView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("job/", JobView.as_view(), name="job"),
    path("crd/", CustomResourceDefinitionView.as_view(), name="crd"),
]
