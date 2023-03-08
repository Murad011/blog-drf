from rest_framework.throttling import AnonRateThrottle


class RegisterThrottle(AnonRateThrottle):
    scope = 'anon'
    # def get_cache_key(self, request, view):
    #     if request.user and request.user.is_authenticated:
    #         return None  # Only throttle unauthenticated requests.
    #
    #     return self.cache_format % {
    #         'scope': self.scope,
    #         'ident': self.get_ident(request)
    #     }

    