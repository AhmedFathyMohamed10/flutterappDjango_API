from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint': '/core/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of all the notes in the API.'
        },
        {
            'Endpoint': '/core/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note in the API.'
        },
        {
            'Endpoint': '/core/create',
            'method': 'POST',
            'body': '{"title": "", "content": ""}',
            'description': 'Creates a new note in the API.'
        },
        {
            'Endpoint': '/core/id/update',
            'method': 'PUT',
            'body': '{"id": "", "title": "", "content": ""}',
            'description': 'Updates a note in the API.'
        },
        {
            'Endpoint': '/core/id/delete',
            'method': 'DELETE',
            'body': '{"id": ""}',
            'description': 'Deletes a note in the API.'
        }
    ]   
    return Response(routes)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):  # Get a note
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):  # Create a note
    # Get the data from the request
    data = request.data
    # Create a new note
    note = Note.objects.create(
        body=data['body'],
    )
    
    # Return the note
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):  # Update a note
    # Get the data from the request
    data = request.data
    # Get the note
    note = Note.objects.get(id=pk)
    # Update the note
    note.body = data['body']
    note.save()
    
    # Return the note
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):  # Delete a note
    # Get the note
    note = Note.objects.get(id=pk)
    # Delete the note
    note.delete()
    
    # Return the note
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


