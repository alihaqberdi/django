from django.shortcuts import render
from .models import Women
from rest_framework import generics
from .serializers import WomenSerilizers
# Create your views here.


class WomenApiView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({"get" : list(lst)})

    def post(self, request):
        new_user = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({"post" :model_to_dict(new_user)})



# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerilizers


#demo test view
#demo test view
#demo test view
#demo test view
#demo test view
#demo test view

#demo test view

#demo test view#demo test view
#demo test view#demo test view



#demo test view#demo test view


#demo test view#demo test view

#demo test view#demo test view

#demo test view#demo test view

#demo test view#demo test view

#demo test view#demo test view


#demo test view


#demo test view#demo test view
