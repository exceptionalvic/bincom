from django.forms import modelformset_factory
from . models import Polling_Unit, Ward, LGA, FilterPU
from django import forms


class PUSearchForm(forms.ModelForm):
    class Meta:
        model = FilterPU
        fields = ('lga_id','pu_id','ward_id',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['maincategory'].queryset = MainCategory.objects.none()
        self.fields['ward_id'].queryset = Ward.objects.none()
        self.fields['pu_id'].queryset = Polling_Unit.objects.none()

        if 'lga_id' in self.data:
            # query by LGA for a combo dropdown
          try:
            lga_id = int(self.data.get('lga_id'))
            self.fields['ward_id'].queryset = Ward.objects.filter(lga_id=lga_id).order_by('ward_id')
          except (ValueError, TypeError):
            pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #   self.fields['category'].queryset = self.instance.maincategory.category_set.order_by('title')

        if 'ward_id' in self.data:
            # query by Ward for a combo dropdown
          try:
            ward_id = int(self.data.get('ward_id'))
            self.fields['pu_id'].queryset = Polling_Unit.objects.filter(ward_id=ward_id).order_by('pu_id')
          except (ValueError, TypeError):
            pass  # invalid input from the client; ignore and fallback to empty Locality queryset
        # elif self.instance.pk:
        #   self.fields['ward'].queryset = self.instance.category.subcategory_set.order_by('title')