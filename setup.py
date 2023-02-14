# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
'''HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()'''

# This call to setup() does all the work
setup(
    name="Social-Media-Sentiment-Analysis",
    version="0.1.2",
    description="A Library for webscraping social media platforms (twitter) and using sentiment analysis on them!",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://social_media_sentiment_analysis.readthedocs.io/",
    author="Raf Muz",
    author_email="CyberRaf01@gmail.com",
    license="GPLv3",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["Social_Media_Sentiment_Analysis"],
    include_package_data=True,
    install_requires=["snscrape","flair>=0.11.1","pandas"]
)