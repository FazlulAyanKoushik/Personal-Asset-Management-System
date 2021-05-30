from django import forms
from .models import Ornaments, Stocks, Share, Insurance, Cash_or_bankvalue, Vehicles, Electronics, Other_m, NoteField 

class OrnamentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrnamentsForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Ornaments
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class OrnamentsSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrnamentsSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Ornaments
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }        

class StocksForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StocksForm, self).__init__(*args, **kwargs)
        
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Stocks
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class StocksSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StocksSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Stocks
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class ShareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShareForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Share
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }        

class ShareSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShareSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Share
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class InsuranceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InsuranceForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = Insurance
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class InsuranceSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InsuranceSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Insurance
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class Cash_or_bankvalueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Cash_or_bankvalueForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Cash_or_bankvalue
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class Cash_or_bankvalueSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Cash_or_bankvalueSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Cash_or_bankvalue
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }
class VehiclesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehiclesForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Vehicles
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class VehiclesSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehiclesSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Vehicles
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }
class ElectronicsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ElectronicsForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Electronics
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class ElectronicsSuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ElectronicsSuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Electronics
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }
class Other_m_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Other_m_Form, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Other_m
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class Other_m_Form_SuperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Other_m_Form_SuperForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_and_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_acquired_and_value'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_of_money'].widget.attrs.update({'class': 'form-control'})
        self.fields['opinon'].widget.attrs.update({'class': 'form-control'})
        self.fields['signature'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_confirm'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Other_m
        fields = ['date_of_acquisition', 'owner', 'class_and_location','details',
        'how_acquired_and_value','source_of_money','opinon','signature','is_confirm']
        widgets = {
            'date_of_acquisition' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }


