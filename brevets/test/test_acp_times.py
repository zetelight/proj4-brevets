"""
Nose tests for acp_times.py

We cannot test for randomness here (no effective oracle),
but we can test that the elements in the returned string
are correct.
"""

from acp_times import *
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

base_time = arrow.get('2017-01-01T00:00:00.000-07:00').isoformat()

def test_open_time():
    # interval for [0, 200]
    print("Begin the test of open time for 200km")
    assert  open_time(0, 200, base_time) == '2017-01-01T00:00:00-07:00'
    assert  open_time(100, 200, base_time) == '2017-01-01T02:56:00-07:00'
    assert  open_time(150, 200, base_time) == '2017-01-01T04:25:00-07:00'
    assert  open_time(200, 200, base_time) == '2017-01-01T05:53:00-07:00'
    assert  open_time(220, 200, base_time) == '2017-01-01T05:53:00-07:00'
    print("Finish the test of open time for 200km")
    print("----")

    # interval for [0, 400]
    print("Begin the test of open time for 400km")
    assert  open_time(200, 400, base_time) == '2017-01-01T05:53:00-07:00'
    assert  open_time(300, 400, base_time) == '2017-01-01T09:00:00-07:00'
    assert  open_time(400, 400, base_time) == '2017-01-01T12:08:00-07:00'
    assert  open_time(440, 400, base_time) == '2017-01-01T12:08:00-07:00'
    print("Finish the test of open time for 400km")
    print("----")

    # interval for [0, 600]
    print("Begin the test of open time for 600km")
    assert  open_time(200, 600, base_time) == '2017-01-01T05:53:00-07:00'
    assert  open_time(400, 600, base_time) == '2017-01-01T12:08:00-07:00'
    assert  open_time(600, 600, base_time) == '2017-01-01T18:48:00-07:00'
    assert  open_time(660, 600, base_time) == '2017-01-01T18:48:00-07:00'
    print("Finish the test of open time for 600km")
    print("----")

    # interval for [0, 1000]
    print("Begin the test of open time for 1000km")
    assert  open_time(300, 1000, base_time) == '2017-01-01T09:00:00-07:00'
    assert  open_time(500, 1000, base_time) == '2017-01-01T15:28:00-07:00'
    assert  open_time(1000, 1000, base_time) == '2017-01-02T09:05:00-07:00'
    assert  open_time(1100, 1000, base_time) == '2017-01-02T09:05:00-07:00'
    print("Finish the test of open time for 1000km")
    print("----")

def test_close_time():
    # interval for [0, 200]
    print("Begin the test of close time for 200km")
    assert  close_time(0, 200, base_time) == '2017-01-01T01:00:00-07:00'
    assert  close_time(100, 200, base_time) == '2017-01-01T06:40:00-07:00'
    assert  close_time(150, 200, base_time) == '2017-01-01T010:00:00-07:00'
    assert  close_time(200, 200, base_time) == '2017-01-01T13:30:00-07:00'
    assert  close_time(220, 200, base_time) == '2017-01-01T13:30:00-07:00'
    print("Finish the test of close time for 200km")
    print("----")

    # interval for [0, 400]
    print("Begin the test of close time for 400km")
    assert  close_time(200, 400, base_time) == '2017-01-01T013:20:00-07:00'
    assert  close_time(300, 400, base_time) == '2017-01-01T20:00:00-07:00'
    assert  close_time(400, 400, base_time) == '2017-01-02T03:00:00-07:00'
    assert  close_time(440, 400, base_time) == '2017-01-021T03:00:00-07:00'
    print("Finish the test of close time for 400km")
    print("----")

    # interval for [0, 600]
    print("Begin the test of close time for 600km")
    assert  close_time(200, 600, base_time) == '2017-01-01T13:20:00-07:00'
    assert  close_time(400, 600, base_time) == '2017-01-02T02:40:00-07:00'
    assert  close_time(600, 600, base_time) == '2017-01-02T16:00:00-07:00'
    assert  close_time(660, 600, base_time) == '2017-01-02T16:00:00-07:00'
    print("Finish the test of close time for 600km")
    print("----")

    # interval for [0, 1000]
    print("Begin the test of close time for 1000km")
    assert  close_time(300, 1000, base_time) == '2017-01-01T20:00:00-07:00'
    assert  close_time(500, 1000, base_time) == '2017-01-02T09:20:00-07:00'
    assert  close_time(1000, 1000, base_time) == '2017-01-04T03:00:00-07:00'
    assert  close_time(1100, 1000, base_time) == '2017-01-04T03:00:00-07:00'
    print("Finish the test of close time for 1000km")
    print("----")