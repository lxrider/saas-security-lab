from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Contact


@login_required
def contact_list(request):
    contacts = Contact.objects.filter(
        organization=request.user.organization
    )

    return render(
        request,
        "contacts/contact_list.html",
        {"contacts": contacts},
    )

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    return render(
        request,
        "contacts/contact_detail.html",
        {"contact": contact},
    )