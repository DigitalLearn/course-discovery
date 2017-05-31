from rest_framework import viewsets
from rest_framework.filters import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from course_discovery.apps.api import filters, serializers
from course_discovery.apps.api.pagination import ProxiedPagination


# pylint: disable=no-member
class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    """ Organization resource. """

    filter_backends = (DjangoFilterBackend,)
    filter_class = filters.OrganizationFilter
    lookup_field = 'uuid'
    lookup_value_regex = '[0-9a-f-]+'
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OrganizationSerializer

    # Explicitly support PageNumberPagination and LimitOffsetPagination. Future
    # versions of this API should only support the system default, PageNumberPagination.
    pagination_class = ProxiedPagination

    def get_queryset(self):
        partner = self.request.site.partner
        return serializers.OrganizationSerializer.prefetch_queryset(partner=partner)

    def list(self, request, *args, **kwargs):
        """ Retrieve a list of all organizations. """
        return super(OrganizationViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """ Retrieve details for an organization. """
        return super(OrganizationViewSet, self).retrieve(request, *args, **kwargs)
