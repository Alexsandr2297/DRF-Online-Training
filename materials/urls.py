from django.urls import path

from rest_framework.routers import SimpleRouter

from materials.views import LessonViewSet, CourseCreateAPIView, CourseListApiView, CourseRetrieveAPIView, CourseUpdateAPIView, CourseDestroyAPIView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", LessonViewSet)


urlpatterns = [
    path("courses/", CourseListApiView.as_view(), name="courses_list"),
    path("courses/<int:pk>", CourseRetrieveAPIView.as_view(), name="courses_retrive"),
    path("courses/create/", CourseCreateAPIView.as_view(), name="courses_create"),
    path("courses/<int:pk>/delete/", CourseDestroyAPIView.as_view(), name="courses_delete"),
    path("courses/<int:pk>/update/", CourseUpdateAPIView.as_view(), name="courses_update")

]
urlpatterns += router.urls