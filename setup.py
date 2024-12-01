from setuptools import setup, find_packages

setup(
    name='po-translator',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'polib',
        'arabic-reshaper',
        'python-bidi',
        'tqdm==4.67.1'
    ],
    entry_points={
        'console_scripts': [
            'po-translate=po_translator.translate:main',
        ],
    },
    author='Abdelkhalek Saadani',
    author_email='abdelkhaleksaadani@gmail.com',
    description='A tool for translating PO files using translate-shell',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/po-translator',
    classifiers=[
        'Programming Language :: Python :: 3', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)