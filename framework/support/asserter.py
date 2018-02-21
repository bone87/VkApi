from framework.support.MyLogger import log_info


def assert_equal(exp1, exp2, message=None):
    try:
        assert exp1 == exp2, message
    except AssertionError:
        log_info('{error}: {message}'.format(error='AssertionError',
                                             message=message))
        raise AssertionError
