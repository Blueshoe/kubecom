from django.urls import path

from apps.kubecom.views import CustomResourceDefinitionView, HomeView, JobView

urlpatterns = [
    path("/", HomeView),
    path("/job/", JobView.as_view()),
    path("/crd/", CustomResourceDefinitionView.as_view()),
]
