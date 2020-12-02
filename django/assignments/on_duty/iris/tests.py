from untitled.tests import TestURL


class IrisTestURL(TestURL):
    SHOW_SKIPPED = True
    SHOW_VALID = True

    assert_http_status = [
        {'status': 200, 'url': '/admin/'},
        {'status': 200, 'url': '/admin/iris/'},
        {'status': 200, 'url': '/admin/iris/iris/'},
        {'status': 200, 'url': '/admin/iris/iris/add/'},
        {'status': 200, 'url': '/admin/iris/iris/1/change/', 'skip': True},
    ]
