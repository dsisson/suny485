# Example code for the class CSC 485, "Testing for Developers"

## Basic Design

Every homework assignment will involve application code to be tested, and the test code.

The assignment's application code goes in a python package (folder + _ _ init_ _.py file) under the "projects" folder.

The assignment's test code goes in a same-named folder under the "tests" folder.


## Running Code Coverage
In order to run coverage against your project, you need to:
1. install it using ````pip install -U coverage```` from the command line
2. get the version from a ````pip freeze```` command
3. make sure you are in a new local branch!
4. add a line to requirements.txt with the coverage version
5. update your setup.cfg with the following new sections:
````yaml
[coverage:run]
# provide data on branch coverage
branch = True

# ignore the empty __init__.py files
omit = */__init__.py

# just look at the "application" code, not the test code
# this requires that you run your code from your *project* folder
source = suny485/projects

[coverage:report]
exclude_also =
    # don't complain about non-runnable code
    if __name__ == .__main__.:
````

Once code coverage is installed and configured, you can generate your coverage report by running these commands:
````commandline
# use the coverage CLI tool to run pytest
coverage run -m pytest -v --tb=short

# when the tests finish, run the report
coverage report -m

# you should get output that looks like this:

Name                                      Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------------------
suny485/projects/hw10/fruit_query.py          5      0      2      0   100%
suny485/projects/hw11/homework11.py          11      0      0      0   100%
suny485/projects/hw12/homework12.py          15      0      4      0   100%
suny485/projects/hw13/homework13.py          18      0      8      0   100%
suny485/projects/hw14/api.py                  9      0      0      0   100%
suny485/projects/hw14/password_utils.py      18      0      8      0   100%
suny485/projects/hw15/api.py                 18      1      2      1    90%   101
suny485/projects/hw15/password_utils.py      18      0      8      0   100%
suny485/projects/hw16/api.py                 18     18      2      0     0%   1-117
suny485/projects/hw16/password_utils.py      18     18      8      0     0%   1-42
suny485/projects/hw16/web.py                 15     15      0      0     0%   1-42
-------------------------------------------------------------------------------------
TOTAL                                       163     52     42      1    69%

````

Documentation on coverage for Python can be found at [Coverage.py](https://coverage.readthedocs.io/en/latest/cmd.html). 

