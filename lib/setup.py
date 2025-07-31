from setuptools import setup, find_packages

setup(
    name='apipie',
    version='0.5.0',
    description='an api organization tool',
    author='kokorocks',
    author_email='ejkmatthison@gmail.com',
    url='https://github.com/kokos-lab/apipie',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'sanic',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

from setuptools import setup, find_packages

setup(
    name="apipie",
    version="0.4.4",
    description="A simple API proxy with rate limiting and API key support for api organization.",
    author="kokorocks",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "sanic",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "apipie=apipie:main"
        ]
    },
    python_requires=">=3.7",
)