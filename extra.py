from app.models import Category, Subcategory, Topic


category = Category.objects.get(name='Science')  # or use .get() or .create()
subcategory = Subcategory.objects.create(name="Chemistry", category=category)

# Now, create the Topic and save it to the database
topic = Topic.objects.create(
    name='Periodic Table',
    description='A 3D periodic table where each element shows its atomic structure, orbitals, or bonding properties.',
    category=category,
    subcategory=subcategory
)


