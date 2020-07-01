from django.contrib import admin
from .models import Bank, Branch


@admin.register(Bank) #decorators for regsitering model
class BankAdmin(admin.ModelAdmin):
    search_fields = ('name',) #Search by Name
    list_filter = ('name', ) #Filter the results by Name

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'bank', 'city', 'district',
    )  #Listing Display
    search_fields = ('name', 'city') #Search for a Bank using Name and city
    list_filter = ('bank',) #Filter the results by bank