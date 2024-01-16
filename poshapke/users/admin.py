from django.contrib import admin
from .models import Users, EmailVerification


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'url_uuid',
        'created',
    )
    fields = (
        'user',
        'url_uuid',
        'created',
        'expiration'
    )
    readonly_fields = (
        'created',
    )


admin.site.register(Users)
