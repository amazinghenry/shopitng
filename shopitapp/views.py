from django.shortcuts import get_object_or_404, render
from .models import *
from shopitapp.forms import SearchForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
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
            # Product.objects.filter(title__trigram_similar=q).annotate(
            #     similar=TrigramSimilarity('title', q)).order_by('-similar')

            #standard search
            results = Product.objects.filter(title__icontains=q)
            #full text search
            # results = Product.objects.filter(title__search=q)
            #search against multiple fields
            #results=Product.objects.annotate(SearchVector('title', '$field'),).filter(search=q)
            #TrigramSimilarity & TrigramDistance
            #from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
            # results = Product.objects.annotate(TrigramSimilarity(
            #     'title', q).filter(similarity=0.8).order_by('-similarity'))

    return render(request, 'shopitapp/search.html', {'form': form, 'results': results, 'q': q})

# >>> This is the product details function, when the user clicks any product,
# this function brings out the details of the clicked product, dynamically <<<


class ProductListView(ListView):
    model = Product
    template_name = 'shopitapp/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'allproduct'
    ordering = ['-created_on']
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['featured_product'] = FeaturedProduct.objects.all()
    #     context['allproduct'] = Product.objects.all().order_by('-created_on')[
    #         :]
        context['leaderbanner'] = Leaderboard.objects.all()
        context['number'] = Product.objects.all().count()
        return context

# user's product


class UserProductListView(ListView):
    model = Product
    template_name = 'shopitapp/user_product.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'allproduct'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(agent=user).order_by('-created_on')


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'description', 'location', 'price', 'category', 'brand', 'condition',
              'screensize', 'display', 'frontcamera', 'backcamera', 'operating_system', 'color', 'ram', 'storage', 'product_image1', 'product_image2', 'product_image3']

    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'description', 'location', 'price', 'category', 'brand', 'condition',
              'screensize', 'display', 'frontcamera', 'backcamera', 'operating_system', 'color', 'ram', 'storage', 'product_image1', 'product_image2', 'product_image3']

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

    def get_context_data(self, **kwargs):
        context = super(PhoneListView, self).get_context_data(**kwargs)
        context['leaderbanner'] = Leaderboard.objects.all()

        return context


class ComputerListView(ListView):
    model = Product
    queryset = Product.objects.filter(category__id=3)
    template_name = 'shopitapp/all-computers.html'
    context_object_name = 'computercategory'

    def get_context_data(self, **kwargs):
        context = super(ComputerListView, self).get_context_data(**kwargs)
        context['leaderbanner'] = Leaderboard.objects.all()

        return context


class TabletListView(ListView):
    model = Product
    queryset = Product.objects.filter(category__id=2)
    template_name = 'shopitapp/all-tablets.html'
    context_object_name = 'tabletcategory'

    def get_context_data(self, **kwargs):
        context = super(TabletListView, self).get_context_data(**kwargs)
        context['leaderbanner'] = Leaderboard.objects.all()

        return context


class TvListView(ListView):
    model = Product
    queryset = Product.objects.filter(category__id=4)
    template_name = 'shopitapp/all-tv.html'
    context_object_name = 'tvcategory'

    def get_context_data(self, **kwargs):
        context = super(TvListView, self).get_context_data(**kwargs)
        context['leaderbanner'] = Leaderboard.objects.all()

        return context
