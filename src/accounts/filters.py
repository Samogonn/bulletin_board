from django_filters import FilterSet
from board.models import Response


class ResponseFilter(FilterSet):
    class Meta:
        model = Response
        fields = ("announcement",)
