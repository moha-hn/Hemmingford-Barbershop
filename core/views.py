from django.shortcuts import render
from staff.models import StaffMember


def home(request):
    staff = StaffMember.objects.filter(is_active=True)
    grouped = {}
    for role_value, role_label in StaffMember.Role.choices:
        members = [s for s in staff if s.role == role_value]
        if members:
            grouped[role_label] = members
    return render(request, "core/home.html", {"grouped": grouped})
