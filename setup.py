from setuptools import setup, find_packages

setup(
    name='RFBGCPred',
    version='1.0.0',
    description='A Random Forest-Based Tool for Prediction of Biosynthetic Gene Clusters (BGCs)',
    author='Sharanbasappa Madival, Anu Sharma, Neeraj Budhlakoti, Krishna Kumar Chaturvedi, Ulavappa Angadi, B Pavana, Mohammad Farooqi, Sudhir Srivastava, Shivadarshan S Jirli, Girish Kumar Jha, Shesh Rai',
    author_email='smadival509@gmail.com, dwijesh.mishra@icar.gov.in',
    url='https://github.com/SHARANBASAPPA/RFBGCPred',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,  # Ensures package includes all necessary non-Python files
    package_data={
        '': ['models/*.pkl', 'models/*.model'],  # Include models in the package
    },
    install_requires=[
        'biopython>=1.81',  # For handling FASTA and GBK files
        'numpy>=1.21.0',
        'scikit-learn>=1.2.2',
        'pandas>=1.3.0',
        'joblib>=1.2.0',
        'tqdm>=4.64.0',
        'gensim>=4.0.0',  # For Word2Vec model
        'umap-learn>=0.5.1',  # For dimensionality reduction
    ],
    entry_points={
        'console_scripts': [
            'rfbgcpred=rfbgcpred.cli:main',  # Entry point to the CLI
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
