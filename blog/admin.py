from django.contrib import admin
from .models import Post, Comment, Contact


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'created_on', 'updated_on', 'status')
	list_filter = ('status', 'created_on')
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('nickname', 'body', 'post', 'created_on', 'active')
	list_filter = ('active', 'created_on')
	search_fields = ('name', 'email', 'body')
	actions = ['approve_comments']

	def approve_comments(self, request, query_set):
		query_set.update(active=True)

admin.site.register(Post, PostAdmin)

class ContactAdmin(admin.ModelAdmin):
	list_display = ('subject', 'email', 'created_on', 'active')
	list_filter = ('active', 'created_on')
	search_fields = ['subject',]
	actions = ['toggle_inquiries']

	def toggle_inquiries(self, request, query_set):
		query_set.update(active=False)

admin.site.register(Contact, ContactAdmin)