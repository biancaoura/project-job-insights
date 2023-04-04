# Job Insights Project

## Summary

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#additional-info">Additional Info</a></li>
  </ol>
</details>

## About The Project

Web app for job analyses developed with `Python` and `Flask`.


> This is a project developed as part of my studies to help me learn about Python and Data Analysis

### Built With

[![Python][Python.io]][Python-url]

[![Flask][Flask.io]][Flask-url]

[![Pytest][Pytest.io]][Pytest-url]


## Getting Started

### Installation

1. Clone the repo
```
$ git clone git@github.com:biancaoura/project-job-insights.git
```
2. Go to the repository
```
$ cd project-job-insights
```
3. Create a virtual environment and activate it
```
$ python3 -m venv .venv && source .venv/bin/activate
```
4. Install the dependencies inside the virtual environment
```
$ python3 -m pip install -r dev-requirements.txt
```



## Usage


Run the app:
```
$ flask run
```

By default, the server is running at `http://127.0.0.1:5000`



## Additional Info

> Data extracted from `Glassdoor` with `Kaggle`

[Python.io]: https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white
[Python-url]: https://www.python.org
[Flask.io]: https://img.shields.io/badge/flask-000000?logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[Pytest.io]: https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white
[Pytest-url]: https://docs.pytest.org/en/7.2.x/