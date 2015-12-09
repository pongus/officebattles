from django.shortcuts import render, get_object_or_404
from .models import Company, Logo
from .forms import CompanyForm, LogoForm


def company_list(request):
    company_list = Company.objects.order_by('-updated')
    context = {'company_list': company_list}

    return render(request, 'companies/company_list.html', context)


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
    company_logo = Logo.objects.filter(company_id=company_id).order_by('-updated').first()

    if (request.method == 'POST'):
        form = CompanyForm(request.POST, instance=company)

        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            form.save_m2m()
            return render(request, 'companies/company_view.html', {'company': company})
    else:
        form = CompanyForm(instance=company)

    context = {
        'company': company,
        'company_logo': company_logo,
        'form': form
    }

    return render(request, 'companies/company_edit.html', context)


def company_view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    company_logo = Logo.objects.filter(company_id=company_id).order_by('-updated').first()

    context = {
        'company': company,
        'company_logo': company_logo
    }

    return render(request, 'companies/company_view.html', context)


def logo_upload(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    company_logo = Logo.objects.filter(company_id=company_id).order_by('-updated').first()

    if request.method == 'POST':
        form = LogoForm(request.POST, request.FILES)

        if form.is_valid():
            form = Logo(logo=request.FILES['logo'])
            form.company_id = company_id
            form.save()
            return render(request, 'companies/company_view.html', {'company': company})
    else:
        form = LogoForm()

    context = {
        'company': company,
        'company_logo': company_logo,
        'form': form
    }

    return render(request, 'companies/logo_upload.html', context)
