from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from app_bungalows.models import Bungalow
from app_fournitures.models import Fourniture
from django.db.models.query import QuerySet
from django.db.models import F


class Bungalow_list_view(ListView):
    model = Bungalow
    template_name = "app_bungalows/bungalows_list.html"
    context_object_name = "bungalows_list"
    # paginate_by = 6

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        # queryset = ProductToCompose.objects.filter(company_id__in=companies).order_by("p_name")
        queryset = Bungalow.objects.all()
        return queryset
BungalowsList = Bungalow_list_view.as_view()

class Bungalow_choice_view(TemplateView):
    template_name = "app_bungalows/bungalows_choice.html"
    # paginate_by = 6

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.GET.get("pk"):
            self.request.session["bungalow_active"] = self.request.GET.get("pk")
        return context

BungalowsChoice = Bungalow_choice_view.as_view()

class Bungalow_maj_view(TemplateView):
    template_name = "app_bungalows/bungalows_maj.html"
    # paginate_by = 6

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

BungalowsMaj = Bungalow_maj_view.as_view()

class Bungalow_maj_setItems_view(TemplateView):
    template_name = "app_bungalows/bungalows_maj_info.html"
    # paginate_by = 6

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        b_id = self.request.session["bungalow_active"]
        Fourniture.objects.filter(bungalow=b_id).update(attendu=F('compte_base'))
        context = super().get_context_data(**kwargs)
        return context

BungalowsMajSetItems = Bungalow_maj_setItems_view.as_view()
