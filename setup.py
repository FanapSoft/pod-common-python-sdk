from setuptools import setup
from pod_common import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()


requires = ["pod-base>=1,<2"]

setup(
    name="pod-common",
    version=__version__,
    url="https://github.com/FanapSoft/pod-common-python-sdk",
    license="MIT",
    author="ReZa ZaRe",
    author_email="rz.zare@gmail.com",
    description="POD common services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["POD", "common", "pod sdk"],
    packages=["pod_common"],
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Natural Language :: English",
        "Natural Language :: Persian",
    ],
    python_requires=">=2.7",
    package_data={
        "pod_common": ["*.ini", "*.json"]
    },
    project_urls={
        "Documentation": "http://docs.pod.ir/v1.0.0.2/PODSDKs/python/5201/common",
        "Source": "https://github.com/FanapSoft/pod-common-python-sdk",
        "Tracker": "https://github.com/FanapSoft/pod-common-python-sdk/issues"
    }
)
