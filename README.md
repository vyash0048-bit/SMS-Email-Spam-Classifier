---
title: Email SMS Spam Classifier
emoji: 📱
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.57.0
app_file: app.py
pinned: false
---

# 📱 SMS & Email Spam Classifier

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![NLTK](https://img.shields.io/badge/NLTK-000000?style=for-the-badge&logo=nltk&logoColor=white)](https://www.nltk.org/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-orange?style=for-the-badge)](https://huggingface.co/spaces/YashAI07/Email_SMS_Spam_Classifier)

An end-to-end Machine Learning application that classifies SMS or Email messages as **Spam** or **Ham** (Not Spam) using Natural Language Processing (NLP) and a Multinomial Naive Bayes model.

---

## ✨ Features

- **Real-time Prediction:** Instant classification of text input.
- **NLP Preprocessing:** Automated text cleaning, tokenization, stopword removal, and stemming.
- **Modern UI:** Built with Streamlit for a clean and interactive user experience.
- **Robust Model:** Trained on the SMS Spam Collection dataset with high precision.

---

## 📊 Model Performance

The classifier is evaluated on the test split of the SMS Spam Collection dataset (using an 80/20 train/test split with a deterministic seed `random_state=2`). You can view the live runtime evaluation metrics stored in `metrics.json`.

| Metric | Value | Description |
| :--- | :---: | :--- |
| **Accuracy** | **97.00%** | Overall percentage of correctly classified messages. |
| **Precision** | **100.00%** | Percentage of predicted spam that is actually spam (zero false positives!). |
| **Recall** | **77.54%** | Percentage of actual spam messages correctly identified. |
| **F1-Score** | **87.35%** | Harmonic mean of precision and recall. |

### 🧩 Confusion Matrix
```
[[896,   0]   # Legitimate messages (Ham) - 100% correct
 [ 31, 107]]  # Spam messages             - 77.54% correct
```

> [!NOTE]
> Because spam filtering datasets are naturally imbalanced, **Precision** is the most critical metric. A precision of **100%** means that a legitimate message is **never** incorrectly flagged as spam (zero false positives), protecting the user from missing important emails/SMS.

---

## 🚀 Getting Started

### 📋 Prerequisites

Ensure you have Python installed. You will also need the following NLTK data:
- `punkt` (for tokenization)
- `stopwords` (for text cleaning)

### ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vyash0048-bit/SMS-Email-Spam-Classifier.git
   cd SMS-Email-Spam-Classifier
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # On Windows
   # source .venv/bin/activate # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

---

## 🧠 How it Works

1. **Text Preprocessing:** The input text is converted to lowercase, tokenized, and stripped of special characters/punctuation.
2. **Stemming:** Words are reduced to their root form (e.g., "running" -> "run") using the Porter Stemmer.
3. **Vectorization:** The processed text is converted into numerical data using a pre-trained **TF-IDF Vectorizer**.
4. **Classification:** A **Multinomial Naive Bayes** model predicts the probability of the message being spam.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Machine Learning:** Scikit-learn
- **NLP:** NLTK
- **Deployment:** Streamlit Cloud / Local Machine

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">Made with ❤️ by <a href="https://github.com/vyash0048-bit">Yash Vyas</a></p>
