# from rest_framework.response import Response
# from rest_framework.decorators import api_view 
# from .serializers import RoomSerializer,Room

# response = [
#     "GET api/",
#     "GET api/home",
#     "GET api/room/:id",
# ]

# @api_view(['GET'])
# def home(request):
#     return Response(response)

# @api_view(["GET"])
# def rooms(request):
#     rooms = Room.objects.all()
#     serializer = RoomSerializer(rooms,many=True)
#     return Response(serializer.data)