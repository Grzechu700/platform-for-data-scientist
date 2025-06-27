from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Dataset, Analysis, Visualization, Researcher


class ResearcherCreationForm(UserCreationForm):
    """Formularz do tworzenia nowych użytkowników typu Researcher.
    Rozszerza standardowy formularz UserCreationForm Django,
    dodając pola specyficzne dla modelu Researcher.
    """
    bio = forms.CharField(
        label='Biografia',
        widget=forms.Textarea(attrs={'placeholder': 'Krótka biografia'}),
        required=False
    )
    institution = forms.CharField(
        label='Instytucja',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa instytucji'}),
        required=False
    )

    class Meta:
        model = Researcher
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'institution', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.bio = self.cleaned_data['bio']
        user.institution = self.cleaned_data['institution']
        if commit:
            user.save()
        return user


class DatasetForm(forms.ModelForm):
    """
    Formularz DatasetForm będzie formularzem modelowym (ModelForm),
    który automatycznie generuje pola formularza na podstawie pól modelu Dataset.
    """
    class Meta:
        model = Dataset
        fields = ["name", "description"]


class AnalysisForm(forms.ModelForm):
    """
    Formularz AnalysisForm będzie formularzem modelowym (ModelForm) dla modelu Analysis.
    """
    class Meta:
        model = Analysis
        fields = ["name", "description", "dataset", "researcher"]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nazwa analizy'}),
            'description': forms.Textarea(attrs={'placeholder': 'Opis analizy'}),
        }


class VisualizationForm(forms.ModelForm):
    """
    Formularz VisualizationForm będzie formularzem modelowym (ModelForm) dla modelu Visualization.
    """
    class Meta:
        model = Visualization
        fields = ["name", "description", "visualization_type", "dataset", "researcher"]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nazwa wizualizacji'}),
            'description': forms.Textarea(attrs={'placeholder': 'Opis wizualizacji'}),
            'visualization_type': forms.TextInput(attrs={'placeholder': 'Typ wizualizacji'}),
        }
