from rest_framework import mixins, viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from rest_framework.routers import DefaultRouter

class CourantViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
  ):

  permission_classes = [IsAuthenticated]
  serializer_class = CourantSerializer

  queryset = Courant.objects.all()

  @detail_route(methods=["post"])
  def post(self, request, pk):
    """ Create courant entry
        ---
        serializer: CourantEntrySerializer
    """
    serializer = CourantEntrySerializer(data=request.data)
    if serializer.is_valid():
      entry = serializer.instance
      entry.user = request.profiel
      entry.courant_id = pk
      entry.date_created = datetime.now()
      entry.date_modified = datetime.now()
      entry.save()
      return Response(CourantEntrySerializer(instance=entry))

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

router = DefaultRouter()
router.register('courant', CourantViewSet, base_name='courant')
urls = router.urls
