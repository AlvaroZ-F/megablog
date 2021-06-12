from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm, ContactForm

class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	template_name = 'content.html'
	paginate_by = 4


def detail(request, slug):
	template_name = 'detail.html'
	post = get_object_or_404(Post, slug=slug)
	comments = post.comments.filter(active=True).order_by('-created_on')
	new_comment = None

	# IF REQUEST TO POST COMMENT FROM COMMENT FORM:
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)

		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = CommentForm()

	return render(
		request,
		template_name,
		{
			'post': post,
			'comments': comments,
			'new_comment': new_comment,
			'comment_form': comment_form,
		},
	)

def about(request):
	template_name = 'about.html'
	return render(request, template_name)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'contact_success.html')

	contact_form = ContactForm()
	template_name = 'contact.html'
	context = {'contact_form': contact_form}
	return render(request, template_name, context)