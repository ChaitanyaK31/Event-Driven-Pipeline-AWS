import pandas as pd
from datetime import datetime
import sys
from awsglue.utils import getResolvedOptions

args_list = ["bucket_name","file_prefix"]
params = getResolvedOptions(sys.argv, args_list)

bucket_name = params['bucket_name']
file_prefix = params['file_prefix']
source_s3_url = f"s3://{bucket_name}/{file_prefix}"

print("bucket_name:", bucket_name) 
print("file_prefix:", file_prefix) 
print("source_s3_url:", source_s3_url)

now = datetime.now()
formatted_datetime = int(now.strftime("%Y%m%d%H%M%S"))
target_s3_url = "s3://s3-projectedp-target/target/orders/"+str(formatted_datetime)+'.parquet'

print("target_s3_url:", target_s3_url)

df = pd.read_csv(source_s3_url)
print(df)

df.drop_duplicates(inplace = True)
df = df.reset_index(drop = True)
df.to_parquet(target_s3_url)