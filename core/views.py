from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import SensorData
from core.serializers import SensorDataSerializer


@api_view(['GET', 'POST'])
def sensor_data_view(request):
    if request.method == 'POST':
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        # Fetch the latest sensor data
        latest_data = SensorData.objects.latest('timestamp')  # Assumes you have a timestamp field
        serializer = SensorDataSerializer(latest_data)
        return Response(serializer.data)


door_status = "closed"  # Initialize the door status


def dashboard_view(request):
    # Pass any initial data if necessary
    context = {
        "initial_door_status": "closed"  # Example context data if you want to display the initial status
    }
    return render(request, "dashboard.html", context)


doorbell_pressed = False  # Flag to track doorbell press


@csrf_exempt
def doorbell_notification(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', None)

        if message == "Someone is at the door":
            return JsonResponse({"notification": "Security: Someone is at the door"}, status=200)
        elif message == "Unidentified person attempted entry":
            return JsonResponse({"notification": "Security: Unauthorized access attempt"}, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def door_status_view(request):
    global door_status

    if request.method == 'POST':
        data = json.loads(request.body)
        status = data.get('status', None)

        if status == "open":
            door_status = "open"
            return JsonResponse({"notification": "Security: Welcome home!"}, status=200)
        elif status == "closed":
            door_status = "closed"
            return JsonResponse({"notification": "Door closed"}, status=200)

    return JsonResponse({"status": door_status}, status=200)


# Store the light status
light_status = {
    "indoor": "off",
    "outdoor": "off"
}


@csrf_exempt
def light_control_view(request):
    global light_status

    if request.method == 'POST':
        data = json.loads(request.body)

        indoor_status = data.get('indoor', None)
        outdoor_status = data.get('outdoor', None)

        if indoor_status in ["on", "off"]:
            light_status["indoor"] = indoor_status
            print(f"Indoor light turned {indoor_status.upper()}.")

        if outdoor_status in ["on", "off"]:
            light_status["outdoor"] = outdoor_status
            print(f"Outdoor light turned {outdoor_status.upper()}.")

        return JsonResponse({"response": "Light status updated", "current_status": light_status}, status=200)

    # GET request to return the current status of the lights
    return JsonResponse({"current_status": light_status}, status=200)


motion_sensor_active = False  # Global variable to track motion sensor state

# @csrf_exempt
'''def motion_sensor_view(request):
    global motion_sensor_active

    if request.method == 'POST':
        data = json.loads(request.body)
        state = data.get('state', None)

        if state in ["on", "off"]:
            motion_sensor_active = (state == "on")
            print(f"Motion sensor turned {state.upper()}.")
            return JsonResponse({"response": f"Motion sensor turned {state}", "active": motion_sensor_active},
                                status=200)
        else:
            return JsonResponse({"error": "Invalid state"}, status=400)

    elif request.method == 'GET':
        # Return current motion sensor status
        return JsonResponse({"active": motion_sensor_active}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=400)'''
