class SummitMiddleware(object):
    def __init__(self, app, *args, **kwargs):
        self.app = app

    def __call__(self, env, start_response):
        response = self.app(env, start_response)
        if env.get('PATH_INFO') == '/echo':
            length = int(env.get('CONTENT_LENGTH') or 0)
            return env.get('wsgi.input').read(length)
        return response

def filter_factory(global_config, **local_config):
    def factory(app):
        return SummitMiddleware(app)
    return factory
