import StringIO
import unittest

from webob import Request

from sample.middleware import SummitMiddleware


class FakeApp(object):
    def __call__(self, env, start_response):
        start_response('200 OK', [])
        return ""


class TestSummitMiddleware(unittest.TestCase):
    def test_simple_request(self):
        environ={'REQUEST_METHOD': 'PUT'}
        req = Request.blank('/echo', environ, body='Hello World')
        mw = SummitMiddleware(FakeApp(), suffix='/echo')
        response = req.get_response(mw)
        self.assertEqual("Hello World", response.body)


if __name__ == '__main__':
    unittest.main()
