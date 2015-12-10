from django.shortcuts import get_object_or_404, render
from .models import Office
from .forms import OfficeForm
from companies.models import Company, Logo


def office_list(request, company_id):
    context = {
        'company': get_object_or_404(Company, pk=company_id),
        'company_logo': Logo.latest(company_id),
        'office_list': Office.list(company_id)
    }

    return render(request, 'offices/office_list.html', context)


def office_new(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    if request.method == 'POST':
        form = OfficeForm(request.POST)

        if form.is_valid():
            office = form.save(commit=False)
            office.save()
            form.save_m2m()

            context = {
                'company': company,
                'company_logo': Logo.latest(company_id),
                'office': office
            }

            return render(request, 'offices/office_view.html', context)
    else:
        form = OfficeForm()

    context = {
        'company': company,
        'company_logo': Logo.latest(company_id),
        'form': form
    }

    return render(request, 'offices/office_edit.html', context)


def office_view(request, company_id, office_id):
    company = get_object_or_404(Company, pk=company_id)
    office = get_object_or_404(Office, pk=office_id)

    context = {
        'company': company,
        'company_logo': Logo.latest(company_id),
        'office': office
    }

    return render(request, 'offices/office_view.html', context)
