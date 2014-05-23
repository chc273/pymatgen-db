import os

from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

with open("README.rst") as f:
    long_desc = f.read()
with open("VERSION") as f:
    version = f.read().strip()

static_data = []
for parent, dirs, files in os.walk(os.path.join("matgendb", "webui",
                                                "static")):
    for f in files:
        if not f.endswith(".psd"):
            print("Adding {} to static_data".format(f))
            static_data.append(os.path.join(parent.lstrip("matgendb/webui/"),
                                            f))

setup(
    name="pymatgen-db",
    packages=find_packages(),
    version=version,
    install_requires=["pymatgen>=2.8.8", "monty>=0.1.0",
                      "pymongo>=2.4", "prettytable>=0.7",
                      "django>=1.5", "mongomock>=1.2.0", "smoqe>=0.1.1"],
    package_data={"matgendb": ["*.json"],
                  "matgendb.webui.home": ["templates/*"],
                  "matgendb.webui": static_data},
    author="Shyue Ping Ong, Dan Gunter",
    author_email="shyuep@gmail.com",
    maintainer="Dan Gunter",
    maintainer_email="dkgunter@lbl.gov",
    url="https://github.com/materialsproject/pymatgen-db",
    license="MIT",
    description="Pymatgen-db is a database add-on for the Python Materials "
                "Genomics (pymatgen) materials analysis library.",
    long_description=long_desc,
    keywords=["vasp", "gaussian", "materials", "project", "electronic",
              "structure", "mongo"],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends"
    ],
    scripts=[os.path.join("scripts", f) for f in os.listdir("scripts")
             if not os.path.isdir(os.path.join("scripts", f))]
)
