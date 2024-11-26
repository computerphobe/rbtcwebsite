# users/admin.py
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Profile, Component, IssuedComponent
from django.shortcuts import get_object_or_404 , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.db.models import F  
from django.utils import timezone


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False  # We don't want to delete profiles from here

# Custom User Admin to include Profile as inline
class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]  # Add the ProfileInline in the User Admin page

    def delete_model(self, request, obj):
        # Ensure related profile is deleted when the user is deleted
        if hasattr(obj, 'profile'):
            obj.profile.delete()
        obj.delete()

# Unregister the default User model admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register the Profile and Component models
admin.site.register(Profile)
admin.site.register(Component)

# Register IssuedComponent with custom actions
@admin.register(IssuedComponent)
class IssuedComponentAdmin(admin.ModelAdmin):
    list_display = ('component', 'student', 'quantity', 'status', 'issue_date', 'return_date')
    list_filter = ('status',)
    actions = ['approve_requests', 'reject_requests', 'mark_as_returned']

    def save_model(self, request, obj, form, change):
        """Handle quantity updates when saving model"""
        if not change:  # New issue request
            super().save_model(request, obj, form, change)
            return

        old_obj = IssuedComponent.objects.get(pk=obj.pk)
        
        with transaction.atomic():
            if old_obj.status != obj.status:
                if obj.status == 'Approved' and old_obj.status == 'Pending':
                    # When approving a request, decrease quantity
                    if obj.component.quantity >= obj.quantity:
                        Component.objects.filter(
                            id=obj.component.id,
                            quantity__gte=obj.quantity
                        ).update(quantity=F('quantity') - obj.quantity)
                        messages.success(request, f"Issued {obj.quantity} units of {obj.component.name}")
                    else:
                        obj.status = 'Pending'  # Revert status
                        messages.error(request, "Insufficient quantity available")
                
                elif obj.status == 'Returned' and old_obj.status == 'Approved':
                    # When marking as returned, increase quantity
                    Component.objects.filter(
                        id=obj.component.id
                    ).update(quantity=F('quantity') + obj.quantity)
                    obj.return_date = timezone.now()
                    messages.success(request, f"Returned {obj.quantity} units of {obj.component.name}")
            
            super().save_model(request, obj, form, change)

    @admin.action(description='Approve selected requests')
    def approve_requests(self, request, queryset):
        with transaction.atomic():
            for issue in queryset.filter(status='Pending'):
                if issue.component.quantity >= issue.quantity:
                    # Decrease quantity
                    Component.objects.filter(
                        id=issue.component.id,
                        quantity__gte=issue.quantity
                    ).update(quantity=F('quantity') - issue.quantity)
                    
                    issue.status = 'Approved'
                    issue.save()
                    
                    messages.success(
                        request,
                        f"Approved: {issue.quantity} units of {issue.component.name}"
                    )
                else:
                    messages.error(
                        request,
                        f"Insufficient quantity for {issue.component.name}"
                    )

    @admin.action(description='Mark selected as returned')
    def mark_as_returned(self, request, queryset):
        with transaction.atomic():
            returned_count = 0
            for issue in queryset.filter(status='Approved'):
                # Increase quantity
                Component.objects.filter(
                    id=issue.component.id
                ).update(quantity=F('quantity') + issue.quantity)
                
                issue.status = 'Returned'
                issue.return_date = timezone.now()
                issue.save()
                returned_count += 1
            
            if returned_count:
                messages.success(request, f"{returned_count} components marked as returned")

    @admin.action(description='Reject selected requests')
    def reject_requests(self, request, queryset):
        updated = queryset.filter(status='Pending').update(status='Rejected')
        messages.success(request, f"{updated} request(s) rejected")

