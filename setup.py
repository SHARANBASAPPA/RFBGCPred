from setuptools import setup, find_packages

setup(
    name='RFBGCPred',
    version='1.0.0',
    authors='Your Name',
    author_email='smadival509@gmail.com',
    description='A Random Forest-Based Tool for Prediction of Biosynthetic Gene Clusters (BGCs)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/RFBGCPred',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['models/*.pkl', 'models/*.model'],   # Ensure this bracket is correct and closed here
    },
    install_requires=[
        'numpy',
        'gensim',
        'scikit-learn',
        'umap-learn',
        'biopython',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'rfbgcpred = rfbgcpred.cli:main',   # This closes correctly here
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
