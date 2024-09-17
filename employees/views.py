from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def employee_list(request):
    contacts = Contact.objects.all()
    return render(request, 'employees/employee_list.html', {'contacts': contacts})

def employee_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'employees/employee_detail.html', {'contact': contact})

def employee_add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = ContactForm()
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'contact': contact})
