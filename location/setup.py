from setuptools import setup, find_packages
from pkg_resources import parse_requirements

# Read the dependencies from requirements.txt
with open('requirements.txt', 'r') as file:
    requirements = [str(req) for req in parse_requirements(file)]

# Read the dependencies from test-requirements.txt
with open('test-requirements.txt', 'r') as file:
    test_requirements = [str(req) for req in parse_requirements(file)]

setup(
    name='location',
    version='1.0',
    packages=find_packages(),
    author='Josh B',
    description='A package for handling location data',  # Add a short description
    url='https://github.com/JoshuaBb/Venue/tree/main/location',  # Add the URL of your project repository
    install_requires=requirements,
    extras_require={
        'test': test_requirements
    },
    test_suite="test",
    # Add keywords to describe your project
    keywords='location venue',
)
