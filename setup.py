"""Setup module for python-reaperdaw."""
from pathlib import Path

from setuptools import find_packages, setup

PROJECT_DIR = Path(__file__).parent.resolve()
README_FILE = PROJECT_DIR / "README.md"
VERSION = "0.0.4"


setup(
    name="python-reaperdaw",
    version=VERSION,
    url="https://github.com/kubawolanin/python-reaperdaw",
    download_url="https://github.com/kubawolanin/python-reaperdaw",
    author="Kuba Wolanin",
    author_email="kuba.wolanin@gmail.com",
    description="Python wrapper for REAPER DAW REST API",
    long_description=README_FILE.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["reaperdaw"]),
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Home Automation",
    ],
)
