from django.shortcuts import render
from django.views.generic.base import TemplateView

tags = ["обучение", "программирование", "python", "oop"]
users = ['Тимон', 'Санек', 'Лёня']

class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context["who"] = user.get_username() if user.is_authenticated else "Гость"
        return context
    
class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"tags": tags, "users": users})

        return context