from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from .forms import CustomerCreateForm
from .models import Customer
# Create your views here.


class CustomerView(View):
    model_class = Customer
    form_class = CustomerCreateForm

    def get(self, request):

        if request.resolver_match.url_name == 'create':
            form = self.form_class()
            return render(request, 'polls/create_customer.html', {'form': form})

        if request.resolver_match.url_name == 'list':

            customer_list = self.model_class.objects.order_by('name')
            context = {'customer_list': customer_list}
            return render(request, 'polls/customer_list.html', context)

    def post(self, request):
        new_form = self.form_class()
        if request.resolver_match.url_name == 'create':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'polls/create_customer.html', {'form': new_form, 'status': 'Success'})
            else:
                return render(request, 'polls/create_customer.html', {'form': form})
        else:
            return render(request, 'polls/create_customer.html', {'form': new_form})
