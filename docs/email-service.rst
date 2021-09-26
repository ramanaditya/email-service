###############
Email Service
###############

Python package to quickly integrate different email services with your Application with just 3 lines of code.

.. image:: https://img.shields.io/pypi/v/email-service.svg?color=2897A6
    :target: https://pypi.org/project/email-service/
    :alt: pypi
.. image:: https://img.shields.io/pypi/pyversions/email-service.svg
    :target: https://pypi.org/project/email-service/
    :alt: python
.. image:: https://img.shields.io/badge/license-MIT-red.svg?style=flat-square
    :target: https://github.com/ramanaditya/email-service
    :alt: license
.. image:: https://img.shields.io/github/v/release/ramanaditya/email-service.svg
    :target: https://github.com/ramanaditya/email-service/releases/
    :alt: GitHub Release
.. image:: https://img.shields.io/github/stars/ramanaditya/email-service.svg?logo=github
    :target: https://github.com/ramanaditya/email-service/stargazers
    :alt: GitHub stars
.. image:: https://img.shields.io/github/forks/ramanaditya/email-service.svg?logo=github&color=teal
    :target: https://github.com/ramanaditya/email-service/network/members
    :alt: GitHub forks


----


Send Your email without caring about the backend code.

:GitHub: `ramanaditya/email-service <https://github.com/ramanaditya/email-service>`__
:PyPI: `pypi.org/project/email-service <https://pypi.org/project/email-service>`__


Usage
======


Install it with pip
--------------------
.. code-block:: console

    $ pip install email-service


Email Integration
--------------------
``Save the`` **API_KEY** ``in the`` **.env** ``file as``


.. code-block:: text

    SENDGRID_API_KEY=api_key


Import EmailHandler
--------------------
.. code-block:: python

    >>> from email_service.email_handler import EmailHandler


Form the dictionary of data
------------------------------
.. code-block:: python

    data = {
        "from_email": "Name WithSpace <from_email@gmail.com>",  # Required
        "subject": "This is the test for the Individual email", # Required
        "reply_to_addresses": "email1@gmail.com",
        "html_body": "<h1>Email Template for Individual email</h1>",    # Either of html_body or text_body is required
        "text_body": "Email Template for Individual email",
        "to_for_bulk": [{"name": "Name", "email": "email@gmail.com"},], # Required for Bulk Email
        "recipients": {
            "to": [{"name": "name1", "email": "email1@gmail.com"},],    # Required
            "cc": [{"name": "name2", "email": "email2@google.com"},],
            "bcc": [{"name": "name3", "email": "email3@google.com"},],
        },
        "attachments": [
            "file_path (pdf)", "calender invite (ics)", "image_path (png/jpg/jpeg)"
        ]
    }


Send the email
-----------------
.. code-block:: python

    >>> # For Individual Email
    >>> send_email = EmailHandler()

    >>> # For Bulk Email
    >>> send_email = EmailHandler(email_type="BULK")


Sendgrid Integration
----------------------
.. code-block:: python

    >>> # Send it using sendgrid
    >>> response = send_email.sendgrid(data)


Response
-----------
.. code-block:: yaml

    status_code:
        202: OK,
        400: Error
    message: Error or Success Message


Development
============

.. image:: https://img.shields.io/github/languages/code-size/ramanaditya/email-service?logo=github
    :target: https://github.com/ramanaditya/email-service/
    :alt: GitHub code size in bytes
.. image:: https://img.shields.io/github/repo-size/ramanaditya/email-service?logo=github
    :target: https://github.com/ramanaditya/email-service/
    :alt: GitHub repo size
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square
    :target: https://github.com/ramanaditya/email-service
    :alt: black


Setup
-------


Clone the repository
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ git clone https://github.com/ramanaditya/email-service


Create a virtual environment using virtualenv or venv.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ python -m venv venv
    $ source venv/bin/activate


Upgrade pip
^^^^^^^^^^^^^^
.. code-block:: console

    $ python -m pip install --upgrade pip


Install python packages
^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ python -m pip install -r requirements.txt


Git Flow
----------


Create new Branch from `develop` branch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ git checkout -b develop origin/develop
    $ git checkout -b feature_branch


