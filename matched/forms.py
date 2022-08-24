from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
	class Meta:
		model = Match
		fields = ['bname','gname']

	def clean_bname(self):
		bname = self.cleaned_data.get('bname')
		if not bname:
			raise forms.ValidationError('Enter B name bruh')
		return bname

	def clean_gname(self):
		gname = self.cleaned_data.get('gname')
		if not gname:
			raise forms.ValidationError('Enter G name bruh')
		return gname
