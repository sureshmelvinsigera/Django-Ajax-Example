from django import forms
from apps.bookadmin.models import Book


class CreateBookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title', 'publisher', 'author', 'price', 'pages',)

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'publisher': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.TextInput(attrs={'class': 'form-control'}),
			'pages': forms.TextInput(attrs={'class': 'form-control'}),
		}
