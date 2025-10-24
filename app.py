import streamlit as st
import pandas as pd
from io import StringIO
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load AI model
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

st.set_page_config(page_title="Cortexis Smart Assistant", page_icon="🤖")
st.title("🤖 Cortexis Smart Virtual Assistant")
st.markdown("---")

# FAQ Upload Section
st.header("📁 Upload Your Business FAQs")
uploaded_file = st.file_uploader("Choose a TXT file", type=['txt'])

if uploaded_file is not None:
    content = StringIO(uploaded_file.getvalue().decode()).read()
    
    # Parse FAQs
    lines = content.strip().split('\n')
    faqs = []
    current_q = ""
    current_a = ""
    
    for line in lines:
        if line.startswith('Q:'):
            if current_q:
                faqs.append((current_q.strip(), current_a.strip()))
            current_q = line[2:]
            current_a = ""
        elif line.startswith('A:') and current_q:
            current_a = line[2:]
    
    if current_q:
        faqs.append((current_q.strip(), current_a.strip()))
    
    st.success(f"✅ {len(faqs)} FAQs loaded successfully!")
    
    # Show sample FAQs
    st.subheader("📋 Your FAQs")
    for q, a in faqs[:3]:
        with st.expander(q):
            st.write(a)
    
    # Chat Section
    st.header("💬 Chat with Your Assistant")
    model = load_model()
    
    questions = [faq[0] for faq in faqs]
    question_embeddings = model.encode(questions)
    
    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask a question about your business..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Find best match
        user_embedding = model.encode([prompt])
        similarities = cosine_similarity(user_embedding, question_embeddings)[0]
        best_match_idx = np.argmax(similarities)
        best_answer = faqs[best_match_idx][1]
        confidence = similarities[best_match_idx]
        
               # Generate response - SMART KEYWORD CHECK
        weather_keywords = ['weather', 'temperature', 'rain', 'sunny', 'cloudy']
        order_keywords = ['order', 'buy', 'purchase', 'cart', 'payment']
        
        # Check for specific keywords
        prompt_lower = prompt.lower()
        is_weather = any(word in prompt_lower for word in weather_keywords)
        is_order = any(word in prompt_lower for word in order_keywords)
        
        if is_weather or is_order or confidence < 0.25:
            response = "❓ I'm not sure about that. Would you like me to connect you to an admin?"
        else:
            response = f"**Answer:** {best_answer}"
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

else:
    st.info("👆 Upload your FAQs first to start chatting!")
    st.markdown("**Example FAQ format:**")
    st.code("""
Q: What are your working hours?
A: We operate from 9 AM to 6 PM, Monday to Saturday.

Q: What is your main product?
A: Our main product is SmartWatch X.
    """)

st.markdown("---")
st.markdown("*Built by Hooria Kashif for Cortexis Solution Hub Internship*")