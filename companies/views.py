from django.shortcuts import render, get_object_or_404
from .models import Company, Logo
from .forms import CompanyForm, LogoForm
from offices.forms import OfficeForm


def company_list(request):
    context = {'company_list': Company.list}

    return render(request, 'companies/company_list.html', context)


def company_new(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            form.save_m2m()

            # Auto-create a default office
            office_form = OfficeForm()
            office = office_form.save(commit=False)
            office.company_id = company.id
            office.name = 'Default'
            office.save()

            context = {'company': company}

            return render(request, 'companies/company_view.html', context)
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
            context = {'company': company}

            return render(request, 'companies/company_view.html', context)
    else:
        form = CompanyForm(instance=company)

    context = {
        'company': company,
        'company_logo': Logo.latest(company_id),
        'form': form
    }

    return render(request, 'companies/company_edit.html', context)


def company_view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    context = {
        'company': company,
        'company_logo': Logo.latest(company_id)
    }

    return render(request, 'companies/company_view.html', context)


def logo_upload(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    if request.method == 'POST':
        form = LogoForm(request.POST, request.FILES)

        if form.is_valid():
            form = Logo(logo=request.FILES['logo'])
            form.company_id = company_id
            form.save()
            context = {'company': company}

            return render(request, 'companies/company_view.html', context)
    else:
        form = LogoForm()

    context = {
        'company': company,
        'company_logo': Logo.latest(company_id),
        'form': form
    }

    return render(request, 'companies/logo_upload.html', context)
