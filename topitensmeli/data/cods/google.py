import gspread 
import pandas as pd
from google.cloud import storage

# iniciando gspread
def get_dfs(credential_path=False,sheet_id=None,block=None,df=None,dfmeli=None):
    if credential_path!=False and sheet_id!=None:
        gs = gspread.oauth(credentials_filename=credential_path)
        # puxando worksheet
        worksheet = gs.open_by_key(sheet_id)
        # puxando sheet meli e shopee
        meli_sheet = worksheet.get_worksheet(1).get_all_values()
        shopee_sheet = worksheet.get_worksheet(2).get_all_values()
        return meli_sheet, shopee_sheet
         
    # gerando dfs
    if block==None:
        print('download meli')
        df_meli = dfmeli
        # df_meli = df_meli.sample(100,random_state=2) 
        print('download shopee')
        df_shopee = df

    return df_meli, df_shopee


def load_data_from_gcs(gcs_uri, data_type='csv', *args, **kwargs):
    # Read the data from GCS URI using pandas
    if data_type == 'csv':
        data = pd.read_csv(gcs_uri, *args, **kwargs)
    else:
        data = pd.read_excel(gcs_uri, *args, **kwargs)

    return data


def upload_dataframe_to_gcs(bucket_name, dataframe, remote_file_name, prefix=None, project_id=None):
    storage_client = storage.Client(project=project_id)

    bucket = storage_client.get_bucket(bucket_name)

    # Convert the DataFrame to CSV format
    csv_data = dataframe.to_csv(index=False).encode('utf-8')

    # Append the prefix to the remote file name
    if prefix:
        remote_file_name = prefix.rstrip('/') + '/' + remote_file_name

    # Create a blob with the specified name in the bucket
    blob = bucket.blob(remote_file_name)

    # Upload the CSV data to the blob
    blob.upload_from_string(csv_data, content_type='text/csv')

    print(f"DataFrame uploaded to GCS bucket: {bucket_name} as {remote_file_name}")
