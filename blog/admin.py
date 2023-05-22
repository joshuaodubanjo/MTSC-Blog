from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Category, CustomUser, Post, Tag


admin.site.site_header  =  "MTSC Blog"  
admin.site.site_title  =  "MTSC Blog admin site"
admin.site.index_title  =  "MTSC Blog Admin"



# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'email', 'last_login']
    list_display_links = ['username', 'email']
    list_filter = ['username', 'is_staff', 'is_superuser', 'is_active']
    fieldsets = (
        ('User', {'fields': ('username', 'password'),}),
        ('Contact_Info', {'fields': ('email',),}),
        ('Personal Info', {'fields': ('first_name', 'last_name'),}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),}),
        ('Important dates', {'fields': ('last_login', 'date_joined'),}),
    )
    add_fieldsets = (
        ('Create Custom User', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name'),
            }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published']
    list_display_links = ['id', 'title']
    list_editable = ['published']
    search_fields = ['title__icontains']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published']
    list_display_links = ['id', 'title']
    list_editable = ['published']
    search_fields = ['title__icontains']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category', 'tag']
    list_display = ['id', 'title', 'author', 'category', 'created_at', 'published']
    list_select_related = ['category']
    list_display_links = ['id', 'title']
    list_editable = ['published',]
    list_filter = ['category','created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    search_fields = ['title__icontains']
    fieldsets = (
        ('Connected Models', {
            'fields': ('author', 'category', 'tag')
        }),
        ('Post Details', {
            'fields': ('title', 'slug', 'img', 'content')
        }),
        ('Important Date', {
            'fields': ('created_at', 'updated_at')
        }),
        ('Publish', {
            'fields': ('published',)
        }),
    )



admin.site.unregister(Group)