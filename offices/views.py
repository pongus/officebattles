from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone

from companies.models import Company
from offices.models import Office

# Create your views here.
def add(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    context = {
        'company': company
    }
    return render(request, 'offices/add.html', context)

def save(request, company_id):
    office_name = request.POST.get('office-name')
    office_updated = timezone.now()
    office = Office(company_id=company_id, name=office_name, updated=office_updated)
    office.save()
    return HttpResponseRedirect('/company/' + str(office.company_id) + '/office/' + str(office.id))

def list(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    office_list = Office.objects.filter(company_id=company_id).order_by('-updated')
    context = {
        'company': company,
        'office_list': office_list,
    }
    return render(request, 'offices/list.html', context)

def view(request, company_id, office_id):
    company = get_object_or_404(Company, pk=company_id)
    office = get_object_or_404(Office, pk=office_id)
    context = {
        'company': company,
        'office': office,
    }
    return render(request, 'offices/view.html', context)
