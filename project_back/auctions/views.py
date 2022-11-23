from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_list_or_404

from .serializers import MyPageserializer,AuctionCreateSerializer
from .models import Painting, Auction


#유화 리스트페이지
class MyPageView(APIView):
    def get(self, request):
        painting = get_list_or_404(Painting, author=request.user.id)
        if painting.author == request.user:
            serializer = MyPageserializer(painting, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("접근 권한 없음", status=status.HTTP_403_FORBIDDEN)

#경매 생성
class AuctionListView(APIView):
    def post(self,request,painting_id):
        serializer = AuctionCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user,painting_id=painting_id)
            return Response(serializer.data,status=status.HTTP_200_OK)       
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#경매 좋아요
class LikeView(APIView):
    def post(self,request,auction_id):
        auction = get_object_or_404(Auction,id=auction_id)
        if request.user in auction.auction_like.all():
            auction.auction_like.remove(request.user)
            return Response('좋아요 취소되었습니다.',status=status.HTTP_200_OK)
        else:
            auction.auction_like.add(request.user)
            return Response('좋아요 되었습니다.',status=status.HTTP_200_OK)