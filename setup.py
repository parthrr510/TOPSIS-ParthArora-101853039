from distutils.core import setup
from os import path
# Reading the README.md file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="TOPSIS-ParthArora-101853039",
    packages = ['TOPSIS-ParthArora-101853039'],
    version = '0.5',
    license = 'MIT',
    description = 'This Package is for calculating the TOPSIS score and rank of a dataset and storing it in a result csv file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='parthrr510',
    author_email='parthrr510@gmail.com',
    url='https://github.com/parthrr510/TOPSIS-ParthArora-101853039.git',
    download_url='https://github.com/parthrr510/TOPSIS-ParthArora-101853039/archive/v_02.tar.gz',
    keywords=['TOPSIS','RANKING','DATAFRAME','MCDM'],
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)