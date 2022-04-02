from rest_framework import status
from conferences.models import Conference
from conferences.serializers.ConferenceDetailSerializer import ConferenceDetailSerializer
from conferences.serializers.ConferenceDetailForCreatorSerializer import ConferenceDetailForCreatorSerializer
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly 


class ConferenceListView(ModelViewSet):
    ''' hello kfbeziufbzeiubzeiubciuzebb '''
    queryset= Conference.objects.all()
    permission_classes = (AllowAny,)
    permission_classes =()
    serializer_class = ConferenceDetailSerializer
    pagination_class = LimitOffsetPagination







    """serializer_class=ConferenceDetailSerializer
                def get(self,request):
                try:
                conferences=Conference.objects.all()
                except:
                return Response({},status=status.HTTP_404_NOT_FOUND)
                if not conferences is None:
                return Response(data=ConferenceDetailSerializer(conferences,many=True).data,status=status.HTTP_200_OK)
                        else:
                            return Response({},status=status.HTTP_200_OK)"""