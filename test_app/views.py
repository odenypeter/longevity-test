from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from test_app.helper import MergeDataHelper
from test_app.models import SampleModel
from test_app.serializers import SampleModelSerializer


class SampleModelViewSet(viewsets.ModelViewSet):
    queryset = SampleModel.objects.all()
    serializer_class = SampleModelSerializer
    permission_classes = (AllowAny,)

    @action(methods=['POST'], detail=False)
    def merge_data(self, request):
        merge_data_helper = MergeDataHelper(request.data)

        merged_data = merge_data_helper.merge_data()
        # save data here
        model_map = [SampleModel(**item) for item in merged_data]
        data = SampleModel.objects.bulk_create(model_map)

        response_data = self.get_serializer(data, many=True).data

        return Response(
            response_data,
            status=status.HTTP_201_CREATED
        )

