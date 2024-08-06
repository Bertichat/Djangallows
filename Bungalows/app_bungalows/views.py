from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.db.models import F
from django.db.models.query import QuerySet

from app_bungalows.models import Bungalow
from app_bungalows.forms import BungalowCopyForm
from app_fournitures.models import Fourniture




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

class Bungalow_copy_setItems_view(FormView):
    form_class = BungalowCopyForm
    template_name = "app_bungalows/bungalows_copyItems.html"
    # paginate_by = 6

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     b_id = self.request.session["bungalow_active"]
    #     Fourniture.objects.filter(bungalow=b_id).update(attendu=F('compte_base'))
    #     context = super().get_context_data(**kwargs)
    #     return context
    # def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
    #     return super().post(request, *args, **kwargs)

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs =  super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form: Any) -> HttpResponse:
        b_dest = self.request.session["bungalow_active"]
        print(b_dest)

        Fourniture.objects.filter(bungalow = b_dest).delete()

        b_to_copy = Bungalow.objects.get(name = form.cleaned_data["name"])
        print(b_to_copy.name)

        f_to_copy = Fourniture.objects.filter(bungalow_id = b_to_copy.id)
        # queryset = Fourniture.objects.filter(bungalow_id = 2)

        # queryset.update(bungalow_id=self.request.session["bungalow_active"])
        # queryset.update(bungalow_id=1)

        for f_id in f_to_copy.values_list("id", flat=True):
            temp = Fourniture.objects.get(id = f_id)
            temp.bungalow_id = b_dest
            temp.pk = None
            temp.save()
        # queryset.save()
        return render(self.request, "app_bungalows/bungalows_maj_info.html")

BungalowsCopySetItems = Bungalow_copy_setItems_view.as_view()
