#!/usr/bin/env python

import argparse
import pandas as pd
import multiprocessing
from .sequence_extraction import extract_sequence_from_fasta, extract_sequence_from_gbk
from .model_utils import load_models, predict_bgc

def process_sequence(sequence, rf_model, w2v_model, umap_model, label_encoder, threshold):
    """ Function to process each sequence in parallel. """
    predicted_bgc_class, confidence = predict_bgc(sequence, rf_model, w2v_model, umap_model, label_encoder, threshold)
    if predicted_bgc_class:
        return f"Predicted BGC class for sequence: {predicted_bgc_class} with confidence: {confidence:.2f}"
    else:
        return f"Prediction confidence {confidence:.2f} is below the threshold {threshold}. No class assigned."

def main():
    """ Main function to handle user input and perform predictions. """
    parser = argparse.ArgumentParser(
        description="RFBGCPred: A Random Forest Based CLI Tool for Prediction of Biosynthetic Gene Clusters from protein sequences."
    )
    
    parser.add_argument('input', type=str, help='The input file (FASTA/GBK/CSV) or sequence for prediction')
    parser.add_argument('--format', choices=['fasta', 'gbk', 'csv', 'sequence'], required=True, help='Input type (FASTA, GBK, CSV, or single sequence)')
    parser.add_argument('--threshold', type=float, default=0.5, help='Confidence threshold for predictions (default is 0.5)')
    args = parser.parse_args()

    # Load pre-trained models only once
    rf_model, label_encoder, umap_model, w2v_model = load_models()

    # Handle input formats
    if args.format == 'fasta':
        sequences = extract_sequence_from_fasta(args.input)
    elif args.format == 'gbk':
        sequences = extract_sequence_from_gbk(args.input)
    elif args.format == 'csv':
        sequences = read_sequences_from_csv(args.input)
    elif args.format == 'sequence':
        sequences = [args.input]

    # Use multiprocessing to predict for multiple sequences
    with multiprocessing.Pool() as pool:
        results = pool.starmap(
            process_sequence, 
            [(seq, rf_model, w2v_model, umap_model, label_encoder, args.threshold) for seq in sequences]
        )

    for result in results:
        print(result)

if __name__ == '__main__':
    main()
