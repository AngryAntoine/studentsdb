from .settings import PORTAL_URL


def students_processor(request):
    return {'PORTAL_URL': PORTAL_URL}
