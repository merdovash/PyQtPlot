import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyQtPlot",
    version="0.0.1",
    author="Vlad Schekochikhin",
    author_email="vladschekochikhin@gmail.com",
    description="PyQt native library for plotting data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/merdovash/PyQtPlot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['PyQt5'],
    python_requires='>=3.6',
)