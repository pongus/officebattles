from django.shortcuts import get_object_or_404, render
from companies.models import Company
from offices.models import Office
from .forms import OfficeForm


def office_new(request, company_id):
    if request.method == 'POST':
        form = OfficeForm(request.POST)

        if form.is_valid():
            office = form.save(commit=False)
            office.save()
            form.save_m2m()

            return render(request, 'offices/office_view.html', {'office': office})
    else:
        form = OfficeForm()

    return render(request, 'offices/office_edit.html', {'form': form})


def list(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    office_list = Office.objects.filter(company_id=company_id).order_by('-updated')

    context = {
        'company': company,
        'office_list': office_list,
    }

    return render(request, 'offices/list.html', context)


def office_view(request, company_id, office_id):
    company = get_object_or_404(Company, pk=company_id)
    office = get_object_or_404(Office, pk=office_id)

    context = {
        'company': company,
        'office': office,
    }

    return render(request, 'offices/office_view.html', context)
