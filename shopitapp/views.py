from django.shortcuts import render
from .models import *
from shopitapp.forms import SearchForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
# Create your views here.


# >>> Product Search <<<
def search_product(request):
    form = SearchForm

    results = []
    q = None

    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            vector = SearchVector('title', weight='B') + \
                SearchVector('category', weight='A')
            query = SearchQuery(q)
            # results = Product.objects.filter(title__search=q)
            # results = Product.objects.annotate(
            #     search=SearchVector('title', 'category'),).filter(search=q)
            results = Product.objects.annotate(
                rank=SearchRank(vector, query)).order_by('-rank')

    return render(request, 'shopitapp/search.html', {'form': form, 'results': results, 'q': q})

# >>> This is the product details function, when the user clicks any product,
# this function brings out the details of the clicked product, dynamically <<<


class ProductListView(ListView):
    model = Product
    template_name = 'shopitapp/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'featured_product'

    def get_queryset(self):
        return FeaturedProduct.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['allproduct'] = Product.objects.all().order_by('-created_on')[
            :4]

        return context

    paginated_by = 4


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'description', 'price', 'category', 'brand', 'condition',
              'screensize', 'operating_system', 'color', 'ram', 'storage', 'product_image1', 'product_image2', 'product_image3']

    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'description', 'price', 'category', 'brand', 'condition',
              'screensize', 'operating_system', 'color', 'ram', 'storage', 'product_image1', 'product_image2', 'product_image3']

    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.agent:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.agent:
            return True
        return False

# >>> Classview for products <<<


class PhoneListView(ListView):
    model = Product
    queryset = Product.objects.filter(category__id=1).order_by('-updated_on')
    template_name = 'shopitapp/all-phones.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'phonecategory'


class ComputerListView(ListView):
    model = Product
    queryset = Product.objects.filter(category__id=3)
    template_name = 'shopitapp/all-laptops.html'
    context_object_name = 'computercategory'


class TabletListView(ListView):
    model = Product
    queryset = Product.objects.filter(category__id=2)
    template_name = 'shopitapp/all-tablets.html'
    context_object_name = 'tabletcategory'


class TvListView(ListView):
    model = Product
    queryset = Product.objects.filter(category__id=4)
    template_name = 'shopitapp/all-tv.html'
    context_object_name = 'tvcategory'


def carousel(request):
    carols = CarouselImage.objects.all()
    return render(request, 'shopitapp/details.html', {'carols': carols})
