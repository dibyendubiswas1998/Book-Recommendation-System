from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="v.0.0.1",
    author="dibyendubiswas1998",
    author_email="dibyendubiswas1998@gmail.com",
    description="It's a complete Pipeline for this project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dibyendubiswas1998/Books-Recommendation-System.git",
    packages=["src"],
    license="GNU",
    python_requires=">=3.10",
    install_requires=[
        'dvc',
        "dvc[gdrive]",
        'pandas',
        'scikit-learn'
    ]
)