from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import License, LicenseCategory


def license_list(request, category_id=None):
    """
    Display a list of licenses.
    - If category_id is given, filter by that category.
    - Supports search (q).
    - Paginate results (10 per page).
    """

    # Get all licenses with their related category
    licenses_qs = License.objects.select_related('category').all()

    category = None
    if category_id:
        category = get_object_or_404(LicenseCategory, id=category_id)
        licenses_qs = licenses_qs.filter(category=category)

    # Search functionality
    query = request.GET.get("q", "").strip()
    if query:
        licenses_qs = licenses_qs.filter(
            Q(name__icontains=query) |
            Q(license_number__icontains=query) |
            Q(address__icontains=query)
        )

    # Order by name
    licenses_qs = licenses_qs.order_by("name")

    # Pagination (10 items per page)
    paginator = Paginator(licenses_qs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "licenses": page_obj,                  # licenses to display
        "page_obj": page_obj,                  # pagination object
        "is_paginated": page_obj.has_other_pages(),
        "category": category,                  # current category
        "categories": LicenseCategory.objects.all(),  # for sidebar/filter dropdown
        "query": query,                        # current search term
    }
    return render(request, "main/license_list.html", context)


def home(request):
    """
    Home page showing all categories and latest licenses.
    """
    categories = LicenseCategory.objects.all().order_by("name")
    latest_licenses = License.objects.select_related("category").order_by("-id")[:5]

    return render(request, "main/home.html", {
        "categories": categories,
        "latest_licenses": latest_licenses,
    })
