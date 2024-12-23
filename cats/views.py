from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class APICat(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICatDetail(APIView):
    def get(self, request, pk):
        cat = Cat.objects.get(id=pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data)

    def put(self, request, pk):
        post = Cat.objects.get(id=pk)
        serializer = CatSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        post = Cat.objects.get(id=pk)
        serializer = CatSerializer(
            instance=post,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Cat.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'POST':
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)
