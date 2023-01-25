from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Nghang, Product, Intro, ProductImage, News


class HomeView(ListView):
    model = Nghang
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['nghangs'] = Nghang.objects.all()
        context['products'] = Product.objects.all()
        context['hot'] = Product.objects.filter(category='banchay') 
        context['new'] = Product.objects.filter(category='moive') 
        context['ads'] = News.objects.filter(ads='chon') 
        context['contact'] = Intro.objects.all()
        return context

class IntroView(ListView):
    model = Intro
    template_name = 'intro.html'
    def get_context_data(self, **kwargs):
        context = super(IntroView, self).get_context_data(**kwargs)
        context['myintro'] = Intro.objects.all()
        context['contact'] = Intro.objects.all()
        return context
class ProductView(DetailView):
    model = Product
    template_name = 'product-detail.html'
    def get_object(self):
        object = super(ProductView , self).get_object()
     
        return object
   
    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['myproduct'] = Product.objects.all()
        context['imgproduct'] = ProductImage.objects.all()
        context['nghangs'] = Nghang.objects.all()
        context['related_products'] = Product.objects.filter(nghang=self.get_object().nghang)
        context['contact'] = Intro.objects.all()
        return context
        
class AllProductView(ListView):
    model = Product
    template_name = 'plist.html'
    paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super(AllProductView, self).get_context_data(**kwargs)
        context['allproduct'] = Product.objects.all()
        context['nghangs'] = Nghang.objects.all()
        context['contact'] = Intro.objects.all()
        return context


class ContactView(ListView):
    model = Intro
    template_name = 'contact.html'
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact'] = Intro.objects.all()
       
        return context

class AllPostView(ListView):
    model = News
    template_name = 'news.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(AllPostView, self).get_context_data(**kwargs)
        context['allnews'] = News.objects.all()
        context['contact'] = Intro.objects.all()
        return context

class PostView(DetailView):
    model = News
    template_name = 'post.html'
    def get_object(self):
        object = super(PostView , self).get_object()
        return object
   
    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['myposts'] = News.objects.all()
        context['newposts'] =News.objects.all().order_by('-id')[:3]
        context['contact'] = Intro.objects.all()
        return context

class SearchResultsView(ListView):
    model = Product
    template_name = 'search.html'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(prname__icontains=query)
        
        else:
            object_list = self.model.objects.none()

        return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['nghangs'] = Nghang.objects.all()
        context['contact'] = Intro.objects.all()
        return context