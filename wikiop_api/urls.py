from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'project-examples',views.ProjectExampleViewSet)
router.register(r'questions-and-answers',views.QuestionAndAnswerViewSet)
router.register(r'primary-section',views.PrimarySectionViewSet)
router.register(r'secondary-section',views.SecondarySectionViewSet)
router.register(r'fixed-section',views.FixedSectionViewSet)

urlpatterns =[
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]