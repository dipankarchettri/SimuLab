from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Topic

# Endpoint 1: Category Page (STEM)
class CategoryPage(APIView):
    def get(self, request):
        # Get all unique categories (already stored in consistent format)
        categories = Topic.objects.values_list('category', flat=True).distinct()
        return Response({"categories": categories}, status=status.HTTP_200_OK)

# Endpoint 2: Subcategory Page (e.g., Physics, Biology, etc.)
class SubcategoryPage(APIView):
    def get(self, request, category):
        # Ensure category is capitalized for matching
        category = category.capitalize()  # Capitalize the first letter to match "Science", "Technology", etc.
        
        # Get distinct subcategories for the given category
        subcategories = Topic.objects.filter(category__iexact=category).values_list('subcategory', flat=True).distinct()
        
        if not subcategories:
            return Response({"error": f"No subcategories found for category '{category}'"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"subcategory": subcategories}, status=status.HTTP_200_OK)

# Endpoint 3: Topic Page (e.g., specific topics like "Newton's Laws of Motion" in Physics)
# TopicPage
class TopicPage(APIView):
    def get(self, request, category, subcategory):
        # Normalize category and subcategory to lowercase
        category = category.lower()
        subcategory = subcategory.lower()

        # Perform case-insensitive filtering with iexact
        topics = Topic.objects.filter(category__iexact=category, subcategory__iexact=subcategory)

        if not topics.exists():
            return Response({
                "error": f"No topics found for category '{category.capitalize()}' and subcategory '{subcategory.capitalize()}'"
            }, status=status.HTTP_404_NOT_FOUND)

        # Serialize the topic data
        topics_data = [{"id": topic.id, "name": topic.name, "description": topic.description} for topic in topics]
        return Response(topics_data, status=status.HTTP_200_OK)
