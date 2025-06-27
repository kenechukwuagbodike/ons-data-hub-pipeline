# ONS Data Hub Pipeline

A hands-on project designed to simulate a real-world Civil Service data engineering challenge, based on the essential requirements for a **Senior Data Engineer (SEO)** at the **Office for National Statistics (ONS)**.

## 📌 Project Summary
This pipeline ingests survey-style data, performs validation and transformation, and loads it into a cloud warehouse for analyst use. It mirrors distributed data processing practices and uses Python, Apache Airflow, and Google Cloud Platform (GCP).

It demonstrates core Civil Service data engineering expectations:
- Designing, writing, and operating ETL pipelines
- Writing clean, documented code in Python
- Using Git-based version control and CI/CD
- Creating reusable, testable, distributed data workflows

## 🧱 Architecture Overview

```
Cloud Storage (CSV files)
    |
    v
[Airflow DAG]
    |
    |-- extract.py   (Pull raw files)
    |-- validate.py  (Check schema, data types)
    |-- transform.py (Clean and reshape)
    |-- load.py      (Write to BigQuery)
    |
    v
BigQuery (Analyst-Ready Tables)
```

A flowchart version of this is available in `docs/flowchart.drawio`.

## 🔧 Tech Stack
- **Python 3.10**
- **Apache Airflow** (Local or Cloud Composer)
- **Google Cloud Platform**: Cloud Storage + BigQuery
- **Git + GitHub** (version control, branches)
- **Pytest** (unit and integration testing)
- **Markdown + diagrams.net** (documentation)

## 📁 Folder Structure
- `dags/` – Airflow DAG definition
- `scripts/` – Python modules for each pipeline stage
- `tests/` – Pytest files
- `docs/` – Markdown docs + flow diagrams
- `notebooks/` – SQL validation or exploration

## ✅ Features Delivered
| Capability | Demonstration |
|------------|----------------|
| ETL in distributed systems | Airflow DAG with modular Python stages |
| Clean code with standards | Docstrings, PEP8, comments, function modularity |
| Git version control | Branching strategy, commits, GitHub repo |
| GCP data engineering | Ingestion → Validation → Transformation → Load to BigQuery |
| Flowchart & Testing | DAG diagram + pytest scripts |
| Reusability & Clarity | Config-driven, documented, readable codebase |

## 🚀 How to Run (Dev Version)
1. Clone the repo: `git clone ...`
2. Create virtual environment: `python -m venv venv && source venv/bin/activate`
3. Install deps: `pip install -r requirements.txt`
4. Run DAG with Airflow or simulate in local script mode

> NOTE: A simulated version using local files (vs GCP) is also available for portability.

## 👨‍⚖️ Civil Service Relevance
This project explicitly targets the following ONS essential skills:
- ✅ ETL design in distributed systems
- ✅ Python code quality and documentation
- ✅ Git versioning and modular workflow
- ✅ GCP development
- ✅ Testing and pipeline robustness

It can be used as:
- A STAR example for interviews
- A GitHub showcase
- A learning tool to build data engineering fluency

---

Feel free to fork or adapt this to your own department's context.

📩 For questions or collaborations, contact: [kene.o.agbodike@gmail.com](mailto:kene.o.agbodike@gmail.com)
