import os
import json
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Ensure NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)  
    
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)

def main():
    print("Loading data...")
    # Load dataset
    df = pd.read_csv("spam.csv", encoding='latin-1')
    
    # Data cleaning
    df = df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], errors='ignore')
    df.rename(columns={'v1': 'target', 'v2': 'text'}, inplace=True)
    
    # Label encoding
    encoder = LabelEncoder()
    df['target'] = encoder.fit_transform(df['target'])
    
    # Drop duplicates
    df.drop_duplicates(keep='first', inplace=True)
    
    # Preprocessing
    print("Preprocessing text (this might take a minute)...")
    df['transformed_text'] = df['text'].apply(transform_text)
    
    # Load vectorizer and model
    print("Loading vectorizer and model...")
    with open('vectorizer.pkl', 'rb') as f:
        tfidf = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
        
    # Transform text using pre-trained vectorizer
    X = tfidf.transform(df['transformed_text']).toarray()
    y = df['target'].values
    
    # Replicate train/test split
    # Since train_test_split is deterministic with random_state=2, this matches the notebook exactly
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
    
    # Make predictions on the test set
    print("Running evaluation...")
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred).tolist()  # Convert numpy array to list for JSON serialization
    
    # Print metrics
    print("\n--- Evaluation Metrics ---")
    print(f"Accuracy:  {accuracy:.6f}")
    print(f"Precision: {precision:.6f}")
    print(f"Recall:    {recall:.6f}")
    print(f"F1 Score:  {f1:.6f}")
    print("Confusion Matrix:")
    print(conf_matrix)
    
    # Save to metrics.json
    metrics = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "confusion_matrix": conf_matrix
    }
    
    with open('metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)
        
    print("\nMetrics successfully saved to 'metrics.json'!")

if __name__ == "__main__":
    main()
