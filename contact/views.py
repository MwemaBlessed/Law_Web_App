from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for reaching out! We'll get back to you soon.")
            return redirect('contact_page')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_page.html', {'form': form})
