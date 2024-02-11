import urllib.request
import tarfile
import os
import subprocess
import platform
from keep_alive import keep_alive
import toml

keep_alive()

# Package URL
url = "https://assets.coreservice.io/public/package/66/gaganode_pro/0.0.300/gaganode_pro-0_0_300.tar.gz"
file_name = "gaganode_pro.tar.gz"
extracted_dir = "./gaganode_pro"

# Download the package
urllib.request.urlretrieve(url, file_name)

# Extract the package
with tarfile.open(file_name, "r:gz") as tar:
    tar.extractall(extracted_dir)

# Remove the downloaded archive
os.remove(file_name)

file_path = 'gaganode_pro/gaganode-linux-amd64/root_conf/default.toml'

# Read the existing TOML file
try:
    with open(file_path, 'r') as f:
        data = toml.load(f)
except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")
    # Handle the error or exit as needed

# Modify the data as needed
data['token'] = os.environ['mem']

# Write the modified data back to the TOML file
with open(file_path, 'w') as f:
    toml.dump(data, f)


print("Package downloaded and extracted successfully.")
#executable_path = os.path.join(extracted_dir)  # Adjust the path accordingly
subprocess.run(['gaganode_pro/gaganode-linux-amd64/gaganode'],shell=True)
