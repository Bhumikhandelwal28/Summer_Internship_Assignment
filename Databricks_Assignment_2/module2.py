# Databricks notebook source
def drop_nd_create_table(table_columns):
    for table_name, columns in table_columns.items():
      column_str = ",\n  ".join(columns)
      drop_sql=f"""
      DROP TABLE IF EXISTS {table_name}
      """
      create_sql = f"""
      CREATE TABLE IF NOT EXISTS {table_name} (
        {column_str}
      )
      USING DELTA
      """
      spark.sql(drop_sql)
      print(f"Creating table: {table_name}")
      spark.sql(create_sql)


# COMMAND ----------

from collections import defaultdict
raw_table = defaultdict(list)
curated_table = defaultdict(list)
presentation_table = defaultdict(list)
df = spark.read.table("default.metadata")
for row in df.collect():
    table_name = row["RawTableName"]
    col_name = row["Rawtablecol"]
    data_type = row["RawTableColDataType"]
    column_def = f"{col_name} {data_type}"
    raw_table[table_name].append(column_def)
    table_name = row["CuratedTableName"]
    col_name = row["Curatedtablecol"]
    data_type = row["CuratedTableColDataType"]
    column_def = f"{col_name} {data_type}"
    curated_table[table_name].append(column_def)
    table_name = row["PresentationTableName"]
    col_name = row["Presentationtablecol"]
    data_type = row["PresentationTableColDataType"]
    column_def = f"{col_name} {data_type}"
    presentation_table[table_name].append(column_def)

    #calling function for creating tables
    drop_nd_create_table(raw_table)
    drop_nd_create_table(curated_table)
    drop_nd_create_table(presentation_table)



# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE User;
# MAGIC