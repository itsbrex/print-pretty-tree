from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent

if this_directory.joinpath("README.md").is_file():
    long_description = this_directory.joinpath("README.md").read_text()
else:
    long_description = ""

requirements = []

setup(
    name="print-pretty-tree",
    version="0.0.3",
    author="itsbrex",
    author_email="itsbrexnpm@gmail.com",
    description="A simple Python script that displays the directory tree of the current working directory with color-coded output for easy file identification.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itsbrex/print-pretty-tree",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
        "Topic :: System :: Filesystems",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        ],
    keywords="directory, tree, pretty-print, file-system, visualization, color-coded, file-identification, command-line, CLI, directory-structure",
    project_urls={},
    entry_points={
    'console_scripts': [
        'pt = print_pretty_tree.main:main',
        'ptree = print_pretty_tree.main:main'
    ]
}
)
