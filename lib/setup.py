from setuptools import setup, find_packages

setup(
    name="apipie",
    version="0.4.4",
    description="A simple API proxy with rate limiting and API key support for API organization.",
    author="kokorocks",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "sanic",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "apipie=apipie.main:main"
        ]
    },
    python_requires=">=3.7",
)
