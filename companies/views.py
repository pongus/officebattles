from django.shortcuts import render, get_object_or_404
from .forms import CompanyForm

from companies.models import Company

# Create your views here.
def index(request):
    return render(request, 'companies/index.html')


def list(request):
    company_list = Company.objects.order_by('-updated')
    context = {'company_list': company_list}
    return render(request, 'companies/list.html', context)


def company_new(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            form.save_m2m()

            return render(request, 'companies/company_view.html', {'company': company})
    else:
        form = CompanyForm()

    return render(request, 'companies/company_edit.html', {'form': form})


def company_edit(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    if (request.method == 'POST'):
        form = CompanyForm(request.POST, instance=company)

        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            form.save_m2m()

            return render(request, 'companies/company_view.html', {'company': company})
    else:
        form = CompanyForm(instance=company)

    return render(request, 'companies/company_edit.html', {'form': form})


def company_view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'companies/company_view.html', {'company': company})

