# Fine Tuning with Databricks

![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Jupyter Notebooks](https://img.shields.io/badge/notebooks-jupyter-orange.svg)
![License MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Databricks](https://img.shields.io/badge/platform-Databricks-red.svg)

Questo repository mostra come eseguire il fine-tuning di modelli LLM (Large Language Models) su Databricks, utilizzando sia il framework Trainer di HuggingFace Transformers che le tecniche QLoRA e LoRA per l'ottimizzazione efficiente dei modelli.

## Overview

Il progetto guida l’utente attraverso tutte le fasi del fine-tuning di un modello transformer su Databricks, dalla preparazione dell’ambiente e dei dati, fino al training e alla valutazione del modello. Sono incluse sia pipeline standard con Trainer che esempi di fine-tuning con QLoRA e LoRA.

---

## Step-by-step Notebook Guide

### 1. `00.setup.ipynb` — Setup iniziale

- **Crea lo schema Unity Catalog**: imposta lo spazio dati su Databricks per gestire i dataset e i modelli.
- **Crea i volumi UC**: prepara le aree di storage per file e dati temporanei.


> **Nota:** Lo spostamento dei file nel volume Unity Catalog deve essere effettuato manualmente tramite l'interfaccia Databricks o strumenti di upload, seguendo le policy di Databricks. I notebook non automatizzano questa operazione.

### 2. `01.import_data.ipynb` — Importazione e preparazione dati

- **Carica i dataset**: importa i file JSONL (train, validation, test) dai volumi UC.
- **Prepara i dati**: combina e trasforma i dataset, crea le etichette e normalizza i dati.
- **Salva come Delta Table**: esporta i dati preparati in formato Delta, ottimale per l’uso in Databricks e ML.

### 3. `02.fine_tuning_with_trainer.ipynb` — Fine-tuning del modello

- **Setup ambiente ML**: configura le librerie necessarie (Transformers, PyTorch, MLflow).
- **Carica i dati**: importa i dataset Delta.
- **Configura il modello**: imposta il modello base (es. BERT) e i parametri di training.
- **Esegui il fine-tuning**: addestra il modello sui dati preparati, sia con Trainer che con QLoRA/LoRA.
- **Valuta e salva**: misura le performance e registra il modello con MLflow.

### 4. `03.test_new_model.ipynb` — Test e valutazione

- **Importa librerie e dati**: carica MLflow, pandas, pyarrow e i dati dal volume UC.
- **Applica il modello**: usa il modello fine-tunato come UDF Spark per generare predizioni sui dati di test.
- **Visualizza risultati**: mostra le predizioni e confronta con le etichette reali.

---

## Come usare

1. Clona questo repository su Databricks o localmente.
2. Installa le dipendenze indicate in `requirements.txt`.
3. Segui i notebook in ordine per imparare e riprodurre il workflow di fine-tuning.

---

## Requisiti

- Account Databricks
- Python 3.8+
- HuggingFace Transformers, PyTorch, MLflow, e librerie ML comuni

---

## Note

Questi notebook sono pensati per uso didattico e sperimentale. Adattali alle tue esigenze prima di usarli in produzione.

---

Per domande o suggerimenti, apri una issue!