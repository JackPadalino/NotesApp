from django.urls import path
from . import views
from .views import NoteCreateView,NoteUpdateView,NoteDeleteView,CategoryView,CategoryNotesView,CategoryCreateView,CategoryDeleteView

urlpatterns = [
    #path('',views.displaynotes,name='notes'),
    #path('',NoteListView.as_view(),name='notes'), 
    path('categories/',CategoryView,name='categories'),
    path('categories/create/',CategoryCreateView.as_view(),name='create-category'),
    path('categories/<int:pk>/details/',CategoryNotesView,name='category-notes'),
    path('categories/<int:pk>/new-note/',NoteCreateView.as_view(),name='create-note'),
    path('categories/<int:pk>/delete/',CategoryDeleteView.as_view(),name='category-delete'),  
    path('notes/<int:pk>/update/',NoteUpdateView.as_view(),name='note-update'),
    path('notes/<int:pk>/delete/',NoteDeleteView.as_view(),name='note-delete'),  
]