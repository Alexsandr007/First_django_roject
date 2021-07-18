from django.shortcuts import render, get_object_or_404 ,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.db.models import Count
from taggit.models import Tag
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm


def post_list(request, tag_slug=None):
  object_list = Post.published.all()
  tag = None

  if tag_slug:
    tag = get_object_or_404(Tag, slug=tag_slug)
    object_list = object_list.filter(tags__in=[tag])


  object_list = Post.objects.all()
  paginator = Paginator(object_list, 3) # По 3 статьи на каждой странице.
  page_number = request.GET.get('page')
  page_obj=paginator.get_page(page_number)



  return render(request,
    'post/blog.html',
    {'page_obj': page_obj,
    'object_list': object_list,
    'tag': tag})

def post_detail(request, year, month, day, post):
  post = get_object_or_404(Post, slug=post,
    status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day)
  tags = Tag.objects.all()

  post_tags_ids = post.tags.values_list('id', flat=True)
  similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
  similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

    # List of active comments for this post
  comments = post.comments.filter(active=True)[::-1]

  new_comment = None
  right_block=Post.published.order_by('-pk')[:3]



  if request.method == 'POST':
        # A comment was posted
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
      # Create Comment object but don't save to database yet
      new_comment = comment_form.save(commit=False)
      # Assign the current post to the comment
      new_comment.post = post
      # Save the comment to the database
      new_comment.save()

      comment_form = CommentForm()
      return redirect(post)
  else:
    comment_form = CommentForm()


  context={'post': post,
  'comments': comments,
  'new_comment': new_comment,
  'comment_form':comment_form,
  'similar_posts': similar_posts,
  'right_block':right_block,
  'tags':tags}


  return render(request,'post/blog-single.html',context)