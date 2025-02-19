from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteForm, CategoryForm
from .models import Notes, Category

# View to display all notes and handle new note creation
def notes(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Saving note without associating with user
            return redirect('view_note')  # Redirect to the view where notes are displayed
    else:
        form = NoteForm()
    notes = Notes.objects.all().order_by('-created_at')  # Fetch all notes, ordered by creation date
    return render(request, "template/notes.html", {'form': form, 'notes': notes})

# View to search and view notes
def note_view(request):
    search_query = request.GET.get('q', '')  # Get search query from the URL (if any)
    if search_query:
        notes = Notes.objects.filter(
            note_title__icontains=search_query) | Notes.objects.filter(note__icontains=search_query)
    else:
        notes = Notes.objects.all().order_by('-created_at')  # If no search query, show all notes
    return render(request, "template/view_notes.html", {'notes': notes})

# View to edit a specific note
def edit_note(request, pk):
    note = get_object_or_404(Notes, pk=pk)  # Get note by primary key (pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()  # Save the updated note
            return redirect('view_note')  # Redirect to the view note page
    else:
        form = NoteForm(instance=note)  # Pre-populate the form with existing note data
    return render(request, "template/edit_note.html", {'form': form, 'note': note})

# View to delete a specific note
def delete_note(request, pk):
    note = get_object_or_404(Notes, pk=pk)  # Get note by primary key (pk)
    if request.method == 'POST':
        note.delete()  # Delete the note from the database
        return redirect('view_note')  # Redirect to the view notes page
    return render(request, "template/delete_note.html", {'note': note})

# View to list all categories
def category_list(request):
    categories = Category.objects.all()  # Fetch all categories
    return render(request, "template/category_list.html", {'categories': categories})

# View to add a new category
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  # Save new category to the database
            return redirect('category_list')  # Redirect to the category list page
    else:
        form = CategoryForm()  # Empty form for creating new category
    return render(request, "template/add_category.html", {'form': form})

# View to edit a specific category
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)  # Get category by primary key (pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()  # Save the updated category
            return redirect('category_list')  # Redirect to the category list page
    else:
        form = CategoryForm(instance=category)  # Pre-populate form with existing category data
    return render(request, "template/edit_category.html", {'form': form, 'category': category})

# View to delete a specific category
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)  # Get category by primary key (pk)
    if request.method == 'POST':
        category.delete()  # Delete the category from the database
        return redirect('category_list')  # Redirect to the category list page
    return render(request, "template/delete_category.html", {'category': category})


# Base view (just renders the base template)
def base_view(request):
    return render(request, 'template/base.html')  # Adjust the template path if necessary
