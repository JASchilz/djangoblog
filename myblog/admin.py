from django.contrib import admin
from myblog.models import Post, Category

class PostCatInline(admin.TabularInline):
    model = Category.posts.through
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'published_date')
    inlines = [PostCatInline,]
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
