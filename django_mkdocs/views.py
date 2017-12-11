from django.http import HttpResponse, Http404, HttpResponseRedirect
import app_settings
from django.views.static import serve
import mimetypes
from django.contrib.auth.decorators import login_required


DOCUMENTATION_ROOT = 'index.html'


@login_required
def documentation(request, path):
    if path == '':
        path = DOCUMENTATION_ROOT
    if not app_settings.DOCUMENTATION_ACCESS_FUNCTION(request.user):
        return HttpResponseRedirect(app_settings.LOGIN_REDIRECT_URL)
    if not app_settings.DOCUMENTATION_XSENDFILE:
        return serve(
            request,
            path,
            app_settings.DOCUMENTATION_HTML_ROOT)
    mimetype, encoding = mimetypes.guess_type(path)
    response = HttpResponse(content_type=mimetype)

    response['Content-Encoding'] = encoding
    response['Content-Disposition'] = ''
    response['X-Sendfile'] = "".join([app_settings.DOCUMENTATION_HTML_ROOT,
                                      path])
    return response
