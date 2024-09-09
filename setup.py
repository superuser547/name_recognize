from setuptools import setup, find_packages

setup(
    name="name_recognize",
    version="0.1.0",
    author="SuperUser",
    description="Библиотека для распознавания и нормализации имен на русском языке с поддержкой нескольких стран",
    packages=find_packages(),
    include_package_data=True,
    package_data={'name_recognize': ['names_ru.csv']},
    install_requires=[],
)
