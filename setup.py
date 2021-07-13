from setuptools import setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Enviroment',
    version='0.1.0',
    description='Simple but effective logging & more.',
    long_description=readme,
    author='Commander07',
    url='https://github.com/commander07/enviroment',
    license=license,
    packages=["enviroment"],
    install_requires=[
        'rich',
    ],
)
