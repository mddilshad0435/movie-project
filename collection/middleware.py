from django.utils.deprecation import MiddlewareMixin
from django.db.models import F
from .models import CountRequests

class ReferMiddleware(MiddlewareMixin):
    def process_request(self, request):
        CountRequests.objects.filter(request='request').update(count=F('count') +1)