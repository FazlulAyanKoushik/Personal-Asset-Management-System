from django import forms
from .models import Land, Building, Homestead, BusinessFirm, Other

class LandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LandForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Land
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class LandSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LandSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Land
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }        

class HomesteadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HomesteadForm, self).__init__(*args, **kwargs)
        
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Homestead
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class HomesteadSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HomesteadSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Homestead
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class BuildingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BuildingForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Building
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }        

class BuildingSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BuildingSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Building
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class BusinessFirmForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BusinessFirmForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = BusinessFirm
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class BusinessFirmSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BusinessFirmSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = BusinessFirm
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class OtherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OtherForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Other
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class OtherSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OtherSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Other
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

# class LandNoteForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(LandNoteForm, self).__init__(*args, **kwargs)
#         self.fields['notefield'].widget.attrs.update({'class': 'form-control'})

#     class Meta:
#         model = NoteField
#         fields = ['notefield',]

