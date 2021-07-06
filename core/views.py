from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Book


class BookListView(ListView):
    template_name = 'index.html'

    model = Book
    queryset = Book.objects.all()
    context_object_name = 'books'


class BookDetailView(DetailView):
    template_name = 'details.html'

    model = Book


class BookCreateView(CreateView):
    template_name = 'cadaster.html'

    model = Book
    fields = '__all__'
    success_url = reverse_lazy('list')


class BookUpdateView(UpdateView):
    template_name = 'cadaster.html'

    model = Book
    fields = '__all__'
    success_url = reverse_lazy('list')


class BookDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Book
    success_url = reverse_lazy('list')
