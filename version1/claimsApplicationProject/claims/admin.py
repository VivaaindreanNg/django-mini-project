from django.contrib import admin
from .models import ClaimsModel
from django.db.models.query import QuerySet


# Changes on model's update status
@admin.action(description="Update status to Accepted")
def updateClaimStatus(modeladmin, request, queryset):
    for claim in queryset:
        claim.updateStatus = "Accepted"
        claim.save()


class ClaimsAdmin(admin.ModelAdmin):
    claim = ClaimsModel()
    fields = ['updateStatus']
    actions = [updateClaimStatus]


admin.site.register(ClaimsModel, ClaimsAdmin)
