import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="pandalchemy2",
    version="0.0.0",
    description="Manipulate SQL tables using a Pandas API and SqlAlchemy back end.",
    long_description=README,
    long_description_content_type="text/markdown",
    #url="https://github.com/eddiethedean/pandalchemy2",
    author="Odos Matthews",
    author_email="odosmatthews@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=['pandas', 'sessionize']
)