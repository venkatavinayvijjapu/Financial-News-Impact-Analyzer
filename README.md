
# Financial News Impact Analyzer 🚀

Analyze how financial news influences market movements through an intelligent multi-agent system.

---

## 🔗 Live Demo  
Check out a quick demo walkthrough:  
https://www.veed.io/view/4212abdf-1d4c-44cb-868d-148649869feb?panel=share  

---

## 🧠 Project Overview

This project builds a **multi-agent pipeline** utilizing LLMs to:

1. **Extract** key financial data (tickers, events) from news articles  
2. **Assess sentiment** (positive / negative / neutral) with confidence scores  
3. **Predict market impact** (direction: up/down/neutral; and expected percent change)  
4. **Evaluate** prediction quality using rule-based and LLM-based assessments  

Inspired by similar systems seen in projects like Makireddyvighnesh’s Financial‑News‑Impact‑Analyzer :contentReference[oaicite:1]{index=1}.

---

## 🛠️ Folder Structure


/
├── agents/            # Each agent module: NewsEvent, Sentiment, Impact, Evaluation
├── data/              # Raw news article inputs
├── outputs/           # Prediction & evaluation results
├── main.py            # Entry point to orchestrate the pipeline
├── eval.py            # Scripts for evaluation metrics & LLM evaluation
├── requirements.txt   # Python dependencies
├── Report.pdf         # Project overview and evaluation results
└── LICENSE            # Apache‑2.0 license


---

## 🧩 Multi-Agent Breakdown

- **News Event Agent**:  
  Parses article text to identify stock tickers and financial events.

- **Sentiment Agent**:  
  Assigns sentiment labels and confidence scores based on article tone.

- **Impact Agent**:  
  Predicts whether the stock will move up/down/neutral and estimates magnitude.

- **Evaluation Agent**:  
  Optionally uses an LLM to rate the prediction quality alongside rule-based metrics.

---

## 📊 Evaluation Metrics

- **Direction Accuracy**: % of correctly predicted directions  
- **Average Confidence**: Trustworthiness of sentiment predictions  
- **LLM Evaluation Score**: Quality rating provided by LLM (optional)

---

## ⚙️ Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/venkatavinayvijjapu/Financial-News-Impact-Analyzer.git
   cd Financial-News-Impact-Analyzer

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional for ChatGPT/LLM evaluation)
   Set your OpenAI API key:

   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

---

## ▶️ How to Run

1. **Run the full pipeline**

   ```bash
   python main.py
   ```

2. **Perform evaluation**

   ```bash
   python eval.py
   ```

3. **Check outputs**

   * `outputs/` folder contains results in JSON or CSV format.
   * `Report.pdf` provides comprehensive run results and visualizations.

---

## 🛠 Troubleshooting & Tips

* LLM responses can sometimes be malformed JSON—added regex cleaning enhances reliability.
* When tickers aren’t found (e.g., general news), fallback to a default tag (like `overall`).
* Validate and clean agent outputs with pydantic schemas for consistent data formats.

---

## 👏 What Worked & What Didn’t

* ✅ **Worked well**: Multi-agent coordination for sentiment extraction and impact prediction
* ⚠️ **Had issues**: Inconsistent LLM output formats—resolved via parsing safeguards
* 🧩 **Fallback handling**: Ensures pipeline continuity even in edge cases

---


## 📞 Contact

Reach me out at venkatavinayvijjapu@gmail.com for any queries.
