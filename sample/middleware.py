from swift.common import wsgi
from swift.common.swob import wsgify
from swift.common.utils import split_path


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
       
        return self.app

def filter_factory(global_config, **local_config):
    suffix = local_config.get('suffix')
    def factory(app):
        return SummitMiddleware(app, suffix=suffix)
    return factory
