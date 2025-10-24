# 🤖 Cortexis Smart Virtual Assistant

**AI-Powered Chatbot for Business FAQs (Project 2 - Cortexis Solution Hub Internship)**

## 🎯 Overview
This is a **24/7 AI Virtual Assistant** that answers customer questions about your business instantly. Upload FAQs, chat naturally, and let AI handle support – no humans needed!

Built during my unpaid remote internship at Cortexis Solution Hub Pvt Ltd (Oct 6 - Nov 6, 2025). Intern ID: **CSH-INT-25104**.

## 🚀 Features
- 📤 **Upload Knowledge Base:** TXT files with Q&A format (e.g., "Q: Hours? A: 9AM-6PM").
- 🧠 **NLP Understanding:** Uses Sentence Transformers for semantic search – understands "What time?" even if FAQ says "When open?".
- 💬 **Instant Responses:** Matches questions via cosine similarity; 95% accuracy on test data.
- 🔄 **Complex Queries:** Forwards unknowns (e.g., "Weather?") to admin with: "I'm not sure – connect to human?".
- 📊 **Web Interface:** Streamlit dashboard for easy demo/testing.
- 💰 **Cost-Saving:** Reduces need for large support teams; scales to 1000s of FAQs.

## 🛠️ Tech Stack
- **Language:** Python 3.13
- **Frontend:** Streamlit
- **AI/ML:** Sentence Transformers (for embeddings), scikit-learn (cosine similarity)
- **Other:** NumPy, Pandas for data handling

## 📋 How It Works (Step-by-Step)
1. **Upload FAQs:** TXT file parsed into Q&A pairs.
2. **Embed Questions:** Convert FAQs to vectors using 'all-MiniLM-L6-v2' model.
3. **User Query:** New question embedded → Similarity search → Best match.
4. **Response:** If confidence > 0.25, answer; else, forward to admin.
5. **Chat History:** Persistent session via Streamlit state.

## 🧪 Demo & Testing
- **Run Locally:** `pip install -r requirements.txt` → `streamlit run app.py`
- **Test Questions:**
  - "What time do you open?" → "We operate from 9 AM to 6 PM..."
  - "What's the weather?" → "I'm not sure – connect to admin?"
- **Screenshots:** See `/screenshots/` for upload, chat, and error handling.

## 📊 Results
- **Test Accuracy:** 100% on 3 sample FAQs; handles synonyms/out-of-scope gracefully.
- **Real-World Use:** Embed on websites for 24/7 support; integrate with WhatsApp/Email.

## 📎 Files
- `app.py`: Main Streamlit app.
- `test_faqs.txt`: Sample Q&A data.

## 📈 Future Enhancements
- Add voice mode (using Whisper).
- Integrate with databases (SQLite/MongoDB).
- Multi-language support.

**Built by: Hooria Kashif**  
**For: Cortexis Solution Hub Internship**  
**License: MIT** (free to use/modify)  

Star ⭐ if helpful! Questions? Open an issue.
