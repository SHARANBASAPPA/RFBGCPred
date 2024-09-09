# **RFBGCPred: Random Forest-Based Tool for Predicting Biosynthetic Gene Clusters (BGCs)**

**RFBGCPred** is a command-line tool for predicting Biosynthetic Gene Clusters (BGCs) from protein sequences. It uses a Random Forest classifier, Word2Vec embeddings, and UMAP dimensionality reduction to classify sequences into BGC classes, including **PKS**, **NRPS**, **RiPP**, **Terpenes**, and **Hybrid PKS-NRPS**.

## Features
- **Four input formats**: Supports single sequence input, FASTA, GenBank (GBK), and CSV files.
- **Confidence Score**: Provides a confidence score for each prediction.
- **Threshold Customization**: Set a confidence threshold to output only predictions above the threshold.
- **Fast Parallel Processing**: Optimized for quick batch processing through parallel execution.
  
## Installation

### Prerequisites
- **Python 3.9+**
- **Required Packages**:
  - `numpy`
  - `pandas`
  - `gensim`
  - `scikit-learn`
  - `umap-learn`
  - `biopython`

### Steps to Install

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SHARANBASAPPA/RFBGCPred.git
   cd RFBGCPred
2. **Install Dependencies: You can install the required dependencies using pip**:
     ```bash
   pip install -r requirements.txt
3. **Run the Setup (Optional): If you'd like to install the tool as a command-line tool, you can run the following command**:
     ```bash
   pip install .

### Steps to Install

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SHARANBASAPPA/RFBGCPred.git
   cd RFBGCPred
2. **Install Dependencies: You can install the required dependencies using pip**:
   pip install -r requirements.txt
3. **Run the Setup (Optional): If you'd like to install the tool as a command-line tool, you can run the following command**:
   pip install .

**Running Predictions**
1. **Single Sequence Input**
    You can predict the BGC class for a single protein sequence by passing it directly through the command line:
     ```bash
    rfbgcpred 'MKKLLLLLLPLLLALLLTPGSRHGLDVLPGAGSSLEVTSPQ' --format sequence --threshold 0.7

2. **FASTA Input**
    To predict BGCs from a FASTA file:
     ```bash
    rfbgcpred input_sequences.fasta --format fasta --threshold 0.7

3. **GenBank (GBK) Input**
    For predicting BGC classes from GenBank files:
     ```bash
    rfbgcpred input_sequences.gbk --format gbk --threshold 0.7

4. **CSV Input**
   For predictions from a CSV file (with a column named "sequence"):
    ```bash
   rfbgcpred input_sequences.csv --format csv --threshold 0.7

**Citation**
If you use RFBGCPred in your research, please cite the following paper:

RFBGCPred: A Random Forest Based Tool for Prediction of Biosynthetic Gene Clusters
Sharanbasappa D Madival, Dwijesh Chandra Mishra, Krishna Kumar Chaturvedi, Anu Sharma, Neeraj Budhlakoti, Ulavappa B Angadi, Pavana B, Mohammad Samir Farooqi, Sudhir Srivastava, Girish K. Jha, and Shesh N. Rai.

