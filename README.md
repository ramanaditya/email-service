# Email Service

Python package to quickly integrate different email services with your Application with just 3 lines of code.

[![pypi](https://img.shields.io/pypi/v/email-service.svg?color=2897A6)](https://pypi.org/project/email-service/)
[![python](https://img.shields.io/pypi/pyversions/email-service.svg)](https://pypi.org/project/email-service/)
[![license](https://img.shields.io/badge/license-MIT-red.svg?style=flat-square)](https://github.com/ramanaditya/email-service)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ramanaditya/email-service)
[![GitHub Release](https://img.shields.io/github/v/release/ramanaditya/email-service.svg)](https://github.com/ramanaditya/email-service/releases/)
[![GitHub stars](https://img.shields.io/github/stars/ramanaditya/email-service.svg?logo=github)](https://github.com/ramanaditya/email-service/stargazers) 
[![GitHub forks](https://img.shields.io/github/forks/ramanaditya/email-service.svg?logo=github&color=teal)](https://github.com/ramanaditya/email-service/network/members) 

<hr>

Send Your email without caring about the backend code. 

- GitHub: https://github.com/ramanaditya/email-service
- PyPI: https://pypi.org/project/email-service/

## Install it with pip
```bash
pip install email-service
```

## Email Integration
> Save the `API_KEY` in the `.env` file as
>
> SENDGRID_API_KEY=api_key
>

### Import EmailHandler
```python
from email_service.email_handler import EmailHandler
```

### Form the dictionary of data
```python
data = {
    "from_email": "Name WithSpace <from_email@gmail.com>",  # Required
    "subject": "This is the test for the Individual email", # Required
    "reply_to_addresses": "email1@gmail.com",  
    "html_body": "<h1>Email Template for Individual email</h1>",    # Either of html_body or text_body is required
    "text_body": "Email Template for Individual email",
    "to_for_bulk": [{"name": "Name", "email": "email@gmail.com"},], # Required for Bulk Email
    "receipients": {
        "to": [{"name": "name1", "email": "email1@gmail.com"},],    # Required
        "cc": [{"name": "name2", "email": "email2@google.com"},],   
        "bcc": [{"name": "name3", "email": "email3@google.com"},],
    },
    "attachments": [
        "file_path (pdf)", "calender invite (ics)", "image_path (png/jpg/jpeg)"
    ]
}

```

### Send the email
```python

# For Individual Email
send_email = EmailHandler()

# For Bulk Email
send_email = EmailHandler(email_type="BULK")

```

### Sendgrid Integration

```python
# Send it using sendgrid
response = send_email.sendgrid(data)

```

### Response
```yaml
status_code:
    202: OK,
    400: Error
message: Error or Success Message
```

# Development

## Setup
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ramanaditya/email-service?logo=github)](https://github.com/ramanaditya/email-service/) 
[![GitHub repo size](https://img.shields.io/github/repo-size/ramanaditya/email-service?logo=github)](https://github.com/ramanaditya/email-service/)

1.  Clone the repository
    ```bash
    git clone https://github.com/ramanaditya/email-service
    ```

2.  Create a virtual environment using virtualenv or venv.
     ```bash
     python -m venv venv 
     source venv/bin/activate
     ```

3. Upgrade pip
    ```bash
    python -m pip install --upgrade pip
    ```
3.  Install python packages
     ```bash
     python -m pip install -r requirements.txt
     ```

4. Create new Branch from `develop` branch
    ```bash
    git checkout -b develop origin/develop
    git checkout -b feature_branch
    ```

5. Generating distribution archives
    ```bash
    # Downloading latest version of setuptools
    python -m pip install --user --upgrade setuptools wheel

    python setup.py sdist bdist_wheel
    ```

6. Uploading to Test PyPI
    ```bash
    # Upload to Test PyPI https://test.pypi.org/ 
    python -m twine upload --repository testpypi dist/*
    ```

7. Download the package
    ```bash
    python -m pip install -i https://test.pypi.org/simple/ email-service
    ```

8. Check against the code
    ```bash
    # Edit the file inside /example to have some valid data
    # export SENDGRID_API_KEY before running the file
    python individual_email.py  # For individual email
    python bulk.py  # For bulk email
    ```
7. Push the Code
    ```bash
    $ git add file_which_was_changed
    $ git commit -m "Commit Message"
    $ git push -u origin feature_branch
    ```

## Issues

[![GitHub issues](https://img.shields.io/github/issues/ramanaditya/email-service?logo=github)](https://github.com/ramanaditya/email-service/issues) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat&logo=git&logoColor=white)](https://github.com/ramanaditya/email-service/pulls) 
[![GitHub last commit](https://img.shields.io/github/last-commit/ramanaditya/email-service?logo=github)](https://github.com/ramanaditya/email-service/)

> 1. Integrating Mailgun
> 2. Integrating Amazon SES

**NOTE**: **Feel free to [open issues](https://github.com/ramanaditya/email-service/issues/new/choose)**. Make sure you follow the Issue Template provided.

## Contribution Guidelines

[![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/ramanaditya/email-service?logo=git&logoColor=white)](https://github.com/ramanaditya/email-service/compare) 
[![GitHub contributors](https://img.shields.io/github/contributors/ramanaditya/email-service?logo=github)](https://github.com/ramanaditya/email-service/graphs/contributors) 

- Write clear meaningful git commit messages (Do read [this](http://chris.beams.io/posts/git-commit/)).
- Make sure your PR's description contains GitHub's special keyword references that automatically close the related issue when the PR is merged. (Check [this](https://github.com/blog/1506-closing-issues-via-pull-requests) for more info)
- When you make very very minor changes to a PR of yours (like for example fixing a text in button, minor changes requested by reviewers) make sure you squash your commits afterward so that you don't have an absurd number of commits for a very small fix. (Learn how to squash at [here](https://davidwalsh.name/squash-commits-git))

- Please follow the [PR Template](https://github.com/ramanaditya/email-service/blob/master/.github/PULL_REQUEST_TEMPLATE.md) to create the PR.
- Always open PR to `develop` branch.
- Please read our [Code of Conduct](./CODE_OF_CONDUCT.md).
- Refer [this](https://github.com/ramanaditya/email-service/blob/master/CONTRIBUTING.md) for more.

> If you like this [repository](https://github.com/ramanaditya/email-service), support it by star :star2:
