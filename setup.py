from setuptools import setup, find_packages
from pathlib import Path

readme = Path("README.md").read_text("utf-8")

setup(
    name='quick-django-docker-setup',
    version='0.1',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/KrzysztofCzapla/quick-django-docker-setup',
    packages=find_packages(),
    include_package_data=True,
    keywords="quick,django,docker,setup",
    install_requires=[
      "tqdm"
    ],
    license_files=['LICENSE'],
    entry_points={
        'console_scripts': [
            'quick-django-docker-setup = quick_django_docker_setup.main:main'
        ]
    }
)
