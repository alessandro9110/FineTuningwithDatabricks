# Databricks notebook source
import mlflow

# COMMAND ----------

# Install pyarrow if not already installed
%pip install pyarrow

import pyarrow.parquet as pq
import pandas as pd

# COMMAND ----------

# Read the Parquet file with pyarrow
table = pq.read_table("/Volumes/main/fine_tuning_transformer_model/files/cleaned_CrifSept-OctCases.parquet"
)
pdf = table.to_pandas()

# Convert pandas DataFrame to Spark DataFrame
df = spark.createDataFrame(pdf)

# COMMAND ----------

display(df)

# COMMAND ----------

df = df.select("Full Mail", "Level3 Category English Label").withColumnRenamed("Full Mail", "text").withColumnRenamed("Level3 Category English Label", "label")
df.display()

# COMMAND ----------

logged_model = f"runs:/b5d0c759e6c74f9a903e5da7841dda61/classification"

# Load model as a Spark UDF. Override result_type if the model does not return double values.
classification_class = mlflow.pyfunc.spark_udf(spark, model_uri=logged_model, result_type='string')

# COMMAND ----------

test = df.limit(10).select(df.text, df.label, classification_class(df.text).alias("prediction"))
display(test)

# COMMAND ----------

import mlflow.pyfunc

logged_model = f"runs:/b5d0c759e6c74f9a903e5da7841dda61/classification"

# Load your MLflow model as a Spark UDF
classification_udf = mlflow.pyfunc.spark_udf(
    spark,
    model_uri=logged_model,  # Update with your model URI
    result_type="string"  # Change to the correct type if needed
)

# COMMAND ----------

# Use the Spark UDF in your DataFrame transformation
test = (
    df.limit(9)
    .select(
        df.text,
        df.label,
        classification_udf(df.text).alias("prediction")
    )
)

display(test)

# COMMAND ----------

