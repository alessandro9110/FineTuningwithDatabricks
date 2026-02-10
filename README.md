# Fine Tuning with Databricks

![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Jupyter Notebooks](https://img.shields.io/badge/notebooks-jupyter-orange.svg)
![License MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Databricks](https://img.shields.io/badge/platform-Databricks-red.svg)

This repository demonstrates how to fine-tune Large Language Models (LLMs) on Databricks using the HuggingFace Transformers Trainer framework. The project includes examples of standard fine-tuning as well as parameter-efficient fine-tuning with LoRA and QLoRA techniques for efficient model optimization.

---

## Overview

The project guides users through the following phases:

1. Environment setup on Databricks.
2. Data import and preparation.
3. Model fine-tuning using the HuggingFace Trainer framework.
4. Parameter-efficient fine-tuning with LoRA.
5. Parameter-efficient fine-tuning with QLoRA.

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

### 4. `03.fine_tuning_with_lora.ipynb` — LoRA Fine-tuning

- **LoRA Configuration**: Sets up parameter-efficient fine-tuning using LoRA (Low-Rank Adaptation).
- **Reduced Parameters**: Fine-tunes only a small subset of parameters while freezing the base model.
- **Memory Efficient**: Requires significantly less memory and computational resources than full fine-tuning.
- **Load data**: Imports Delta datasets.
- **Execute training**: Trains LoRA adapters on prepared data.
- **Evaluate and save**: Merges adapters with base model and logs to MLflow.

### 5. `04.fine_tuning_with_qlora.ipynb` — QLoRA Fine-tuning

- **QLoRA Configuration**: Combines LoRA with 4-bit quantization for maximum efficiency.
- **4-bit Quantization**: Uses bitsandbytes library to quantize the base model to 4-bit precision.
- **Ultra Memory Efficient**: Enables fine-tuning of large models on limited GPU resources.
- **Load data**: Imports Delta datasets.
- **Execute training**: Trains QLoRA adapters on quantized model.
- **Evaluate and save**: Merges adapters, dequantizes for inference, and logs to MLflow.

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
