from django.shortcuts import get_object_or_404, render

from .models import Company

# Create your views here.
def index(request):
    return render(request, 'companies/index.html')

def list(request):
    company_list = Company.objects.order_by('-created')[:5]
    context = {'company_list': company_list}
    return render(request, 'companies/list.html', context)

def view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'companies/view.html', {'company': company})
