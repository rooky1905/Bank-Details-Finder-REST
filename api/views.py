import csv
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Bank, Branch #importing our Bank and Branch Models
from .serializers import BranchSerializer #To serialize the data obtained after communication.

class ImportView(View):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        csv_file = request.FILES.get('csv_file')
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        count = 0
     
        for row in reader:
            bank_name = row.get('bank_name')
            ifsc = row.get('ifsc')
            branch = row.get('branch')
            address = row.get('address')
            city = row.get('city')
            district = row.get('district')
            state = row.get('state')
            print("IFSC-- {}".format(ifsc))
            if not ifsc:
                break
            bank_object, created = Bank.objects.get_or_create(
                name=bank_name
            )
            branch_defaults = {
                'name': branch,
                'bank': bank_object,
                'address': address,
                'city': city,
                'district': district,
                'state': state    
            }
        
            branch_object, created = Branch.objects.update_or_create(
                ifsc=ifsc, defaults=branch_defaults
            )
            if created:
                print("row created{}".format(branch_defaults))

            
            count += 1
        messages.success(request, "{} rows imported.".format(count))
            
        return render(request, 'upload.html')
                

class DetailView(View):
    def get(self, request, ifsc):
        branch = Branch.objects.filter(ifsc__iexact=ifsc).first() #Showing Details of a searched IFSC Bank
        serializer = BranchSerializer(branch)
        return JsonResponse(serializer.data, safe=False) #returning the obtained results.


class ListView(View):
    def get(self, request, city, bank):
        branch_qset = Branch.objects.filter(
            city__iexact=city, bank__name__icontains=bank) #Showing list of all banks in that city containing keyword in name!
            #City name must be exact but bank name must contain keyword.
        serializer = BranchSerializer(branch_qset, many=True)
        return JsonResponse(serializer.data, safe=False)
