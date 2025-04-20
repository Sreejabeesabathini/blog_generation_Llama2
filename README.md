# 📝 AI Blog Generator using LLaMA 2

This project is a **Streamlit-based web application** that generates professional blog content using the **LLaMA 2** language model. It allows users to input a topic, choose a target audience, and receive a structured blog post that ends with a clean and meaningful conclusion.

---

## 🚀 Features

- ✅ Topic-based blog generation using LLaMA 2
- ✅ Profession-specific writing style (e.g. Researchers, Freshers, etc.)
- ✅ Approximate word control (e.g. 300 words, no cutoff)
- ✅ Automatically trims incomplete or awkward endings
- ✅ User-friendly interface built with Streamlit
- ✅ Local `.bin` model integration using CTransformers

---

## 📦 Installation

1. Clone the Repository
git clone https://github.com/yourusername/ai-blog-generator.git
cd ai-blog-generator

3. Install Required Packages
pip install -r requirements.txt

Or manually install:
pip install streamlit langchain ctransformers

🧠 Model Setup
This project uses a locally hosted LLaMA 2 model in .bin format, compatible with CTransformers.
Update the model path in app.py to match your local setup:
model=r'D:\your\local\path\llama-2-7b-chat.ggmlv3.q8_0.bin'
Make sure your system has sufficient RAM/CPU to handle large language models locally.

▶️ Running the App
In the project directory, run:
streamlit run app.py
Then open your browser and go to http://localhost:8501

✨ How It Works
Enter a topic like “Linear Regression”

Choose your audience style (e.g., Freshers)

Specify a word count (e.g., 300)

Click Generate and receive a structured blog that ends cleanly

📁 File Structure
├── app.py               # Streamlit app with LLaMA integration
├── README.md            # Project instructions and overview
├── requirements.txt     # Python dependencies
└── models/              # Folder where your local .bin model lives

🛠 Technologies Used
Streamlit – for UI
LangChain – LLM orchestration
CTransformers – for LLaMA 2 .bin support
LLaMA 2 – language model by Meta


