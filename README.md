```markdown
# RFBGCPred: A Random Forest-Based Tool for Prediction of Biosynthetic Gene Clusters

It provides various input format support, including protein sequences, FASTA/Multi-FASTA files, GenBank (GBK) files, and CSV files containing protein sequences. The tool is designed to work efficiently by loading models lazily and supports multiple output formats such as console, CSV, TXT, and JSON.

## Features
- **Input Format Support**:
  - **Single protein sequence**: Directly input a single protein sequence for prediction.
  - **FASTA/Multi-FASTA file**: Predict BGCs from a nucleotide sequence file (FASTA).
  - **GenBank (GBK) file**: Extract protein sequences from GenBank files and predict BGCs.
  - **CSV file**: Input a CSV file containing protein sequences for batch predictions.
  
- **Output Options**:
  - **Console**: Output the predictions directly to the terminal (default).
  - **CSV**: Save predictions as a CSV file.
  - **TXT**: Save predictions as a plain text file.
  - **JSON**: Save predictions in a structured JSON format.

- **Lazy Model Loading**: Models are loaded only once to optimize memory usage and reduce computation time.
- **Batch Processing**: Processes sequences in batches for improved speed when working with large datasets.


## Installation

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-repo/rfbgcpred.git
cd rfbgcpred
```

### 2. Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies cleanly:

```bash
python -m venv rfbgcpred_env
source rfbgcpred_env/bin/activate  # For Linux/macOS
rfbgcpred_env\Scripts\activate  # For Windows
```

### 3. Install Dependencies

You can install all required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Install the Tool

Once dependencies are installed, you can install the package using the following command:

```bash
python setup.py install
```

### 5. Deactivate the Virtual Environment (Optional)

After usage, you can deactivate the virtual environment:

```bash
deactivate
```



## Usage

RFBGCPred provides several options for input and output. You can specify the input type (single sequence, FASTA, GBK, or CSV) and the output format (console, CSV, TXT, or JSON).

### Command-Line Usage:

```bash
rfbgcpred --option {single,fasta,gbk,csv} --input <input_file_or_sequence> [--output_type {console,csv,txt,json}] [--output_file <file_path>]
```

### Input Options:

1. **Single Protein Sequence**:
   - `--option single`: Predict BGC from a single protein sequence.
   
   Example:
   ```bash
   rfbgcpred --option single --input "MVLSPADKTNIK"
   ```

2. **FASTA or Multi-FASTA File**:
   - `--option fasta`: Use this option for FASTA files containing nucleotide sequences.
   
   Example:
   ```bash
   rfbgcpred --option fasta --input sequences.fasta --output_type csv --output_file predictions.csv
   ```

3. **GenBank (GBK) File**:
   - `--option gbk`: Use this option to extract protein sequences from GBK files.
   
   Example:
   ```bash
   rfbgcpred --option gbk --input data.gbk --output_type txt --output_file results.txt
   ```

4. **CSV File**:
   - `--option csv`: Use this option to input a CSV file containing protein sequences.
   
   Example:
   ```bash
   rfbgcpred --option csv --input sequences.csv --output_type json --output_file results.json
   ```

### Output Options:

1. **Console** (default):
   - Output predictions directly to the console.

   Example:
   ```bash
   rfbgcpred --option single --input "MVLSPADKTNIK"
   ```

2. **CSV**:
   - Save predictions to a CSV file.

   Example:
   ```bash
   rfbgcpred --option csv --input sequences.csv --output_type csv --output_file predictions.csv
   ```

3. **TXT**:
   - Save predictions to a plain text file.

   Example:
   ```bash
   rfbgcpred --option gbk --input data.gbk --output_type txt --output_file results.txt
   ```

4. **JSON**:
   - Save predictions to a structured JSON file.

   Example:
   ```bash
   rfbgcpred --option csv --input sequences.csv --output_type json --output_file results.json
   ```

## Example Workflows

### 1. **Single Protein Sequence (Console Output)**:
```bash
rfbgcpred --option single --input "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQANNL"
```
This will predict the BGC class of a single protein sequence and print the results to the console.

### 2. **FASTA File (Save to CSV)**:
```bash
rfbgcpred --option fasta --input sequences.fasta --output_type csv --output_file predictions.csv
```
This will process all the sequences in a FASTA file and save the predictions in a CSV file.

### 3. **GBK File (Save to TXT)**:
```bash
rfbgcpred --option gbk --input data.gbk --output_type txt --output_file results.txt
```
This will extract protein sequences from a GBK file, predict BGCs, and save the results to a text file.

### 4. **CSV File (Save to JSON)**:
```bash
rfbgcpred --option csv --input sequences.csv --output_type json --output_file results.json
```
This will predict BGCs from a CSV file and save the results in JSON format.


## Dependencies
The following dependencies are required and can be installed via the `requirements.txt` file:
- `python>=3.9`: As all the models were developed under this environment.
- `biopython>=1.81`: For handling FASTA and GBK files.
- `numpy>=1.21.0`: For numerical computations.
- `scikit-learn>=1.2.2`: For machine learning model usage.
- `pandas>=1.3.0`: For handling CSV files.
- `joblib>=1.2.0`: For model serialization and parallel processing.
- `tqdm>=4.64.0`: For progress bars in long-running processes.
- `gensim>=4.0.0`: For Word2Vec model processing.

### Installing Dependencies:

```bash
pip install -r requirements.txt
```


## Best Practices

- **Use a Virtual Environment**: Always create a virtual environment for installing the dependencies and running the tool to avoid conflicts with other packages in your system.
- **Error Handling**: The tool includes error handling for invalid input types or formats. Make sure the input data is correctly formatted.
- **Security**: Keep your dependencies updated to avoid any security vulnerabilities. Use the latest versions specified in the `requirements.txt` file.



## License

This project is done as part of PhD work of Dr. Sharanbasappa under the chairmanship of Dr. Dwijesh Chandra Mishra. 
This work is holds all the copyright @ICAR-Indian Agricultural Statistics Research Institute, New Delhi, INDIA.

