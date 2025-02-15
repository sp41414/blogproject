from django.contrib import admin
from .models import Post 

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'status')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author', 'status')
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author=request.user)
    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.author != request.user and not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)
    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.author != request.user and not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)
admin.site.register(Post, PostAdmin)
