import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="diebold-mariano-test",
    version="0.0.6",
    author="echosun",
    author_email="echosun1996@126.com",
    description="Diebold Mariano test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/echosun1996/DieboldMarianoTest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'scipy>=1.4.1',
    ],
    python_requires='>=3.5',
)