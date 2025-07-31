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
