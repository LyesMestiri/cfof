import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cfof",
    version="0.4.1",
    author="Lyès Mestiri",
    author_email="lyes.mestiri@hotmail.fr",
    description="Concentration Free Outlier Factor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LyesMestiri/cfof",
    project_urls={
        "Bug Tracker": "https://github.com/LyesMestiri/cfof/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "scipy",
        "scikit-learn",
    ],
)
