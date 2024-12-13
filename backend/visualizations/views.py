from django.http import JsonResponse

def visualization_data(request, topic_name):
    visualizations = {
        "projectile-motion": {
            "type": "projectile-motion",
            "parameters": {"initialVelocity": 20, "angle": 45, "gravity": 9.8},
        },
        "pendulum-motion": {
            "type": "pendulum-motion",
            "parameters": {"length": 10, "gravity": 9.8},
        },
    }

    data = visualizations.get(topic_name)
    if data:
        return JsonResponse(data)
    return JsonResponse({"error": "Visualization not found"}, status=404)
