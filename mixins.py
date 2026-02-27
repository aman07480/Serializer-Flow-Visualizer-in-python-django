from .flow_logger import log_step


class SerializerFlowMixin:

    def __init__(self, *args, **kwargs):

        log_step("Serializer Initialized")

        super().__init__(*args, **kwargs)


    def is_valid(self, *args, **kwargs):

        log_step("Validation Started")

        result = super().is_valid(*args, **kwargs)

        log_step("Validation Finished")

        return result


    def create(self, validated_data):

        log_step("Create Method Called", validated_data)

        return super().create(validated_data)


    def update(self, instance, validated_data):

        log_step("Update Method Called", validated_data)

        return super().update(instance, validated_data)


    def to_representation(self, instance):

        log_step("Serialization Started")

        data = super().to_representation(instance)

        log_step("Serialization Finished", data)

        return data