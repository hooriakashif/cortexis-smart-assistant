# 🤖 Cortexis Smart Virtual Assistant

**AI-Powered Chatbot for Business FAQs (Project 2 - Cortexis Solution Hub Internship)**

## 🎯 Overview
This is a **24/7 AI Virtual Assistant** designed to answer customer questions about your business instantly. Upload FAQs via a TXT file, chat naturally, and let AI handle support—no humans required! Built during my unpaid remote internship at Cortexis Solution Hub Pvt Ltd (Oct 6 - Nov 6, 2025). Intern ID: **CSH-INT-25-6104**.

## 🚀 Features
- 📤 **Upload Knowledge Base:** Supports TXT files with Q&A format (e.g., "Q: Hours? A: 9AM-6PM").
- 🧠 **NLP Understanding:** Uses Sentence Transformers for semantic search to interpret questions like "What time?".
- 💬 **Instant Responses:** Delivers accurate answers based on cosine similarity matching.
- 🔄 **Complex Queries:** Forwards unknowns (e.g., "Weather?") to admin with: "I'm not sure – connect to human?".
- 📊 **Web Interface:** Powered by Streamlit for an interactive demo.

## 🛠️ Tech Stack
- **Language:** Python 3.13
- **Frontend:** Streamlit
- **AI/ML:** Sentence Transformers (embeddings), scikit-learn (cosine similarity)
- **Other:** NumPy, Pandas (data handling)

## 📋 How It Works (Step-by-Step)
1. **Upload FAQs:** Parse a TXT file into Q&A pairs.
2. **Embed Questions:** Convert FAQs to vectors using the 'all-MiniLM-L6-v2' model.
3. **User Query:** Match new questions via similarity search.
4. **Response:** Answer if confidence > 0.25; otherwise, forward to admin.
5. **Chat History:** Maintained via Streamlit session state.

## 🧪 Demo & Testing
- **Run Locally:** Install dependencies manually (e.g., `pip install streamlit sentence-transformers`) → `streamlit run app.py`.
- **Test Questions:**
  - "What time do you open?" → "We operate from 9 AM to 6 PM..."
  - "What's the weather?" → "I'm not sure – connect to admin?"

## 📊 Results
- **Test Accuracy:** 100% on 3 sample FAQs; handles synonyms/out-of-scope queries.
- **Real-World Use:** Ideal for website integration or 24/7 customer support.

## 📎 Files
- `app.py`: Main Streamlit application code.
- `test_faqs.txt`: Sample Q&A data for testing.

## 📈 Future Enhancements
- Add `requirements.txt` for easy setup.
- Include `screenshots/` folder with demo images.
- Implement voice mode or database integration.

**Built by: Hooria Kashif**  
**For: Cortexis Solution Hub Internship**  
**License: MIT** (free to use/modify)  

Star ⭐ if helpful! Questions? Open an issue.
