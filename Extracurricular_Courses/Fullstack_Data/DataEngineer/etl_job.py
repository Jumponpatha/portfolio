import boto3
import pandas as pd
from io import StringIO, BytesIO
from prefect import task, flow

# Extract data from source
s3_client = boto3.client('s3')
bucket_name = 'fullstackdata2023'
source_path = 'common/data/full/full_transaction.csv'

@task(retries=3)
def extract(bucket_name, source_path):
    # Get the object from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=source_path)
    # Read the CSV file content
    csv_string = StringIO(response['Body'].read().decode('utf-8'))
    # Use Pandas to read the CSV file
    df = pd.read_csv(csv_string)
    print(f"*** Extract df with {df.shape[0]} rows.")
    return df

# Transform transaction data into customer data
@task
def transform(df):
    customer_cols = ['customer_id', 'customer_name', 'customer_province']
    customer = df[customer_cols].drop_duplicates()
    print(f"*** Transform df to customer with {df.shape[0]} rows.")
    return customer


# Load data into S3 bucket
@task
def load(customer):
    my_name = 'domo-max'
    target_path = f'{my_name}/customer/customer.parquet'
    parquet_buffer = BytesIO()
    customer.to_parquet(parquet_buffer, index = False)
    print(f"Uploading to bucket {bucket_name}, at path {target_path} ")
    s3_client.put_object(Bucket=bucket_name, Key=target_path, Body=parquet_buffer.getvalue())
    print("Upload success!")

@flow(log_prints=True)
def pipeline():
    df = extract(bucket_name, source_path)
    customer = transform(df)
    load(customer)

if __name__ == '__main__':
    # pipeline()
    pipeline.serve(name="my_first_pipeline")
