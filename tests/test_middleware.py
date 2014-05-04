import StringIO
import unittest

import mock
from swift.common.swob import Request

from sample.middleware import SummitMiddleware


class FakeApp(object):
    def __call__(self, env, start_response):
        start_response('200 OK', [])
        return ""


class TestSummitMiddleware(unittest.TestCase):
    def test_get_preview(self):
        req = Request.blank('/v1/a/c/o?preview')
        mw = SummitMiddleware(FakeApp(), suffix='preview')
        res = req.get_response(mw)
        self.assertEqual(res.environ['PATH_INFO'], '/v1/a/c_preview/o')

    @mock.patch('sample.middleware.create_preview')
    @mock.patch('swift.common.wsgi.make_subrequest')
    def test_extract_preview(self, request_mock, create_preview_mock):
        create_preview_mock.return_value = 'dummy'
        environ = {'REQUEST_METHOD': 'PUT'}
        req = Request.blank('/v1/a/c/o', environ)
        mw = SummitMiddleware(FakeApp(), suffix='preview')
        res = req.get_response(mw)
        request_mock.assert_called_with(req.environ, body='dummy', path='/v1/a/c_preview/o')

    @mock.patch('swift.common.wsgi.make_subrequest')
    def test_delete_preview(self, mocked_request):
        environ = {'REQUEST_METHOD': 'DELETE'}
        req = Request.blank('/v1/a/c/o', environ)
        mw = SummitMiddleware(FakeApp(), suffix='preview')
        res = req.get_response(mw)
        mocked_request.assert_called_with(req.environ, path='/v1/a/c_preview/o')


if __name__ == '__main__':
    unittest.main()
