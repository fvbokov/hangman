from setuptools import setup, find_packages

install_requires = []

setup(
    name="hangman-game",
    version="1.0",
    description="",
    install_requires=install_requires,
	package_data={'': ['hangman/assets']},
    packages=find_packages(),
)