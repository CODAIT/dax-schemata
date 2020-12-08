# DAX Schemata

This is the repository that we maintain the default DAX schema files for
[PyDAX](https://github.com/codait/pydax).

To run tests locally, run:

    $ pip install -U -rrequirements/tox.txt  # If you are inside a virtual environment, conda environment
    $ pip3 install --user -U tox  # If you are outside any virtual environment or conda environment

    # lint tests
    $ tox -e lint
    # pydax tests
    $ tox -e pydax
