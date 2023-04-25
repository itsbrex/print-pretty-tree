from setuptools import setup, find_packages
import os

if os.path.exists("README.md"):
    with open("README.md", "r") as readme_file:
        readme = readme_file.read() 
else:
    readme = ""

requirements = []

setup(
    name="print-pretty-tree",
    version="0.0.1",
    author="itsbrex",
    author_email="itsbrexnpm@gmail.com",
    description="A short description of the project.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/itsbrex/print-pretty-tree",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[],
    keywords=[],
    project_urls={},
)
