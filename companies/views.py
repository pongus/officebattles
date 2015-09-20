from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Company

# Create your views here.
def index(request):
    return render(request, 'companies/index.html')

def list(request):
    company_list = Company.objects.order_by('-created')
    context = {'company_list': company_list}
    return render(request, 'companies/list.html', context)

def add(request):
    return render(request, 'companies/add.html')

def save(request):
    company_name = request.POST.get('company-name')
    company_updated = timezone.now()
    company = Company(name=company_name, updated=company_updated)
    company.save()
    return HttpResponseRedirect('/company/' + str(company.id))

def view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'companies/view.html', {'company': company})
