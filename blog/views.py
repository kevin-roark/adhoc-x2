from datetime import datetime

from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from taggit.models import Tag

from blog.models import *

class PostIndex(ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.select_related().filter(published=True).filter(timestamp__lte=datetime.now())

class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.select_related().filter(published=True)

class PostPreview(DetailView):
    model = Post
    template = "blog/post_detail.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostPreview, self).dispatch(*args, **kwargs)

class FriendList(ListView):
    model = Link
    def get_queryset(self):
        return Link.objects.all()

class ImageList(ListView):
    model = Image

class PostsByTag(PostIndex):
    def get_queryset(self):
        return Post.objects.select_related().filter(tags__slug__in=[self.kwargs['tag']]).filter(published=True).filter(timestamp__lte=datetime.now())

    def get_context_data(self, **kwargs):
        context = super(PostsByTag, self).get_context_data(**kwargs)
        tag = get_object_or_404(Tag, slug = self.kwargs['tag'])
        context['current_nav'] = tag.slug
        if tag.slug == 'breaking' or tag.slug == 'favorites' or tag.slug == 'features':
            pass
        else:
            context['title'] = 'Posts Tagged %s' % tag
        return context

class HomeView(PostIndex):
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        features = Feature.objects.filter(active=True).order_by('order')
        post_ids = []
        for f in features:
            post_ids.append(f.post_id)

        context['features'] = features
        context['recent_breaking'] = Post.objects.filter(tags__name__in=['breaking']).filter(published=True).filter(timestamp__lte=datetime.now()).exclude(id__in=post_ids)[:5]
        context['recent_features'] = Post.objects.filter(tags__name__in=['features']).filter(published=True).filter(timestamp__lte=datetime.now()).exclude(id__in=post_ids)[:5]
        context['recent_favorites'] = Post.objects.filter(tags__name__in=['favorites']).filter(published=True).filter(timestamp__lte=datetime.now()).exclude(id__in=post_ids)[:5]
        return context

class PostsByAuthor(PostIndex):
    def get_queryset(self):
        self.author = get_object_or_404(User, pk=self.kwargs['user_id'])
        return Post.objects.select_related().filter(author=self.author).filter(published=True).filter(timestamp__lte=datetime.now()).order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super(PostsByAuthor, self).get_context_data(**kwargs)
        context['title'] = 'Posts by %s' % self.author.get_full_name()
        return context

class AllEntriesFeed(Feed):
    title = "AdHoc"
    link = "/"
    description = "All Entries from AdHoc"
    description_template = "blog/feed_entry.html"

    def items(self):
        return Post.objects.filter(published=True).filter(timestamp__lte=datetime.now()).order_by('-timestamp')[:10]

    def item_title(self, item):
        return item.title

    def item_author_name(self, item):
        return item.author.get_full_name()

    def item_pubdate(self, item):
        return item.timestamp

@login_required
@csrf_exempt
def new_image(request):

    try:
        i = Image(image = request.FILES['upload'])
        i.save()

        response = "<script type='text/javascript'>"
        response += "window.parent.CKEDITOR.tools.callFunction(%s, '%s');" % (request.GET['CKEditorFuncNum'], i.medium_image.url)
        response += "</script>"

        return HttpResponse(response)
    except:
        return HttpResponse("uhh")
