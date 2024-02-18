from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serealizers import RoomSerealizer

@api_view(['GET'])
def getApi(request):
    url_s = [
        'GET api/',
       'GET api/rooms',
        'GET api/room/:id'
    ]
    return Response(url_s)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serealizer = RoomSerealizer(rooms, many=True)
    return Response(serealizer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serealizer = RoomSerealizer(room, many=False)
    return Response(serealizer.data)