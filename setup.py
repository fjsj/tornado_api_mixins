import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "tornado_api_mixins",
    version = "0.0.1",
    author = "Didip Kerabat",
    author_email = "didipk@gmail.com",
    description = ("Packaged version of tornado_api "
                   "(https://github.com/didip/tornado_api) "
                   "including only FacebookGraphMixin and FoursquareMixin."),
    license = "Apache License, Version 2.0",
    keywords = "tornado mixin facebook foursquare api client",
    url = "https://github.com/fjsj/tornado_api",
    packages=['tornado_api_mixins'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: Apache Software License",
    ],
)