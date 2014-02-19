# cookiecutter-pacostacos

Cookiecutter template for a RESTful web API service for a predictive
algorithm. See <https://github.com/audreyr/cookiecutter>.

-   Free software: BSD license
-   [Pytest](http://pytest.org/) runner: Supports unittest, pytest, nose style tests and
    more
-   [TravisCCI](http://travis-ci.org/): Ready for Travis Continuous integration testing
-   [Tox](http://testrun.org/tox/) testing: Setup to easily test for python 2.6, 2.7, 3.3 and
    [PyPy](http://pypy.org/)
-   [Sphinx](http://sphinx-doc.org/) docs: Documentation raedy for generation with, for
    example, [ReadTheDocs](https://readthedocs.org/)
-   [Wheel](http://pythonwheels.com) support: Use the newest python package distribution
    standard from the get go
-   Uses [Flask-RESTful](http://flask-restful.readthedocs.org/en/latest/) to implement a REST
    API.

## Usage

Generate a predictive algorithm REST API:

    cookiecutter https://github.com/mdbecker/cookiecutter-pacostacos.git

Then:

-   Create a repo and put it there.
-   Add the repo to your Travis CI account.
-   Add the repo to your ReadTheDocs account + turn on the ReadTheDocs
    service hook.
-   Run tox to make sure all tests pass.
-   Release your package the standard Python way.
-   Test the example app by running:
```bash
curl http://localhost:5000/ -d "data=testing 123" -X PUT
{
    "result": "321 gnitset"
}
```

## Not Exactly What You Want?

Don't worry, you have options:

### Similar Cookiecutter Templates

-   [audreyr/cookiecutter-pypackage](https://github.com/Nekroze/cookiecutter-pypackage): The original pypackage, uses
    unittest for testing and other minor changes.

### Fork This

If you have differences in your preferred setup, I encourage you to fork
this to create your own version. Once you have your fork working, add it
to the Similar Cookiecutter Templates list with a brief explanation.
It's up to you whether or not to rename your fork.

### Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if
they make my own packaging experience better.
