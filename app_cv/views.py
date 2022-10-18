from django.shortcuts import render
from django.views import View


class MainPageView(View):
    def get(self, request):
        return render(request, 'main_page.html')


class SkillsView(View):
    def get(self, request):

        return render(request, 'skills.html')


class ExperienceView(View):
    def get(self, request):
        return render(request, 'experience.html')


class ProjectsView(View):
    def get(self, request):
        # context = {
        #     'сайты': [
        #
        #     ],
        #     'боты': [
        #
        #     ],
        #     'другое': [
        #
        #     ],
        # }
        return render(request, 'projects.html')
