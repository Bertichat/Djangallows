from typing import Any

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from app_fournitures.models import Fourniture
from app_bungalows.models import Bungalow
from app_fournitures.forms import createFournitureForm, updateFournitureForm
from django.db.models.query import QuerySet
from django.db.models import F

class createFournitureTemplate(TemplateView):
    template_name = "app_fournitures/add_fourniture_template.html"

addFournitureTemplate = createFournitureTemplate.as_view()

class createFourniture(CreateView):
    model = Fourniture
    template_name = "app_fournitures/add_fourniture.html"
    form_class = createFournitureForm

    def form_valid(self, form):
        pk_id = self.request.session["bungalow_active"]
        bungalow = Bungalow.objects.get(pk=pk_id)

        fourniture = form.save(commit=False)
        fourniture.bungalow = bungalow
        fourniture.attendu = fourniture.compte_base
        fourniture.save()

        context = {
        }

        return render(self.request, "app_bungalows/bungalows_list.html", context)

addFourniture = createFourniture.as_view()

class updateFournitureView(UpdateView):
    model = Fourniture
    template_name = "app_fournitures/update_fourniture.html"
    form_class = updateFournitureForm
    # success_url = "app_fournitures/Fourniture_diff"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["pk"] = self.kwargs["pk"]
        return context

    def form_valid(self, form):
        fourniture = form.save(commit=False)
        fourniture.save()

        # context = {} 

        return render(self.request, "app_fournitures/fourniture_diff.html")

updateFourniture = updateFournitureView.as_view()

class Fourniture_checklist_view(ListView):
    model = Fourniture
    template_name = "app_fournitures/check_list.html"
    context_object_name = "check_list"
    # paginate_by = 6

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        b_id = self.request.session["bungalow_active"]
        # queryset = ProductToCompose.objects.filter(company_id__in=companies).order_by("p_name")
        queryset = Fourniture.objects.filter(bungalow=b_id)
        return queryset
    
Fourniture_checklist = Fourniture_checklist_view.as_view()

class Fourniture_diff_view(ListView):
    model = Fourniture
    template_name = "app_fournitures/fourniture_diff.html"
    context_object_name = "diff_list"
    # paginate_by = 6

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        b_id = self.request.session["bungalow_active"]
        # queryset = ProductToCompose.objects.filter(company_id__in=companies).order_by("p_name")
        queryset = Fourniture.objects.filter(bungalow=b_id).annotate(diff=F('attendu')-F('compte_base'))
        
        return queryset
    
Fourniture_diff = Fourniture_diff_view.as_view()
