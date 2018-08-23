from django import forms
from apps.bookadmin.models import BookModel


class BookModelForm(forms.ModelForm):
	class Meta:
		model = BookModel
		fields = ('title', 'publisher', 'author', 'price', 'pages',)

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'publisher': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.TextInput(attrs={'class': 'form-control'}),
			'pages': forms.TextInput(attrs={'class': 'form-control'}),
		}
