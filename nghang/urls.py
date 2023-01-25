from django.urls import path
from .views import HomeView, IntroView, AllProductView, ProductView, ContactView, AllPostView, PostView, SearchResultsView
app_name='nghang'
urlpatterns = [
    path('', HomeView.as_view() , name='homepage'),
    path('intro/', IntroView.as_view() , name='intropage'),
    path('all-product/', AllProductView.as_view() , name='all-product'),
    path('<slug:slug>', ProductView.as_view() , name='product-detail'),
    path('contact/', ContactView.as_view() , name='contact-page'),
    path('all-post/', AllPostView.as_view() , name='all-post'),
    path('all-post/<slug:slug>', PostView.as_view() , name='post-detail'),
    path('search/', SearchResultsView.as_view(), name="search-results"),
]
