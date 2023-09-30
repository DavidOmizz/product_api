from django.urls import path
from . views import Products,AddListCategory,Tags,TagView, product_detail,tags_detail,TagViewset


urlpatterns = [
    path('', Products, name='home'),
    path('<int:id>',product_detail, name = 'product_detail'),
    path('category', AddListCategory, name = 'category'),
    path('tag',TagView.as_view(), name = 'tag'),
    # path('taggs',TagViewset, name = 'taggs'),
    path('tag/<int:id>',tags_detail, name = 'tag_detail'),
]
