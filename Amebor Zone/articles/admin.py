from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
from .models import Article, Comment

# Inline class for managing comments on an article
class CommentInline(admin.TabularInline):  
    model = Comment
    extra = 0

# Admin class for managing articles
class ArticleAdmin(admin.ModelAdmin):  
    inlines = [
        CommentInline,
    ]

# Admin class for managing CustomUser (User model with followers)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('followers', 'following')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('followers', 'following')}),
    )

# Register the models with the admin site
admin.site.register(Article, ArticleAdmin) 
admin.site.register(Comment) 
#admin.site.register(CustomUser, CustomUserAdmin)
