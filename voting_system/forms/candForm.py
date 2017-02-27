from django import forms

from voting_system.models.candidate import Candidate

class candForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('id', 'first_name', 'last_name', 'email',)