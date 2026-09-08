from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

def studentview(request,pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(data=serializer.data)
    return HttpResponse(json_data)

def studentListview(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    json_data = JSONRenderer().render(data=serializer.data)
    return HttpResponse(json_data)

@csrf_exempt
def createStudentView(request):
    if request.method == 'POST':
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        parser_data = JSONParser().parse(stream_data)
        serializer = StudentSerializer(data = parser_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Save Successfully'}
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_res,content_type='application/json')
        error = serializer.errors()
        return HttpResponse(error,content_type = 'application/json')
        
# Create your views here.
