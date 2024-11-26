# views.py
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login  # Import Django's login function
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Component, IssuedComponent
from django.contrib.auth import views as auth_views
from .forms import IssueComponentForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def members(request):
    return render(request, 'team.html')

def projects(request):
    return render(request, 'blog.html')

def events(request):
    return render(request, 'service-single.html')

def achievements(request):
    return render(request, 'achievement/ACHIEVEMENT.html')

def gallery(request):
    return render(request, 'gallery/index.html')

def inventory_menu(request):
    return render(request, 'Inventory_2/menu.html')

def service_single(request):
    return (render(request, 'service-single.html'))

def team(request):
    return render(request, "team.html")

def contact(request):
    return render(request, 'contact-us.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def landing(request):
    return render(request,'landing.html')

def contact(request):
    return render(request, 'contact.html')

def event(request):
    return HttpResponse("event page")

def projects(request):
    return HttpResponse("projects page")

def gallary(request):
    return HttpResponse("gallery of robotics club")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            messages.success(request, "Registration successful.")
            return redirect('login')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def protect(request):
    return render(request, 'protect.html')

def ship(request):
    return render(request, 'shipping.html')

# portfolio ngo other
def portfolio(request):
    return render(request, 'portfolio.html')

def ngo(request):
    return render(request, 'ngo.html')

def policy(request):
    return render(request, 'policy.html')

@login_required
def user_profile(request):
    user = request.user
    pending_component = IssuedComponent.objects.filter(student=request.user, status='Pending')
    returned_components = IssuedComponent.objects.filter(student=request.user, status="Returned")
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'user_profile.html', {
        'pending_components': pending_component,
        'returned_components' : returned_components,
        'user': user,
        'profile': profile,
        'issued_components': issue_component,
    })

# Login View - using Django's built-in view
class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'  # Specify the template for the login page

# Logout View - using Django's built-in view
class CustomLogoutView(auth_views.LogoutView):
    template_name = 'logged_out.html'

@login_required
def issue_component(request, component_id):
    component = get_object_or_404(Component, id=component_id)  # Fetch the component by ID

    if request.method == "POST":
        form = IssueComponentForm(request.POST)
        if form.is_valid():
            # Create the issue request but don't commit to the database yet
            issue = form.save(commit=False)
            issue.component = component  # Assign the selected component to the issue
            issue.student = request.user  # Assign the logged-in user
            issue.status = "Pending"  # Set the status to 'Pending'
            issue.save()  # Save the issue request
            messages.success(request, "Issue request submitted successfully.")
            return redirect("components")  # Redirect to components page or any other page
        else:
            messages.error(request, f"Error submitting the issue request: {form.errors}")
    else:
        form = IssueComponentForm()

    return render(request, "inventory/issue_component_form.html", {"form": form, "component": component})
  # Redirect back if method isn't POST

@login_required
def my_issued_components(request):
    issued_components = IssuedComponent.objects.filter(student=request.user, status="Approved")
    pending_components = IssuedComponent.objects.filter(student=request.user, status='Pending')
    rejected_components = IssuedComponent.objects.filter(student=request.user, status='Rejected')
    returned_components = IssuedComponent.objects.filter(student=request.user, status="Returned")
    return render(request, 'inventory/my_issued_components.html', {'issued_components': issued_components, 'pending_components': pending_components, "rejected_components": rejected_components, 'returned_components': returned_components})



@login_required
def components(request):
    components = Component.objects.all()
    return render(request, 'inventory/components.html', {'components': components})

# Commented for non-conflict reasons
# @login_required
# @staff_member_required
# def approve_request(request, issue_id):
#     issue = get_object_or_404(IssuedComponent, id=issue_id)
    
#     if issue.status == 'Pending':
#         component = issue.component
#         if component.quantity >= issue.quantity:
#             component.quantity -= issue.quantity  # Reduce the quantity of the component
#             component.save()  # Save the updated component
#             issue.status = 'Approved'  # Update the issue request status
#             issue.save()  # Save the updated issue request
#             messages.success(request, f"Request for {component.name} has been approved.")
#         else:
#             messages.error(request, f"Insufficient stock for {component.name}. Cannot approve.")
#     else:
#         messages.error(request, "This request has already been processed.")
    
#     return redirect('manage_requests')

# @login_required
# @staff_member_required
# def reject_request(request, issue_id):
#     issue = get_object_or_404(IssuedComponent, id=issue_id)
#     if issue.status == 'Pending':
#         issue.status = 'Rejected'
#         issue.save()
#         messages.success(request, f"Request for {issue.component.name} has been rejected.")
#     else:
#         messages.error(request, "This request has already been processed.")
    
#     return redirect('manage_requests')
