from django.db import models

class Topic(models.Model):
    CATEGORY_CHOICES = [
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Engineering', 'Engineering'),
        ('Mathematics', 'Mathematics'),
    ]
    
    SCIENCE_SUBCATEGORY_CHOICES = [
        ('Physics', 'Physics'),
        ('Biology', 'Biology'),
        ('Chemistry', 'Chemistry'),
        ('Earth Science', 'Earth Science'),
    ]
    
    TECHNOLOGY_SUBCATEGORY_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('Web Development', 'Web Development'),
        ('Software Engineering', 'Software Engineering'),
    ]
    
    # Add more subcategory choices for other categories as needed.

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=50, blank=True, null=True)  # Subcategory field

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class VisualizationConfig(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    config = models.JSONField()  # Stores global configuration for the visualization
    interactive_params = models.JSONField(default=dict)  # Stores topic-specific parameters for interactivity

    def __str__(self):
        return f"Configuration for {self.topic.name}"