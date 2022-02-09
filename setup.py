"""htmlx - Generate html with python 3"""

from setuptools import find_packages, setup

from htmlx import __version__ as version


def read(filename):
    """Returns the contents of a file."""
    with open(filename, encoding='utf-8') as file:
        return file.read()


setup(
    name="htmlx",
    version=version,
    author="@byteface",
    author_email="byteface@gmail.com",
    license="MIT",
    url="https://github.com/byteface/htmlx",
    download_url="https://github.com/byteface/htmlx/archive/" + version + " .tar.gz",
    description="Generate html with python 3",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    keywords=[
        "html",
        "generate",
        "templating",
        "dom",
        "vdom",
        "json",
        "web",
        "template",
        "DOM",
        "GUI",
        "render",
        "website",
        "apps",
        "html5",
        "SVG",
        "x3d",
        "events",
        "geom",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Multimedia :: Graphics :: Presentation",
        "Topic :: Software Development",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Terminals",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    install_requires=["urllib3~=1.26.7"],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "htmlx = htmlx.__main__:run",
        ],
    },
)
