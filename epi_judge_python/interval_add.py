import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook


Interval = collections.namedtuple("Interval", ("left", "right"))

"""13.7 Merging Intervals

Suppose the time during the day that a person is busy is stored as a disjoint time
intervals. If an event is added to the person's calendar, the set of busy times
may need to be updated.

In the abstract, we want a way to add an interval to a set of disjoint intervals
and represent the new set as a set of disjoint intervals. For example, if the initial set of
intervals is [-4,-1], [0,2], [3,6] [7,9], [11, 12], [14,17] and then the
added interval is [1,8], the result is [-4, -1], [0, 9], [11, 12], [14,17]

[-4,-1], [0,2], [3,6] [7,9], [11, 12], [14,17]


[[-4,-1], [0, 9], [14,17]]

[ ATTEMPTED ] 6/4
Time Complexity:
Space Complexity
"""


def add_interval(disjoint_intervals, new_interval):
    if not disjoint_intervals:
        return []
    res, i = [], 0
    # all elements before
    while (
        i < len(disjoint_intervals) and disjoint_intervals[i].right < new_interval.left
    ):
        res.append(disjoint_intervals[i])
        i += 1

    while (
        i < len(disjoint_intervals) and new_interval.right >= disjoint_intervals[i].left
    ):
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            max(new_interval.right, disjoint_intervals[i].right),
        )
        i += 1
    return res + [new_interval] + disjoint_intervals[i:]

@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals, Interval(*new_interval))
    )


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            "interval_add.tsv",
            add_interval_wrapper,
            res_printer=res_printer,
        )
    )
