from django.forms import TextInput, Textarea, ModelForm, MultipleChoiceField, CheckboxSelectMultiple
from .models import Partner, Menu

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = (
            "name",
            "contact",
            "address",
            "description",
            "category",
        )
        FOOD_TYPE = (
            ("한식", "ko"),
            ("중식", "cn"),
            ("일식", "jp"),
        )
        category = MultipleChoiceField(
            required=False,
            widget=CheckboxSelectMultiple,
            choices=FOOD_TYPE,
        )
        widgets = {
            "name": TextInput(attrs={"class":"form-control"}),
            "contact": TextInput(attrs={"class":"form-control"}),
            "address": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
        }
        fields = [
            "name",
            "contact",
            "address",
            "description",
            "category",
        ]

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = (
            "image",
            "name",
            "price",
        )
        widgets = {
            # "image": TextInput(attrs={"class":"form-control"}),
            "name": TextInput(attrs={"class":"form-control"}),
            "price": TextInput(attrs={"class":"form-control"}),
        }
