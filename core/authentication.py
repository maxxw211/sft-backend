from django.utils.translation import gettext_lazy as _
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from rest_framework.authentication import TokenAuthentication


def get_authorization_header(request):
    auth = request.headers.get("token", b"")
    if isinstance(auth, str):
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request)

        if not auth:
            return None

        try:
            token = auth.decode()
        except UnicodeError:
            msg = _(
                "Invalid token header. Token string should not contain invalid characters."
            )
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)
