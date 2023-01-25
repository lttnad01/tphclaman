from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin
from django.contrib import admin

from .models import Nghang, Product, Intro, ProductImage, News

class ProductInline(SummernoteModelAdminMixin, admin.StackedInline):
    model = Product
    extra = 1
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    

class NghangAdmin(admin.ModelAdmin):
    list_display = ['ngname', 'ngicon' ] 
    inlines = [
        ProductInline
    ]


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('prcontent',)
    list_display = ['prname','price'] 
    list_filter = ['category'] 
    inlines= [ProductImageInline,]
class ProductImageAdmin(admin.ModelAdmin):
    list_filter=['productID']

class IntroAdmin(SummernoteModelAdmin):
    summernote_fields = ('incontent',)

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('postcontent',)

# Register your models here.

admin.site.register(Nghang, NghangAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Intro, IntroAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(News, NewsAdmin)
