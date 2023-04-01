from typing import Union, List, Dict
from .jobs import read


def get_max_or_min_salary(path: str, setting: str) -> int:
    jobs = read(path)
    salaries = [
        int(job[f"{setting}_salary"])
        for job in jobs
        if job[f"{setting}_salary"].isdigit()
    ]

    if salaries:
        if setting == "max":
            return max(salaries)
        elif setting == "min":
            return min(salaries)
    return 0


def get_max_salary(path: str) -> int:
    return get_max_or_min_salary(path, "max")


def get_min_salary(path: str) -> int:
    return get_max_or_min_salary(path, "min")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        max_salary = float(job.get("max_salary"))
        min_salary = float(job.get("min_salary"))
        salary = float(salary)
    except (TypeError, ValueError):
        raise ValueError("Invalid salary")
    if max_salary < min_salary:
        raise ValueError("Max salary must be greater than min salary")
    return max_salary >= salary >= min_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filtered = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered.append(job)
        except ValueError:
            pass
    return filtered
