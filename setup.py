from distutils.core import Extension, setup

# A Python package may have multiple extensions, but this template has one.
module1 = Extension(
    "DemoPackage",
    define_macros=[("USE_PRINTER", "1")],
    include_dirs=["include"],
    sources=["src/demo.c"],
)

setup(
    name="DemoPackage",
    version="1.0",
    description="This is a demo package",
    author="<first> <last>",
    author_email="person@site.com",
    url="https://docs.python.org/extending/buildling",
    long_description=open("README.rst").read(),
    ext_modules=[module1],
)
