from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth import (
    login,
    logout,
    authenticate
)

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Listing

from .forms import (
    RegisterForm,
    ListingForm
)


# =========================
# ALL LISTINGS
# =========================

def all_listings(request):

    query = request.GET.get('q')

    listings = Listing.objects.all().order_by(
        '-created_at'
    )

    if query:

        listings = listings.filter(
            title__icontains=query
        )

    context = {
        'listings': listings
    }

    return render(
        request,
        'listings/all_listings.html',
        context
    )


# =========================
# DETAILS
# =========================

def listing_detail(request, id):

    listing = get_object_or_404(
        Listing,
        id=id
    )

    context = {
        'listing': listing
    }

    return render(
        request,
        'listings/listing_detail.html',
        context
    )


# =========================
# REGISTER
# =========================

def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('all_listings')

    else:

        form = RegisterForm()

    context = {
        'form': form
    }

    return render(
        request,
        'listings/register.html',
        context
    )


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('all_listings')

        else:

            messages.error(
                request,
                'Invalid username or password'
            )

    return render(
        request,
        'listings/login.html'
    )


# =========================
# LOGOUT
# =========================

def logout_view(request):

    logout(request)

    return redirect('all_listings')


# =========================
# NEW LISTING
# =========================

@login_required
def new_listing(request):

    if request.method == 'POST':

        form = ListingForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            listing = form.save(commit=False)

            listing.created_by = request.user

            listing.save()

            return redirect('all_listings')

    else:

        form = ListingForm()

    context = {
        'form': form
    }

    return render(
        request,
        'listings/new_listing.html',
        context
    )


# =========================
# EDIT LISTING
# =========================

@login_required
def edit_listing(request, id):

    listing = get_object_or_404(
        Listing,
        id=id,
        created_by=request.user
    )

    if request.method == 'POST':

        form = ListingForm(
            request.POST,
            request.FILES,
            instance=listing
        )

        if form.is_valid():

            form.save()

            return redirect(
                'listing_detail',
                id=listing.id
            )

    else:

        form = ListingForm(instance=listing)

    context = {
        'form': form
    }

    return render(
        request,
        'listings/new_listing.html',
        context
    )


# =========================
# DELETE LISTING
# =========================

@login_required
def delete_listing(request, id):

    listing = get_object_or_404(
        Listing,
        id=id,
        created_by=request.user
    )

    listing.delete()

    return redirect('all_listings')