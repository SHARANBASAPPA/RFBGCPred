#!/usr/bin/env python

import argparse
import csv
import json
import multiprocessing
from rfbgcpred.model_utils import load_models, predict_batch, predict_bgc
from Bio import SeqIO
from .sequence_extraction import extract_sequence_from_fasta, extract_sequence_from_gbk

# Step 1: Define the user input options
def process_input(option, input_file, output_type, output_file, threshold):
    """Process input based on user option (single, fasta, gbk, csv)."""
    rf_model, label_encoder, umap_model, w2v_model = load_models()  # Load models once

    if option == 'single':
        process_single_sequence(input_file, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold)
    elif option == 'fasta':
        process_fasta_file(input_file, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold)
    elif option == 'gbk':
        process_gbk_file(input_file, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold)
    elif option == 'csv':
        process_csv_file(input_file, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold)
    else:
        print("Invalid option selected.")

# Step 2: Handle single protein sequence prediction
def process_single_sequence(sequence, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold):
    """Process a single protein sequence and handle output."""
    predictions, confidences = predict_batch([sequence], rf_model, label_encoder, umap_model, w2v_model, threshold)
    results = [(predictions[0], confidences[0])]
    handle_output(results, output_type, output_file)

# Step 3: Handle multi-FASTA file prediction
def process_fasta_file(file_path, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold):
    """Process a multi-FASTA file for predictions."""
    sequences = extract_sequence_from_fasta(file_path)
    batch_predict(sequences, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold)

# Step 4: Handle GBK file prediction
def process_gbk_file(file_path, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold):
    """Process a GBK file, extracting protein sequences for prediction."""
    sequences = extract_sequence_from_gbk(file_path)
    batch_predict(sequences, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold)

# Step 5: Handle CSV file prediction
def process_csv_file(file_path, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold):
    """Process a CSV file with protein sequences."""
    sequences = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            sequences.append(row[0])  # Assuming first column is the sequence

    batch_predict(sequences, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold)

# Step 6: Batch prediction function
def batch_predict(sequences, output_type, output_file, rf_model, label_encoder, umap_model, w2v_model, threshold):
    """Process predictions in batches."""
    predictions, confidences = predict_batch(sequences, rf_model, label_encoder, umap_model, w2v_model, threshold)
    results = list(zip(predictions, confidences))
    handle_output(results, output_type, output_file)

# Step 7: Handle output based on user choice
def handle_output(results, output_type, output_file):
    """Handle the output based on user selection (console, csv, txt, json)."""
    if output_type == 'console':
        for prediction, confidence in results:
            print(f"Prediction: {prediction}, Confidence: {confidence}")
    
    elif output_type == 'csv':
        with open(output_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Prediction", "Confidence"])
            for prediction, confidence in results:
                writer.writerow([prediction, confidence])
        print(f"Results saved to {output_file}")
    
    elif output_type == 'txt':
        with open(output_file, 'w') as txt_file:
            for prediction, confidence in results:
                txt_file.write(f"Prediction: {prediction}, Confidence: {confidence}\n")
        print(f"Results saved to {output_file}")
    
    elif output_type == 'json':
        output_data = [{"Prediction": prediction, "Confidence": confidence} for prediction, confidence in results]
        with open(output_file, 'w') as json_file:
            json.dump(output_data, json_file, indent=4)
        print(f"Results saved to {output_file}")
    
    else:
        print("Invalid output type.")

# Command-line interface
def main():
    """Main function to handle user input and perform predictions."""
    parser = argparse.ArgumentParser(description='RFBGCPred - A Random Forest Based Tool for Prediction of Biosynthetic Gene Clusters')
    
    parser.add_argument('--option', required=True, choices=['single', 'fasta', 'gbk', 'csv'],
                        help='Input option: single protein, fasta file, gbk file or csv file.')
    parser.add_argument('--input', required=True, help='Input file path or sequence.')
    parser.add_argument('--output_type', required=False, choices=['console', 'csv', 'txt', 'json'], default='console',
                        help='Output option: console (default), csv, txt, or json.')
    parser.add_argument('--output_file', required=False, help='Output file path (for csv, txt, or json).')
    parser.add_argument('--threshold', type=float, default=0.5, help='Confidence threshold for predictions (default: 0.5)')

    args = parser.parse_args()

    # Check if output file is required
    if args.output_type in ['csv', 'txt', 'json'] and not args.output_file:
        parser.error("--output_file is required for csv, txt, or json output types.")
    
    process_input(args.option, args.input, args.output_type, args.output_file, args.threshold)

if __name__ == "__main__":
    main()
