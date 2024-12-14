from django.urls import path
from .views import CategoryPage, SubcategoryPage, TopicPage

urlpatterns = [
    path('categories/', CategoryPage.as_view(), name='category_page'),
    path('categories/<str:category_name>/subcategories/', SubcategoryPage.as_view(), name='subcategory_page'),
    path('categories/<str:category_name>/subcategories/<str:subcategory_name>/topics/', TopicPage.as_view(), name='topic_page'),
    # Add a new URL pattern for topics directly if needed
]

