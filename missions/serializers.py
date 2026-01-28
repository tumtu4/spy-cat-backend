from rest_framework import serializers
from .models import Mission, Target
from cats.models import Cat


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "name", "country", "notes", "completed"]
        read_only_fields = ["id"]

    def update(self, instance, validated_data):
        if instance.completed:
            raise serializers.ValidationError(
                "Cannot update a completed target."
            )

        if instance.mission.completed:
            raise serializers.ValidationError(
                "Cannot update target of a completed mission."
            )

        updated_instance = super().update(instance, validated_data)

        mission = updated_instance.mission
        if all(target.completed for target in mission.targets.all()):
            mission.completed = True
            mission.save()

        return updated_instance


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)
    cat = serializers.PrimaryKeyRelatedField(
        queryset=Cat.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Mission
        fields = ["id", "cat", "completed", "targets"]
        read_only_fields = ["id"]

    def validate_targets(self, value):
        if not (1 <= len(value) <= 3):
            raise serializers.ValidationError(
                "Mission must have between 1 and 3 targets."
            )
        return value

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")
        mission = Mission.objects.create(**validated_data)

        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)

        return mission

    def update(self, instance, validated_data):

        instance.cat = validated_data.get("cat", instance.cat)
        instance.completed = validated_data.get("completed", instance.completed)
        instance.save()

        targets_data = validated_data.get("targets")
        if targets_data:
            for target_data in targets_data:
                target_id = target_data.get("id")
                if not target_id:
                    continue
                try:
                    target_instance = instance.targets.get(id=target_id)
                    serializer = TargetSerializer(
                        target_instance,
                        data=target_data,
                        partial=True  # PATCH
                    )
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                except Target.DoesNotExist:
                    continue

        if all(t.completed for t in instance.targets.all()):
            instance.completed = True
            instance.save()

        return instance