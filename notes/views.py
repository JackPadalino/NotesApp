from django.shortcuts import render
from .models import Note,Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import CategoryCreateForm,NoteCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

'''
class NoteListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(author=user)
        return notes
    template_name = 'notes/mynotes.html'
    context_object_name = 'notes'
'''

@login_required
def CategoryView(request):
    user = request.user
    categories = Category.objects.filter(author=user)
    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.author = user
            category.save()
            return redirect('categories')
    else:
        form = CategoryCreateForm()
    context = {
        'title':'New category',
        'categories':categories,
        'form':form,
    }
    return render(request,'notes/categories.html',context)

class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = Category
    template_name = 'notes/create-category.html'
    form_class=CategoryCreateForm

    def form_valid(self,form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

def CategoryNotesView(request,pk):
    user = request.user
    category = Category.objects.get(pk=pk)
    notes = Note.objects.filter(category=category)
    context = {
        'title':f'{category.title}',
        'notes':notes,
        'category':category
    }
    return render(request,'notes/category-notes.html',context)

class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Note
    template_name = 'notes/create-note.html'
    form_class=NoteCreateForm

    def form_valid(self,form):
        form.instance.category_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

class NoteDetailsView(LoginRequiredMixin,DetailView):
    model = Note
    template_name ='notes/note-details.html'

class NoteUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Note
    fields = ['title','content']
    template_name ='notes/note-update.html'
    #success_url = reverse_lazy('category-notes')

    # this form_valid function sets the author of the updated post to be the current logged in user
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # this test_func function checks to make that the current logged in user is the author of a post before allowing to update
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class NoteDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('categories')
    
    # this test_func function checks to make that the current logged in user is the author of a post before allowing to update
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class CategoryDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Category
    template_name = 'notes/category_confirm_delete.html'
    success_url = reverse_lazy('categories')
    
    # this test_func function checks to make that the current logged in user is the author of a post before allowing to update
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False