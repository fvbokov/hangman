from setuptools import setup, find_packages

install_requires = []
extras_require = {
    "freeze": ["pyinstaller"]
}

entry_points = {
    "console_scripts": [
        "hangman=hangman.__main__:main",
    ]
}

setup(
    name="hangman-game",
    version="1.0",
    description="",
    install_requires=install_requires,
    extras_require=extras_require,
	package_data={"hangman": ["assets/*.txt"]},
    packages=find_packages(),
    entry_points=entry_points,
)
