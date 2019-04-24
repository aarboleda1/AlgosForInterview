from test_framework import generic_test, test_utils


def combinations(n, k):
    def directed_combinations(offset, partial_combination):
        if len(partial_combination) == k:
            res.append(partial_combination)
            return
        # Generate remaining combinations over (offset, ..., n - 1) of size
        # num_remaining
        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n - i + 1:
            directed_combinations(i + 1, partial_combination + [i])
            i += 1
    res = []
    directed_combinations(1, [])
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
