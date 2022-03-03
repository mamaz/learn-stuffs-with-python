"""
union operation
"""


def union(set1: list, set2: list) -> list:
    result = []

    for s1 in set1:
        for s2 in set2:
            if s1 == s2:
                result.append(s1)

    return result


if __name__ == "__main__":
    cases = [
        {"s1": [1, 2, 3], "s2": [3, 4, 5], "ans": [3]},
        {"s1": [1], "s2": [3], "ans": []},
        {"s1": [], "s2": [], "ans": []},
    ]

    for case in cases:
        print(case)
        assert union(case["s1"], case["s2"]) == case["ans"]
