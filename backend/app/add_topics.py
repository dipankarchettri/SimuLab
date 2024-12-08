from app.models import Topic

topics = [
    {
        "name": "Newton's Laws of Motion",
        "description": "Explains the relationship between a body and the forces acting on it.",
        "category": "Science",  # Assign category here
        "subcategory": "Physics",  # Assign subcategory here
    },
    {
        "name": "Simple Machines",
        "description": "Devices that make work easier, like levers, pulleys, and inclined planes.",
        "category": "Science",  # Assign category here
        "subcategory": "Physics",  # Assign subcategory here
    },
    {
        "name": "States of Matter",
        "description": "Solid, liquid, and gas states with examples and properties.",
        "category": "Science",  # Assign category here
        "subcategory": "Physics",  # Assign subcategory here
    },
]

for topic in topics:
    obj, created = Topic.objects.get_or_create(
        name=topic["name"],
        description=topic["description"],
        category=topic["category"],
        subcategory=topic["subcategory"],  # Add subcategory here
    )
    if created:
        print(f"Topic created: {obj.name}")
    else:
        print(f"Topic already exists: {obj.name}")
