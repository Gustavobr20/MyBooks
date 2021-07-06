from django.urls import path

from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('add/', BookCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete'),
    path('datail/<int:pk>/', BookDetailView.as_view(), name='detail'),
]
