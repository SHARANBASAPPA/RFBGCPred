import pickle
import gensim
import numpy as np

# Global variables to store the models after loading
rf_model = None
label_encoder = None
umap_model = None
w2v_model = None
models_loaded = False

def load_models():
    """Load all pre-trained models and label encoders. Load only once."""
    global rf_model, label_encoder, umap_model, w2v_model, models_loaded
    if not models_loaded:
        # Load models only once
        with open('models/rf_model.pkl', 'rb') as rf_file, \
             open('models/label_encoder.pkl', 'rb') as le_file, \
             open('models/umap_model.pkl', 'rb') as umap_file:
            
            rf_model = pickle.load(rf_file)
            label_encoder = pickle.load(le_file)
            umap_model = pickle.load(umap_file)
        
        w2v_model = gensim.models.Word2Vec.load("models/w2v_model.model")
        models_loaded = True
        print("Models loaded successfully.")
    
    return rf_model, label_encoder, umap_model, w2v_model

def preprocess_sequence(sequence, w2v_model, umap_model):
    """Preprocess a given protein sequence using Word2Vec and UMAP."""
    embeddings = np.array([w2v_model.wv[aa] for aa in sequence if aa in w2v_model.wv])
    if len(embeddings) == 0:
        raise ValueError("No valid embeddings found for the provided sequence.")
    avg_embedding = np.mean(embeddings, axis=0)
    reduced_embedding = umap_model.transform([avg_embedding])
    return reduced_embedding

def predict_bgc(sequence, rf_model, w2v_model, umap_model, label_encoder, threshold=0.5):
    """Predict the BGC class for a given protein sequence with confidence score."""
    processed_input = preprocess_sequence(sequence, w2v_model, umap_model)
    probabilities = rf_model.predict_proba(processed_input)
    max_prob_index = np.argmax(probabilities)
    max_prob = probabilities[0][max_prob_index]
    
    if max_prob >= threshold:
        predicted_class = label_encoder.inverse_transform([max_prob_index])[0]
        return predicted_class, max_prob
    else:
        return None, max_prob

def predict_batch(sequences, threshold=0.5):
    """Predict labels for a batch of sequences, reusing models."""
    rf_model, label_encoder, umap_model, w2v_model = load_models()  # Ensure models are loaded
    predictions = []
    confidences = []
    
    for sequence in sequences:
        predicted_class, confidence = predict_bgc(sequence, rf_model, w2v_model, umap_model, label_encoder, threshold)
        predictions.append(predicted_class)
        confidences.append(confidence)
    
    return predictions, confidences
