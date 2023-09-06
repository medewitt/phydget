from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'Phylogenetic Differential Gene Expression Tool'
LONG_DESCRIPTION = 'PhyDGET is a method for analyzing transcriptome-wide expression data in a phylogenetic context to highlight genes whose expression is changing on particular branches of a phylogeny.'

# Setting up
setup(
        name="PhyDGET", 
        version=VERSION,
        author="James Pease",
        author_email="@peaselab.org",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        license="GPL-3.0 license",
        install_requires=[],
        entry_points={
        'console_scripts': [
            'phydget = phydget:main_function'
        ],
        },
        keywords=['python', 'tools', 'internal', 'phylodynamics'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
