from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt")) as f:
    requirements = f.read().splitlines()

setup(
    name="ezapi-icc-pro",
    packages=["icc_pro"],
    entry_points={"console_scripts": []},
    include_package_data=True,
    package_data={},
    install_requires=requirements,
    setup_requires=["setuptools_scm", "pytest-runner"],
    use_scm_version=True,
    tests_require=["pytest"],
    test_suite="tests",
    author="Zeheng Li",
    author_email="imzehengl@gmail.com",
    maintainer="Zeheng Li",
    maintainer_email="imzehengl@gmail.com",
    description="A Python wrapper for ICC PRO RESTful API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zehengl/ezapi-icc-pro/",
)
