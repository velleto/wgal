import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wgal",
    version="0.0.1",
    author="Ryan Rueger",
    author_email="dev@velleto.com",
    description="Creates a static HTML/CSS/JS photo gallery.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/velleto/wgal",
    packages=setuptools.find_packages(),
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    scripts=["bin/wgal"],
    include_package_data=True,
)
