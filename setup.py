import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geolocation",
    version="1.0.0-a.3",
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
    python_requires='>=3.6',
    install_requires=[
        'Delorean>=1.0.0',
        'geopy>=2.1.0',
    ]
)
