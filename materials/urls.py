from django.urls import path

from rest_framework.routers import SimpleRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonListApiView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)


urlpatterns = [
    path("courses/", LessonListApiView.as_view(), name="courses_list"),
    path("courses/<int:pk>", LessonRetrieveAPIView.as_view(), name="courses_retrive"),
    path("courses/create/", LessonCreateAPIView.as_view(), name="courses_create"),
    path("courses/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="courses_delete"),
    path("courses/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="courses_update")

]
urlpatterns += router.urls