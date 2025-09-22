from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Read the requirements from a file and return them as a list."""
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    return [req.strip() for req in requirements if req.strip() and req.strip() != "-e ."]
setup(
    name="datascienceproject",  # project name
    version="0.1.0",  # initial version
    author="Niharika Jain",
    author_email="niharikaflyhigh@gmail.com",
    description="A simple data science project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/USERNAME/DataScienceProject",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires=">=3.8",
)
