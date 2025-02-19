from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NoteForm, CategoryForm
from .models import Notes, Category

def base_view(request):
    return render(request, 'template/base.html')

def notes(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_note')
    else:
        form = NoteForm()
    notes = Notes.objects.all().order_by('-created_at')
    return render(request, "template/notes.html", {'form': form, 'notes': notes})

def note_view(request):
    search_query = request.GET.get('q', '')
    if search_query:
        notes = Notes.objects.filter(
            note_title__icontains=search_query) | Notes.objects.filter(note__icontains=search_query)
    else:
        notes = Notes.objects.all().order_by('-created_at')
    return render(request, "template/view_notes.html", {'notes': notes})

def edit_note(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('view_note')
    else:
        form = NoteForm(instance=note)
    return render(request, "template/edit_note.html", {'form': form, 'note': note})

def delete_note(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('view_note')
    return render(request, "template/delete_note.html", {'note': note})

def category_list(request):
    categories = Category.objects.all()
    return render(request, "template/category_list.html", {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, "template/add_category.html", {'form': form})

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, "template/edit_category.html", {'form': form})

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, "template/delete_category.html", {'category': category})