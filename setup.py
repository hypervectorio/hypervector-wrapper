from setuptools import setup, find_packages

setup(
    name='hypervector-wrapper',
    version='0.0.1',
    description='Python wrapper to use the Hypervector API',
    author='Jason Costello, Hypervector Limited',
    author_email="jason@hypervector.io",
    url="https://github.com/hypervectorio/hypervector-wrapper",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)