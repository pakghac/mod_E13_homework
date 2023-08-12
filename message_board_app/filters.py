from django_filters import FilterSet

from message_board_app.models import Response


class ResponseFilter(FilterSet):
    class Meta:
        model = Response
        fields = ['message']
