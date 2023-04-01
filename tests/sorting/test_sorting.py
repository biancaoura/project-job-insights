import pytest
from src.pre_built.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"max_salary": 10000, "min_salary": 1000, "date_posted": "2023-01-30"},
        {"max_salary": 7000, "min_salary": 5000, "date_posted": "2023-02-12"},
        {"max_salary": 5000, "min_salary": 2000, "date_posted": "2023-01-02"},
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "max_salary")
    assert [job["max_salary"] for job in jobs] == [10000, 7000, 5000]

    sort_by(jobs, "min_salary")
    assert [job["min_salary"] for job in jobs] == [1000, 2000, 5000]

    sort_by(jobs, "date_posted")
    assert [job["date_posted"] for job in jobs] == [
        "2023-02-12",
        "2023-01-30",
        "2023-01-02",
    ]
