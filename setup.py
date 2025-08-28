from setuptools import setup, find_packages

setup(
    name="cmdplug",
    version="0.1.0",
    description="Create simple commands in Python with ease!",
    author="HeapX",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Intended Audience :: Developers",
    ],
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages(where="src", include=["cmdplug*"]),
    project_urls={
        "Repository": "https://github.com/Security-Development/cmdplug",
    },
)
