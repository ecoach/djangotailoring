from setuptools import setup, find_packages

setup(
    name = "djangotailoring",
    version = "0.5",
    packages = find_packages(),
    include_package_data = True,
    package_data = {
        '': ['*.txt', '*.rst', '*.json', '*.html', '*.css'],
        'djangotailoring.management': ['*.pyt'],
    }
)
