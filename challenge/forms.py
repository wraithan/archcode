from django.forms import ModelForm
from archcode.challenge.models import Solution

class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['challenge','language','user','source']
