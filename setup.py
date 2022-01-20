from distutils.core import setup

with open("README.md", 'r') as f:
    long_description = f.read()

VERSION = "0.5"

setup(
    name='map_tile_stitcher',
    packages=['map_tile_stitcher', 'map_tile_stitcher.util', 'map_tile_stitcher.definitions'],
    version=VERSION,
    license='apache-2.0',
    description='Downloads and stitches tiles to a large high-resolution map on any zoom level',
    long_description=long_description,
    author='Lukas Baur',
    url='https://github.com/baurls/TileStitcher',  # Provide either the link to your github or to your website
    download_url='https://github.com/baurls/TileStitcher/archive/refs/tags/v{}.tar.gz'.format(VERSION),
    keywords=['tiling', 'map', 'tiles'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'joblib',
        'tqdm',
        'Pillow'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
