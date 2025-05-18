# 🤖 Smart Data Assistant — Metadata-Aware AI Assistant for Analytics

An open-source, end-to-end project that demonstrates how to build a smart assistant for querying and analyzing business data using natural language, powered by LangChain and enriched with metadata awareness via DataHub.

---

## 🔍 What This Project Does

- ✅ Ingests transactional sales data into a DuckDB database
- ✅ Registers metadata, table descriptions, and lineage in [DataHub](https://datahubproject.io/)
- ✅ Uses [LangChain](https://www.langchain.com/) to translate natural language into SQL
- ✅ Queries DuckDB and summarizes the result using an AI assistant (Streamlit interface)
- ✅ Suggests follow-up questions using data lineage and context

---

## 🗂 Project Structure

```plaintext
smart-data-assistant/
├── data/                   # Raw data (e.g., sales_data.csv)
├── pipeline/               # Python scripts for ingestion and transformation
├── assistant/              # LangChain + Streamlit chatbot app
├── metadata/               # Metadata setup and lineage registration
├── data_model/             # Star schema diagram and data model docs
├── requirements.txt        # All dependencies
├── .gitignore              # Ignore unnecessary files
└── README.md               # This file
