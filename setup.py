import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geolocation",
    version="1.1.0",
    author="Lo Han",
    author_email="lohan.uchsa@protonmail.com",
    description="Geolocation Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elleaech/geolocation",
    packages=setuptools.find_packages(),
    keywords="bot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Babel==2.9.0",
        "Delorean==1.0.0",
        "geographiclib==1.50",
        "geopy==2.1.0",
        "humanize==3.2.0",
        "python-dateutil==2.8.1",
        "pytz==2021.1",
        "six==1.15.0",
        "tzlocal==2.1",
    ],
)
