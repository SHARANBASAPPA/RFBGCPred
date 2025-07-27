
# RFBGCPred

**RFBGCPred** is a Random Forest-based tool for predicting Biosynthetic Gene Clusters (BGCs).  
This version is fully open-source under MIT License and includes trained models for direct use.

## Features
- Supports multiple input formats:
  1. FASTA (`.fasta`)
  2. GenBank (`.gbk` / `.genbank`)
  3. CSV (must contain a `Sequence` column)
- Includes pre-trained models (no training required).
- Automatically handles UMAP compatibility issues by using a fallback to RF if necessary.

## Installation
Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the tool using any supported input file:
```bash
python run_RFBGCPred.py --input data/example.fasta --output results_fasta.csv
python run_RFBGCPred.py --input data/example.gbk --output results_gbk.csv
python run_RFBGCPred.py --input data/example.csv --output results_csv.csv
```

## Output
- A CSV file containing:
  - `ID`: sequence identifier
  - `Prediction`: predicted BGC class

## License
MIT License. You are free to use, modify, and share.
