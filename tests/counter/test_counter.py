from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "Qualifications") == 1651
    assert count_ocurrences("data/jobs.csv", "Qualifications") != 0
    assert count_ocurrences("data/jobs.csv", "testando") == 0
