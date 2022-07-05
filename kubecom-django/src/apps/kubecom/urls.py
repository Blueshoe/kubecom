from django.urls import path

from apps.kubecom.views import HomeView, JobView, CustomResourceDefinitionView

urlpatterns = [
    path("/", HomeView),
    path("/job/", JobView.as_view()),
    path("/crd/", CustomResourceDefinitionView.as_view()),
]
