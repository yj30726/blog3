from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlog
from .models import Blog, Comment
from .forms import BlogCommentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def blogMain(request):
    blogs = Blog.objects.all()

    return render(request, 'blogMain.html', {'blogs': blogs})

def createBlog(request):
    if request.method == 'POST':
        form = CreateBlog(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogMain')
        else:
            return redirect('index')
    else:
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})
  # form = CreateBlog()
#    return render(request, 'createBlog.html', {'form': form})
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog_id=blog_id)

    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)

        if comment_form.is_valid():
            content = comment_form.cleaned_data['comment_textfield']

            print(content)

            return redirect('blogMain')
        else:
            return redirect('blogMain')

    else:
        comment_form = BlogCommentForm()

        context = {
            'blog_detail': blog_detail,
            'comments': comments,
            'comment_form': comment_form
        }

        return render(request, 'detail.html', context)