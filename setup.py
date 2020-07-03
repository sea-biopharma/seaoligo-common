import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="seaoligo-common",
    version="1.1.0",
    description="Common python packages for sea-web-services",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sea-biopharma/seaoligo-common",
    author="SEA Biopharma",
    author_email="sea.biopharma@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["seaoligo-common"],
    include_package_data=True,
    install_requires=['flask', 'flask-sqlalchemy', 'pyjwt'],
)
