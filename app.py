import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import time
import json
import visuals as vis

# NLTK data downloads are omitted at runtime to ensure instant application loading
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

# Load the vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Page Configuration
st.set_page_config(
    page_title="SentinShield - AI Spam & Phishing Classifier",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Glassmorphic Styling from external style.css
try:
    with open('style.css', 'r') as f:
        custom_css = f.read()
    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)
except Exception:
    pass

# Session State initialization
if 'history' not in st.session_state:
    st.session_state.history = []

# Sidebar Panel Configuration
with st.sidebar:
    st.markdown(vis.draw_sidebar_header(), unsafe_allow_html=True)
    
    # Custom Control Panel
    st.markdown('<h3 style="color:#f1f5f9; font-weight:700; font-size:14px; margin-top:10px; text-transform: uppercase; letter-spacing:0.05em; color: #818cf8;">⚙️ Threat Control</h3>', unsafe_allow_html=True)
    cinematic_mode = st.toggle("Enable Cinematic Scan Delay", value=True, help="Adds a progressive scanning delay to visualize calculations.")
    show_diagnostics_detail = st.toggle("Show Diagnostic Insights", value=True, help="Shows extra qualitative evaluations of performance parameters.")
    
    # Session Log History
    st.markdown('<h3 style="color:#f1f5f9; font-weight:700; font-size:15px; margin-top:25px; border-bottom:1px solid rgba(255, 255, 255, 0.08); padding-bottom:10px;">🔍 Session Log</h3>', unsafe_allow_html=True)
    if not st.session_state.history:
        st.markdown('<p style="color:#64748b; font-size:13px; font-style:italic;">No messages analyzed yet.</p>', unsafe_allow_html=True)
    else:
        for item in st.session_state.history[:5]:
            tag_class = "spam" if item["result"] == "SPAM" else ("susp" if item["result"] == "SUSPICIOUS" else "ham")
            st.markdown(vis.draw_history_item(item, tag_class), unsafe_allow_html=True)

# Main Hero Header
st.markdown(vis.draw_hero_section(), unsafe_allow_html=True)

# Setup Navigation Tabs
tab1, tab2, tab3 = st.tabs(["💬 Spam Classifier", "📊 Model Diagnostics", "🛡️ Shield Center"])

# 💬 Tab 1: Spam Classifier
with tab1:
    col_left, col_right = st.columns([1.3, 0.7])
    
    with col_left:
        # Native header aligns perfectly at the top of the column with 0 whitespace gap
        st.markdown("### ✍️ Analyze Message Content")
        
        input_sms = st.text_area(
            "Enter your email or SMS message content here:",
            placeholder="Paste text here to inspect for malicious links, smishing templates, or generic spam...",
            height=200,
            label_visibility="collapsed"
        )
        
        # Real-time character & word counters
        words_count = len(input_sms.split())
        chars_count = len(input_sms)
        read_time = max(1, round((words_count / 200) * 60)) if words_count > 0 else 0
        
        # Render live text stats grid inside a fully closed card template
        st.markdown(vis.draw_stats_grid(chars_count, words_count, read_time), unsafe_allow_html=True)
        
        # High-risk Spam keywords inspection
        spam_keywords = ["free", "win", "claim", "money", "prize", "urgent", "cash", "offer", "alert", "verify", "winner", "reward", "billing", "account", "update", "bank", "credit", "card", "official", "limit", "security", "passcode"]
        found_keywords = [w for w in spam_keywords if f" {w}" in f" {input_sms.lower()}"]
        
        if found_keywords and input_sms.strip():
            st.markdown('<div style="margin-top: 15px; text-align: center;"><span style="font-size: 12px; color: #ef4444; font-weight:700; text-transform:uppercase; letter-spacing:0.05em;">⚠️ Spam Trigger Words Identified:</span></div>', unsafe_allow_html=True)
            badges = "".join([f'<span class="keyword-badge">{kw}</span>' for kw in found_keywords])
            st.markdown(f'<div class="badge-container">{badges}</div>', unsafe_allow_html=True)
        
        # Action button
        predict_clicked = st.button("Predict / Scan Content", key="predict_btn")
        
    with col_right:
        if predict_clicked and input_sms.strip():
            with st.spinner("Decoding threat vectors..."):
                if cinematic_mode:
                    time.sleep(0.7)  # Cinematic feedback delay
                
                transformed_sms = transform_text(input_sms)
                vector_input = tfidf.transform([transformed_sms])
                
                # Model outputs
                proba = model.predict_proba(vector_input)[0][1]
                
                # Categorize results
                if proba >= 0.7:
                    result_cat = "SPAM"
                elif proba >= 0.3:
                    result_cat = "SUSPICIOUS"
                else:
                    result_cat = "HAM"
                
                # Insert to session state history
                history_text = input_sms.strip()
                st.session_state.history.insert(0, {
                    "text": history_text[:40] + "..." if len(history_text) > 40 else history_text,
                    "proba": proba,
                    "result": result_cat
                })
            
            # Display Prediction Gauge in fully closed card template
            st.markdown('<div class="glass-card" style="text-align: center;"><h3 style="color:#ffffff; font-weight:700; margin-bottom:20px; margin-top:0px;">🔍 Analysis Report</h3>' + vis.draw_probability_gauge(proba) + vis.draw_result_banner(result_cat) + '</div>', unsafe_allow_html=True)
            
        elif predict_clicked and not input_sms.strip():
            st.warning("Please type or paste some text content to scan.")
        else:
            # Standby/Idle Right Panel inside a fully closed glass-card
            st.markdown(vis.draw_idle_standby(), unsafe_allow_html=True)

# 📊 Tab 2: Model Diagnostics
with tab2:
    # Native header aligns perfectly at the top of the tab
    st.markdown("## 📊 NLP Model Quality Metrics")
    st.markdown('<p style="color: #94a3b8; font-size: 14.5px; margin-bottom: 25px; margin-top:-5px;">Loaded directly from our training pipeline evaluations, verifying classifier stability across test data distributions.</p>', unsafe_allow_html=True)
    
    # Try loading metrics from metrics.json
    try:
        with open('metrics.json', 'r') as f:
            metrics = json.load(f)
    except Exception:
        metrics = {
            "accuracy": 0.970019,
            "precision": 1.0,
            "recall": 0.775362,
            "f1_score": 0.873469,
            "confusion_matrix": [[896, 0], [31, 107]]
        }
    
    # Metrics Grid inside fully closed card template
    st.markdown(vis.draw_diagnostics_grid(metrics), unsafe_allow_html=True)
    
    # Confusion Matrix Table inside fully closed card template
    cm = metrics["confusion_matrix"]
    st.markdown(vis.draw_confusion_matrix(cm), unsafe_allow_html=True)
    
    # Render diagnostics explanation inside closed block only if enabled
    if show_diagnostics_detail:
        st.markdown(vis.draw_diagnostics_insight(metrics, cm), unsafe_allow_html=True)

# 🛡️ Tab 3: Shield Center (Safe-Inbox Guidelines)
with tab3:
    st.markdown(vis.draw_shield_guidelines(), unsafe_allow_html=True)
