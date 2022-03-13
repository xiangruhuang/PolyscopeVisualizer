import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
          
setuptools.setup(
    name="vis3d",
    version="0.0.1",
    description="Visualization Code Wrapper for polyscope & 3D data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
