from swift.common.swob import HTTPOk, wsgify


class SummitMiddleware(object):
    def __init__(self, app, *args, **kwargs):
        self.app = app
        self.suffix = kwargs.get('suffix', '')

    @wsgify
    def __call__(self, request):
        if request.path_info == self.suffix:
            return HTTPOk(request=request, body=request.body)
        return self.app

def filter_factory(global_config, **local_config):
    suffix = local_config.get('suffix')
    def factory(app):
        return SummitMiddleware(app, suffix=suffix)
    return factory
