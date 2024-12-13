from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Subcategory, Topic

# Endpoint 1: Category Page (STEM)
class CategoryPage(APIView):
    def get(self, request):
        # Get all categories (get all Category objects and return their names)
        categories = Category.objects.values_list('name', flat=True)
        return Response({"categories": categories}, status=status.HTTP_200_OK)

# Endpoint 2: Subcategory Page (e.g., Physics, Biology, etc.)
class SubcategoryPage(APIView):
    def get(self, request, category_name):
        # Ensure category_name is capitalized for matching
        category_name = category_name.capitalize()  # Capitalize the first letter to match
        
        # Get category object for the given category name
        category = Category.objects.filter(name=category_name).first()

        if not category:
            return Response({"error": f"Category '{category_name}' not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Get distinct subcategories for the given category
        subcategories = Subcategory.objects.filter(category=category).values_list('name', flat=True)

        if not subcategories:
            return Response({"error": f"No subcategories found for category '{category_name}'"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"subcategories": subcategories}, status=status.HTTP_200_OK)

# Endpoint 3: Topic Page (e.g., specific topics like "Newton's Laws of Motion" in Physics)
class TopicPage(APIView):
    def get(self, request, category_name, subcategory_name):
        # Normalize category_name and subcategory_name to lowercase
        category_name = category_name.capitalize()
        subcategory_name = subcategory_name.capitalize()

        # Get category and subcategory objects
        category = Category.objects.filter(name=category_name).first()
        subcategory = Subcategory.objects.filter(name=subcategory_name, category=category).first()

        if not category:
            return Response({"error": f"Category '{category_name}' not found"}, status=status.HTTP_404_NOT_FOUND)

        if not subcategory:
            return Response({"error": f"Subcategory '{subcategory_name}' not found in category '{category_name}'"}, status=status.HTTP_404_NOT_FOUND)
        
        # Get topics for the given category and subcategory
        topics = Topic.objects.filter(category=category, subcategory=subcategory)

        if not topics.exists():
            return Response({
                "error": f"No topics found for category '{category_name}' and subcategory '{subcategory_name}'"
            }, status=status.HTTP_404_NOT_FOUND)

        # Serialize the topic data
        topics_data = [{"id": topic.id, "name": topic.name, "description": topic.description} for topic in topics]
        return Response(topics_data, status=status.HTTP_200_OK)
