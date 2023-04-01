from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    return list(set(row["industry"] for row in jobs if row["industry"]))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job.get("industry") == industry]
