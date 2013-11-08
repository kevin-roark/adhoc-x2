from haystack.indexes import *
from haystack import site
from blog.models import Post


class PostIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    published = BooleanField(model_attr='published')
    timestamp = DateTimeField(model_attr='timestamp')

    def index_queryset(self):
        """
        Called when the entire search index is updated.
        aka objects returned can be searched
        """
        return Post.objects.filter(published=True)

site.register(Post, PostIndex)