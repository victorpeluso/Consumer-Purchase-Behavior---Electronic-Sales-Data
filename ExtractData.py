import zipfile

# Define path to the downloaded file
zip_file_path = "C:/Users/alexp/PycharmProjects/ConsumerBehavior/electronic-sales-sep2023-sep2024.zip"
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall("C:/Users/alexp/PycharmProjects/ConsumerBehavior/data/")