from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model


def catalog(request):
    return render(request, 'catalog/catalog.html')



class ServiceRequestView(LoginRequiredMixin, View):
    form_class = ServiceRequestForm
    template_name = 'catalog/service_request_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('catalog:thank_you')
        else:
            return render(request, self.template_name, {'form': form})
        
        
        
class ThanksForRequestView(View):
    def get(self, request):
        return render(request, 'catalog/thanks_for_request.html')
