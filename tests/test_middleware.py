import StringIO
import unittest

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


if __name__ == '__main__':
    unittest.main()
