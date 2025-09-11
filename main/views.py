from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import License, LicenseCategory


def license_list(request, category_id=None):
    """
    Display a list of licenses.
    - Supports filtering by category (from URL or GET param).
    - Supports search (q).
    - Paginate results (10 per page).
    """

    licenses_qs = License.objects.select_related('category').all()
    category = None

    # Handle category from GET (dropdown) or URL
    category_param = request.GET.get("category")
    if category_param:
        category = get_object_or_404(LicenseCategory, id=category_param)
        licenses_qs = licenses_qs.filter(category=category)
    elif category_id:
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

    # Pagination
    paginator = Paginator(licenses_qs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "licenses": page_obj,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "category": category,
        "categories": LicenseCategory.objects.all(),
        "query": query,
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
