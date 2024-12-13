from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Engineering', 'Engineering'),
        ('Mathematics', 'Mathematics'),
    ]
    
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.SET_NULL, null=True, blank=True)  # Now ForeignKey to Subcategory

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class VisualizationConfig(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    config = models.JSONField()  # Stores global configuration for the visualization
    interactive_params = models.JSONField(default=dict)  # Stores topic-specific parameters for interactivity

    def __str__(self):
        return f"Configuration for {self.topic.name}"



