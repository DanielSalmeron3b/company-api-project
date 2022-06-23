from django.views import View
from .models import Company
from django.http import JsonResponse
from django.forms import model_to_dict

# Create your views here.

class CompanyListView(View):
    def get(self, request):
        if('name' in request.GET):
            company_list = Company.objects.filter(name__contains=request.GET['name'])
        else:
            company_list = Company.objects.all()
        return JsonResponse(list(company_list.values()), safe=False)


class CompanyDetailView(View):
    def get(self, request, pk):
        company_list = Company.objects.get(pk=pk)
        return JsonResponse(model_to_dict(company_list), safe=False)
