import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gsearch", # Replace with your own username
    version="0.0.1",
    author="Itay Sin Malia",
    author_email="itays.malia@gmail.com",
    description="A google cli interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itaysmalia/gsearch.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data={
        "":["by.txt","icon.txt"]
    }
)