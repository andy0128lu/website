from django.views.generic.base import TemplateView


class ChatterBotAppView(TemplateView):
    template_name = "templates/app.html"