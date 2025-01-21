from django.shortcuts import render,redirect
from .data import USERS

# Users list
def users_list(request):
    return render(request, "users/users_list.html", {"users": USERS})

# User details
def user_detail(request, id):
    user = next((user for user in USERS if user["id"] == id), None)
    return render(request, "users/user_details.html", {"user": user})

# Redirect from home input to user details
def user_detail_redirect(request):
    user_id = request.GET.get("id")
    if user_id:
        return redirect("users:user_detail", id=int(user_id))
    return redirect("users:users_list")

# Filter even users
def filter_even_users(request):
    even_users = [user for user in USERS if user["id"] % 2 == 0]
    return render(request, "users/users_list.html", {"users": even_users})
