from django.shortcuts import render, get_object_or_404
from .models import StaffMember


def staff_detail(request, pk):
    member = get_object_or_404(StaffMember, pk=pk, is_active=True)
    return render(request, "staff/detail.html", {"member": member})