Push the Code
^^^^^^^^^^^^^^^
.. code-block:: console

    $ git add file_which_was_changed
    $ git commit -m "Commit Message"
    $ git push -u origin feature_branch


Build Package for Local Testing
================================
.. code-block:: console

    $ # Build the package
    $ python setup.py build

    $ # Install the package
    $ python setup.py install


PyPI
-----


This is just for the reference and need not to be run,
If you want to run these scripts, please take a note of this

* For testing, we maintain the test package at `testpypi <https://test.pypi.org/project/email-service/>`__
* PyPI or Test PyPI, does not accept same file name, you can change the file name or version in the `./setup.py <https://github.com/ramanaditya/email-service/blob/main/setup.py>`__
* You will be prompted to enter
    - Either username and password
    - or, username as "__token__" and password as token (can be generated from the pypi website)
* It will be uploaded to your pypi or testpypi account


Generating distribution archives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ # Downloading latest version of setuptools
    $ python -m pip install --user --upgrade setuptools wheel

    $ python setup.py sdist bdist_wheel


Uploading to Test PyPI
^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ # Upload to Test PyPI https://test.pypi.org/
    $ python -m twine upload --repository testpypi dist/*


Download the package from Test PyPI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ python -m pip install -i https://test.pypi.org/simple/ email-service


Check against the code
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ # Edit the file inside /example to have some valid data
    $ # export SENDGRID_API_KEY before running the script
    $ python individual_email.py  # For individual email
    $ python bulk.py  # For bulk email


Uploading to PyPI
^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ # Upload to PyPI https://pypi.org/
    $ python -m twine upload dist/*


Download the package from Test PyPI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ python -m pip install -i https://test.pypi.org/simple/ email-service


Issues
========


.. image:: https://img.shields.io/github/issues/ramanaditya/email-service?logo=github
    :target: https://github.com/ramanaditya/email-service/issues
    :alt: GitHub issues
.. image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat&logo=git&logoColor=white
    :target: https://github.com/ramanaditya/email-service/pulls
    :alt: PRs Welcome
.. image:: https://img.shields.io/github/last-commit/ramanaditya/email-service?logo=github
    :target: https://github.com/ramanaditya/email-service/
    :alt: GitHub last commit


+-------------+-------------+
| Issue No.   | Issue       |
+=============+=============+
|             |             |
+-------------+-------------+


**NOTE**: **Feel free to** `open issues <https://github.com/ramanaditya/email-service/issues/new/choose>`__. Make sure you follow the Issue Template provided.


Contribution Guidelines
========================

.. image:: https://img.shields.io/github/issues-pr-raw/ramanaditya/email-service?logo=git&logoColor=white
    :target: https://github.com/ramanaditya/email-service/compare
    :alt: GitHub pull requests
.. image:: https://img.shields.io/github/contributors/ramanaditya/email-service?logo=github
    :target: https://github.com/ramanaditya/email-service/graphs/contributors
    :alt: GitHub contributors


* Write clear meaningful git commit messages (Do read `this <http://chris.beams.io/posts/git-commit/>`__).
* Make sure your PR's description contains GitHub's special keyword references that automatically close the related issue when the PR is merged. (Check `this <https://github.com/blog/1506-closing-issues-via-pull-requests>`__ for more info)
* When you make very very minor changes to a PR of yours (like for example fixing a text in button, minor changes requested by reviewers) make sure you squash your commits afterward so that you don't have an absurd number of commits for a very small fix. (Learn how to squash at `here <https://davidwalsh.name/squash-commits-git>`__)
* Please follow the `PR Template <https://github.com/ramanaditya/email-service/blob/main/.github/PULL_REQUEST_TEMPLATE.md>`__ to create the PR.
* Always open PR to ``develop`` branch.
* Please read our `Code of Conduct <https://github.com/ramanaditya/email-service/blob/main/CODE_OF_CONDUCT.md>`__.
* Refer `this <https://github.com/ramanaditya/email-service/blob/main/CONTRIBUTING.md>`__ for more.


``If you`` ❤️ ``this`` `repository <https://github.com/ramanaditya/email-service>`__ ``, support it by star 🌟``
