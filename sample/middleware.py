import StringIO

from swift.common import wsgi
from swift.common.swob import wsgify
from swift.common.utils import split_path

from PIL import Image


def create_preview(data):
    size = 150, 150
    image_obj = StringIO.StringIO(data)
    preview_obj = StringIO.StringIO()
    im = Image.open(image_obj)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(preview_obj, "JPEG")
    preview_obj.seek(0)
    return preview_obj.read()


class SummitMiddleware(object):
    def __init__(self, app, *args, **kwargs):
        self.app = app
        self.suffix = kwargs.get('suffix', '')

    @wsgify
    def __call__(self, request):
        try:
            (version, account, container, objname) = split_path(request.path_info, 4, 4, True)
        except ValueError:
            return self.app

        preview_path = '/%s/%s/%s_%s/%s' % (version, account, container, self.suffix, objname)

        if request.method == 'GET' and request.params.has_key('preview'):
            request.path_info = preview_path
       
        if request.method == 'PUT':
            preview = create_preview(request.body)
            if preview:
                sub = wsgi.make_subrequest(request.environ, path=preview_path, body=preview)
                sub.get_response(self.app)

        if request.method == 'DELETE':
            sub = wsgi.make_subrequest(request.environ, path=preview_path)
            sub.get_response(self.app)

        return self.app

def filter_factory(global_config, **local_config):
    suffix = local_config.get('suffix')
    def factory(app):
        return SummitMiddleware(app, suffix=suffix)
    return factory
