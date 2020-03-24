import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kemksp", # Replace with your own username
    version="0.0.1",
    author="Kontiko",
    author_email="kontiko.fb@gmail.com",
    description="A package to manage your KSP Addons",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kontiko/Kerbal-Extension-Manager",
    packages= setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'kem = kemksp.kemterminal:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
) 

