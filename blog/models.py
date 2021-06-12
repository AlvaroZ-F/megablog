from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField

STATUSES = (
	(0, 'Draft'),
	(1, 'Published'),
)

class Post(models.Model):
	title = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE,
		related_name='blog_posts')
	updated_on = models.DateTimeField(auto_now=True)
	content = HTMLField("Content")
	created_on = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='images', blank=True, null=True)
	status = models.IntegerField(choices=STATUSES, default=0)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', kwargs={'slug': str(self.slug)})


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE,
		related_name='comments')
	nickname = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return "Comment {} by {}".format(self.body, self.nickname)


class Contact(models.Model):
	email = models.EmailField()
	subject = models.CharField(max_length=255)
	message = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.email

	def get_absolute_url(self):
		return reverse('contact')