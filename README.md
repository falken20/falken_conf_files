<div align="center">
<!-- Para logo se puede usar https://studio.tailorbrands.com/-->
<img src="./docs/img/logo_app.png" alt="drawing" width="400"/>
<a href="https://richionline-portfolio.nw.r.appspot.com"><img src="https://falken-home.herokuapp.com/static/home_project/img/falken_logo.png" width=40 alt="Personal Portfolio web"></a>

### Shields (https://shields.io/)

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![GitHub language count](https://img.shields.io/github/languages/count/falken20/falken_conf_files) ![GitHub Top languaje](https://img.shields.io/github/languages/top/falken20/falken_conf_files) ![Test coverage](https://img.shields.io/badge/test%20coverage-0%25-green)

[![Richi web](https://img.shields.io/badge/web-richionline-blue)](https://richionline-portfolio.nw.r.appspot.com) [![Twitter](https://img.shields.io/twitter/follow/richionline?style=social)](https://twitter.com/richionline)

Optionals:
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0)](https://www.python.org) 
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/falken20/primazon)
[![PyPI version](https://badge.fury.io/py/rich.svg)](https://badge.fury.io/py/rich)
![Tag](https://img.shields.io/badge/tag-1.0.0-blue) 
![Release](https://img.shields.io/badge/release-1.0.0-blue)
</div>

### falken_conf_files
Different configure files to copy in the projects

- .github/workflows/python-app.yml -> CICD with GitHub
- .env -> Several environment vars
- .flaskenv -> Several Flask environment vars
- .gcloudignore -> Default config for Files and folders that it shouldn't upload to Google Cloud Platform
- .gitignore -> Default config about .gitignore for my projects
- config_fk.py -> Python config file about several personal consts
- error.py -> Python example to manage a commun error message

- falken_logo.ico
- falken_logo.png

---

##### Setup


```bash
pip install -r requirements.txt
```

##### Running the app

```bash
cd falken_chat
python main.py
```

##### Setup tests

```bash
pip install -r requirements-tests.txt
```

##### Running the tests with pytest and coverage

```bash
./scripts/ccheck_project.sh
```
or
```bash
coverage run -m pytest -v && coverage html --omit=*/venv/*,*/tests/*
```
