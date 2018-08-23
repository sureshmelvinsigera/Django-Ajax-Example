from django.conf.urls import url
from apps.bookadmin import views

urlpatterns = [
	url(r'^$', view=views.bookadmin_index_view, name='bookadmin_index_view'),
	url(r'^create/$', view=views.bookadmin_index_view, name='create_book_record'),
	url(r'^delete/(?P<id>\d+)/$', view=views.bookadmin_delete_book, name='delete_book_record'),
	url(r'^update/(?P<id>\d+)/$', view=views.bookadmin_update_book, name='update_book_record')
]
