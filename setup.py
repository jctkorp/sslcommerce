from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sslcommerz/__init__.py
from sslcommerz import __version__ as version

setup(
	name="sslcommerz",
	version=version,
	description="Sslcommerz Payment Gateway",
	author="Tridotstech Pvt Ltd",
	author_email="info@tridotstech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
