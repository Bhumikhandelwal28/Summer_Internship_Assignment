# Databricks notebook source
def drop_nd_create_table(table_columns):
    for table_name, columns in table_columns.items():
      column_str = ",\n  ".join(columns)
      drop_sql = f"""
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
raw_table_info = defaultdict(list)
curated_table_info = defaultdict(list)
df = spark.read.table("default.newdata")
for row in df.collect():
    table_name = row["RawTableName"]
    col_name = row["Rawtablecol"]
    data_type = row["RawTableColDataType"]
    logic_value = row["Logic"]
    column_def = f"{col_name} {data_type}"
    raw_table_info[table_name].append(column_def)
    table_name = row["CuratedTableName"]
    col_name = row["Curatedtablecol"]
    data_type = row["CuratedTableColDataType"]
    column_def = f"{col_name} {data_type}"
    curated_table_info[table_name].append(column_def)
    
drop_nd_create_table(raw_table_info)
drop_nd_create_table(curated_table_info)


# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO USER VALUES("b231349","Bhumi"),("b231348","Chetan"),("b231347","Sani");
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM USER;

# COMMAND ----------

dbutils.widgets.text("process_name","Enter process name")
process_name=dbutils.widgets.get("process_name")
input_process_names=[name.strip() for name in process_name.split(",") if name.strip()]
filtered_df=df.filter(df.ProcessName.isin(input_process_names))
display(filtered_df)



# COMMAND ----------

row_table_name=df.select("RawTableName").distinct().collect()[0][0]
user_df=spark.read.table(row_table_name)
display(user_df)
filtered_df=user_df
for row in df.collect():
    logic=row["Logic"]
    if logic:
        filtered_df=filtered_df.filter(logic)
        display(filtered_df)
        if row['CuratedTableName']:
            filtered_df.write.insertInto(row['CuratedTableName'])
curated_table_name=df.select("CuratedTableName").distinct().collect()[0][0]
cur_user_df=spark.read.table(curated_table_name)
display(cur_user_df)



# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM default.curUser