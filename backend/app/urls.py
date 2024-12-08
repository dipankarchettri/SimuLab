from django.urls import path
from .views import CategoryPage, SubcategoryPage, TopicPage

urlpatterns = [
    # Endpoint 1: Category page (STEM)
    path('categories/', CategoryPage.as_view(), name='category-page'),

    # Endpoint 2: Subcategory page (e.g., Science -> Physics)
    path('subcategories/<str:category>/', SubcategoryPage.as_view(), name='subcategory-page'),

    # Endpoint 3: Topic page (e.g., Science -> Physics -> Newton's Laws of Motion)
    path('topics/<str:category>/<str:subcategory>/', TopicPage.as_view(), name='topic-page'),
]
