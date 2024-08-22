from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import formation  
from .serializers import FormationSerializer
 
from django.db.models import Avg

# Create your views here.

@api_view(['GET'])
def get_all_formations(request):

   formations = formation.objects.all()
   serializer = FormationSerializer(formations,many= True)
   print(formations)
   return Response({"formations":serializer.data})

@api_view(['GET'])
def get_by_id_formation(request,pk):
    formations = get_object_or_404(formation,id=pk)
    serializer = FormationSerializer(formations,many=False)
    print(formations)
    return Response({"formations":serializer.data})
