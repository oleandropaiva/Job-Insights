from typing import List, Dict

from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    listIndustry = read(path)
    listIndustries = []
    for job in listIndustry:
        if job["industry"] != "" and job["industry"] not in listIndustries:
            listIndustries.append(job["industry"])
    return listIndustries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return [job for job in jobs
            if job['industry'] == industry]
