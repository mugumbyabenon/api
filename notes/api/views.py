from rest_framework.decorators import  api_view
from rest_framework.response import Response
from . serializers import NoteSerializer
from .models import Note

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            "Endpoint":'/notes/',
            'method':"GET",
            'body':None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint':'/notes/id',
            'method': 'GET',
            'body':None,
            'description': 'Returns a simgle note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post '
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            "body": {'body':""},
            "description": 'Creates an existing note withdata sent in'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'DELETE',
            "body": None,
            "description": 'Deletes an existing screen'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)
@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteNote(request,pk):
    Note.objects.get(id=pk).delete
    return Response("Note was deleted")

