import boto3
import pandas as pd
from io import StringIO, BytesIO

aws_access_key_id = 'AKIASZSZ6RCERY2KJAFF'
aws_secret_access_key = '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'

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)
# Extract data from source
s3_client = session.client('s3')
bucket_name = 'fullstackdata2023'
source_path = 'common/data/full/full_transaction.csv'

def extract(bucket_name, source_path):
    # Get the object from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=source_path)
    # Read the CSV file content
    csv_string = StringIO(response['Body'].read().decode('utf-8'))
    # Use Pandas to read the CSV file
    df = pd.read_csv(csv_string)
    return df

def transform(df):
    # Transform transaction data into customer data
    customer_cols = ['customer_id', 'customer_name', 'customer_province']
    customer = df[customer_cols].drop_duplicates()
    return customer


# Load data into S3 bucket
def load(customer):
    my_name = 'domo-max'
    target_path = f'{my_name}/customer/customer.parquet'
    parquet_buffer = BytesIO()
    customer.to_parquet(parquet_buffer, index = False)
    s3_client.put_object(Bucket=bucket_name, Key=target_path, Body=parquet_buffer.getvalue())
    print("Upload success!")

def pipeline():
    df = extract(bucket_name, source_path)
    customer = transform(df)
    load(customer)

if __name__ == '__main__':
    pipeline()