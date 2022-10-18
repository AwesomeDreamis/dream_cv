from django.urls import path
from .views import MainPageView, ExperienceView, SkillsView, ProjectsView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('skills/', SkillsView.as_view(), name='skills'),
    path('projects/', ProjectsView.as_view(), name='projects'),
]
