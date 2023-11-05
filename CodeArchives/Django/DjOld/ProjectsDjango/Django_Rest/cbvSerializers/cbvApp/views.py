from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins,generics,viewsets

# to add security while adding 
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BaseAuthentication]
#     permission_classes = [IsAuthenticated]


# using generics
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    

''' # using mixins
class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)    

class StudentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)  

    def delete(self,request,pk):
        return self.destroy(request,pk)                
'''

""" # using generic class based views
class StudentList(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)                
        except Student.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)        
        return Response(serializer.data)

    def put(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def delete(self,request,pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""