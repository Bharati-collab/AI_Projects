# Restaurant Concept Generator (Structured Output) 🍽️🤖

A Streamlit application that uses a Large Language Model (LLM) to generate a restaurant concept from a selected cuisine.  
Unlike basic text generation demos, this project returns **structured JSON output** that can be reliably parsed, stored, and used in downstream analytics.

---

## Why this project matters (AI + Analytics)
Most LLM demos produce free-form text that is hard to validate or analyze.  
This app enforces a **structured output contract (JSON)** so results are:
- machine-readable
- consistent
- easy to store (CSV/DB)
- ready for dashboards and reporting

---

## Features
✅ Streamlit UI with cuisine selection  
✅ LLM-powered restaurant name + tagline + menu item generation  
✅ **Structured JSON output** (schema-like keys)  
✅ JSON parsing with error handling  
✅ Optional “Show Raw JSON” checkbox (useful for recruiters/debugging)  
✅ Secure API key handling with `.env` (not committed to GitHub)

---

## Tech Stack
- **Python**
- **Streamlit**
- **LangChain**
- **OpenAI API**
- **python-dotenv**
- JSON parsing (`json.loads`)


## Project Structure

RestaurantNameGenerator/

- main.py
- langchainhelper.py
- requirements.txt
- README.md
- app_output.png

---


