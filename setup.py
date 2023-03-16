from setuptools import setup, find_packages


setup(
    name="geo",
    version="0.0.1",
    author="Minh-Chien Trinh",
    author_email="mctrinh@jbnu.ac.kr",
    packages=find_packages(),
    description="A Python package for practical geometry algorithms.",
    url="https://github.com/mctrinh/geo",
    license="MIT",
    python_requires = '>=3.7',
    keywords="geometry, geo",
    install_requires = ['numpy']
)