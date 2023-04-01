from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    keys = ["title", "salary", "type"]
    assert [jobs[0][i] for i in keys if jobs[0].get(i)]
