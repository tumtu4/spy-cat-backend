from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Mission, Target
from .serializers import MissionSerializer, TargetSerializer
from cats.models import Cat



class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()

        if mission.cat is not None:
            return Response(
                {"error": "Cannot delete a mission assigned to a cat."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def assign_cat(self, request, pk=None):
        mission = self.get_object()
        cat_id = request.data.get("cat_id")

        if not cat_id:
            return Response(
                {"error": "cat_id is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            cat = Cat.objects.get(id=cat_id)
        except Cat.DoesNotExist:
            return Response(
                {"error": "Cat not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        if Mission.objects.filter(cat=cat).exists():
            return Response(
                {"error": "This cat already has a mission."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if mission.completed:
            return Response(
                {"error": "Cannot assign a cat to a completed mission."},
                status=status.HTTP_400_BAD_REQUEST
            )

        mission.cat = cat
        mission.save()

        return Response({"message": "Cat assigned successfully."})


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer