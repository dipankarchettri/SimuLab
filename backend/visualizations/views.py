from django.http import JsonResponse

# Centralized dictionary for visualizations
VISUALIZATIONS = {
    "projectile-motion": {
        "type": "projectile-motion",
        "parameters": {
            "initialVelocity": 20,
            "angle": 45,
            "gravity": 9.8,
        },
    },
    "pendulum-motion": {
        "type": "pendulum-motion",
        "parameters": {
            "length": 10,
            "gravity": 9.8,
        },
    },
    "gravitational-force": {
        "type": "gravitational-force",
        "parameters": {
            "mass1": 5.972e24,  # Earth's mass in kg
            "mass2": 7.348e22,  # Moon's mass in kg
            "distance": 384400000,  # Distance in meters
        },
    },
    "3d-graphing": {
        "type": "3d-graphing",
        "parameters": {
            "function": "x**2 + y**2",  # Default mathematical function
            "xRange": [-10, 10],         # Range for x-axis
            "yRange": [-10, 10],         # Range for y-axis
            "resolution": 50,            # Grid resolution
        },
    },
    "bubble-sort": {
        "type": "bubble-sort",
        "parameters": {
            "array": [5, 3, 8, 4, 2],  # Default array to sort
            "steps": [],  # Steps will be populated during the sort
        },
    },
    "merge-sort": {
        "type": "merge-sort",
        "parameters": {
            "array": [5, 3, 8, 4, 2],  # Default array to sort
            "steps": [],  # Steps will be populated during the sort
        },
    },
}

def bubble_sort(arr):
    """
    A simple Bubble Sort algorithm that returns the sorted array 
    and the steps taken (in terms of swaps).
    """
    steps = []
    n = len(arr)
    
    # Perform Bubble Sort
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(arr.copy())  # Capture the array after each swap
                
    return arr, steps

def merge_sort(arr):
    """
    A simple Merge Sort algorithm that returns the sorted array 
    and the steps taken during the merge process.
    """
    steps = []

    # Merge Sort algorithm
    def merge(left, right):
        result = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        sorted_array = merge(left, right)
        steps.append(sorted_array)  # Capture the array at each merge step
        return sorted_array

    sorted_array = merge_sort_recursive(arr)
    return sorted_array, steps

def visualization_data(request, topic_name):
    """
    Handles requests for visualization data based on topic name.
    Parameters can be overridden via query string.
    """
    visualization = VISUALIZATIONS.get(topic_name)
    
    if not visualization:
        return JsonResponse(
            {"error": f"Visualization '{topic_name}' not found"}, status=404
        )
    
    # Extract default parameters and allow overrides from query parameters
    parameters = visualization["parameters"]
    query_params = request.GET

    for key in parameters.keys():
        if key in query_params:
            try:
                # Convert to appropriate type for numerical and string parameters
                if key == "function":
                    parameters[key] = query_params[key]  # Keep as string
                elif key == "array":
                    parameters[key] = list(map(int, query_params[key].split(',')))  # Convert string of numbers to list of integers
                else:
                    parameters[key] = float(query_params[key])
            except ValueError:
                return JsonResponse(
                    {"error": f"Invalid value for parameter '{key}'"}, status=400
                )
    
    # Handle Bubble Sort visualization
    if topic_name == "bubble-sort":
        array, steps = bubble_sort(parameters["array"])
        return JsonResponse(
            {
                "type": visualization["type"],
                "parameters": {
                    "sortedArray": array,
                    "steps": steps,
                },
            }
        )
    
    # Handle Merge Sort visualization
    if topic_name == "merge-sort":
        array, steps = merge_sort(parameters["array"])
        return JsonResponse(
            {
                "type": visualization["type"],
                "parameters": {
                    "sortedArray": array,
                    "steps": steps,
                },
            }
        )
    
    # Return the visualization data with updated parameters for other types
    return JsonResponse(
        {
            "type": visualization["type"],
            "parameters": parameters,
        }
    )
