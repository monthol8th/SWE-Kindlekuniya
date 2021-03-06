import datetime
from haystack import indexes
from .models import Product


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    author = indexes.CharField(model_attr='author')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
