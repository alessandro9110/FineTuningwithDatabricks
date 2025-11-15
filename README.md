# Fine Tuning with Databricks

![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Jupyter Notebooks](https://img.shields.io/badge/notebooks-jupyter-orange.svg)
![License MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Databricks](https://img.shields.io/badge/platform-Databricks-red.svg)

This repository demonstrates how to fine-tune Large Language Models (LLMs) on Databricks using the HuggingFace Transformers Trainer framework. The project aims to include examples of fine-tuning with QLoRA and LoRA techniques for efficient model optimization.

> **Disclaimer:** The notebooks for fine-tuning with QLoRA and LoRA are not yet developed. This repository currently focuses on the setup, data preparation, and standard fine-tuning workflows.

---

## Overview

The project guides users through the following phases:

1. Environment setup on Databricks.
2. Data import and preparation.
3. Model fine-tuning using the HuggingFace Trainer framework.

---

## Step-by-step Notebook Guide

### 1. `00.setup.ipynb` — Initial Setup

- **Create Unity Catalog Schema**: Sets up the data space on Databricks to manage datasets and models.
- **Create UC Volumes**: Prepares storage areas for files and temporary data.

> **Note:** File transfer to the Unity Catalog volume must be done manually through the Databricks interface or upload tools, following Databricks policies. Notebooks do not automate this operation.

### 2. `01.import_data.ipynb` — Data Import and Preparation

- **Load datasets**: Imports JSONL files (train, validation, test) from UC volumes.
- **Prepare data**: Combines and transforms datasets, creates labels, and normalizes data.
- **Save as Delta Table**: Exports prepared data in Delta format, optimal for use in Databricks and ML workflows.

### 3. `02.fine_tuning_with_trainer.ipynb` — Model Fine-tuning

- **ML Environment Setup**: Configures necessary libraries (Transformers, PyTorch, MLflow).
- **Load data**: Imports Delta datasets.
- **Configure model**: Sets the base model (e.g., BERT) and training parameters.
- **Execute fine-tuning**: Trains the model on prepared data using the HuggingFace Trainer framework.
- **Evaluate and save**: Measures performance and logs the model with MLflow.

---

## How to Use

1. Clone this repository on Databricks or locally.
2. Install dependencies listed in `requirements.txt`.
3. Follow the notebooks in order to learn and reproduce the fine-tuning workflow.

---

## Requirements

- Databricks Account
- Python 3.8+
- HuggingFace Transformers, PyTorch, MLflow, and common ML libraries

## Cluster Configuration

The fine-tuning notebooks are designed to run on a Databricks cluster with the following configuration:

- **Spark Version**: 15.4.x-cpu-ml-scala2.12
- **Node Type**: Standard_D16ds_v5 (16 cores, 64 GB memory)
- **Driver Node Type**: Standard_D16ds_v5
- **Autotermination**: 60 minutes
- **Data Security Mode**: SINGLE_USER
- **Runtime Engine**: STANDARD
- **Cluster Mode**: Single Node (0 workers)

For optimal performance, ensure the cluster has sufficient resources for model training.

---

## Notes

These notebooks are intended for educational and experimental use. Adapt them to your needs before using in production.

---

For questions or suggestions, open an issue!
