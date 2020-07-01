from rest_framework import serializers
from .models import Bank, Branch

class BranchSerializer(serializers.ModelSerializer):
    bank = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Branch
        fields = (
            'id', 'ifsc', 'name', 'bank', 'address',
            'city', 'district', 'state')
        #All Field could also have been selected.