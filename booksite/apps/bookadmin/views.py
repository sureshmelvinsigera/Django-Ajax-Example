from django.shortcuts import render
from apps.bookadmin.models import BookModel
from apps.bookadmin.form import BookModelForm
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.
def bookadmin_index_view(request):
	if request.method == 'POST':
		if request.is_ajax():
			createbookform = BookModelForm(request.POST)
			if createbookform.is_valid():
				createbookform.cleaned_data
				createbookform.save()
				latest = BookModel.objects.latest('id').id
				book_object = model_to_dict(BookModel.objects.get(pk=latest))
				return JsonResponse({'error': False, 'data': book_object})
			else:
				print(createbookform.errors)
				return JsonResponse({'error': True, 'data': createbookform.errors})
		else:
			error = {
				'message': 'Error, must be an Ajax call.'
			}
			return JsonResponse(error, content_type="application/json")
	else:
		createbookform = BookModelForm()
		all_books_object = BookModel.objects.all()
		data = {
			'createbookform_html': createbookform,
			'books': all_books_object,
		}
		return render(request, template_name='index.html', context=data)


def bookadmin_update_book(request, id):
	if request.method == 'POST' and request.is_ajax():
		try:
			book_object = model_to_dict(BookModel.objects.get(pk=id))
			return JsonResponse({'error': False, 'data': book_object})
		except BookModel.DoesNotExist:
			return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})
	return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})


def bookadmin_delete_book(request, id):
	if request.method == 'POST' and request.is_ajax():
		try:
			book_object = BookModel.objects.get(pk=id)
			book_object.delete()
			return JsonResponse({'status': 'Success', 'message': 'Recoard has been deleted.'})
		except BookModel.DoesNotExist:
			return JsonResponse({'status': 'Fail', 'message': 'Recoard does not exist.'})
	return JsonResponse({'status': 'Fail', 'message': 'Error, must be an Ajax call.'})
