import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geolocation",
    version="1.0.0-a.1",
    author="Lo Han",
    author_email="lohan.uchsa@protonmail.com",
    description="Geolocation Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sourcerer0/geolocation",
    packages=setuptools.find_packages(),
    keywords="bot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pycountry>=20.7.3',
        'Delorean>=1.0.0',
        'geopy>=2.1.0',
        'pytz>=2021.1',
    ]
)
