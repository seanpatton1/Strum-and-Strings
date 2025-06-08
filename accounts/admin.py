from django.contrib import admin
from .models import NewsletterSubscriber


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_status', 'date_subscribed')
    search_fields = ('email',)

    def user_status(self, obj):
        if obj.user and obj.user.email.lower() == obj.email.lower():
            return "Registered"
        return "Guest"
    user_status.short_description = "User Status"
