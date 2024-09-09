# RFBGCPred: Random Forest-Based Tool for Predicting Biosynthetic Gene Clusters (BGCs)

**RFBGCPred** is a command-line tool for predicting Biosynthetic Gene Clusters (BGCs) from protein sequences. It uses a Random Forest classifier, Word2Vec embeddings, and UMAP dimensionality reduction to classify sequences into BGC classes, including **PKS**, **NRPS**, **RiPP**, **Terpenes**, and **Hybrid PKS-NRPS**.

## Features
- **Four input formats**: Supports single sequence input, FASTA, GenBank (GBK), and CSV files.
- **Confidence Score**: Provides a confidence score for each prediction.
- **Threshold Customization**: Set a confidence threshold to only output predictions above the threshold.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RFBGCPred.git
   cd RFBGCPred
