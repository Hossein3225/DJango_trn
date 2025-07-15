from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def Homepage(request):
    context = {
        "inventory_list": ["chiz1", "chiz2", "chiz3"],
        "greeting": "thank you for visiting",
    }
    return render(request, "home.html", context)


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 main street"
        context["phone_number"] = "555-555-555"
        return context
