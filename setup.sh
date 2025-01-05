#!/bin/bash

# Create the Streamlit configuration directory
mkdir -p ~/.streamlit/

# Create the Streamlit configuration file
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
" > ~/.streamlit/config.toml

# Install Python dependencies
pip install py7zr

# Python script to extract and load similarity.7z and its .pkl file
python - <<EOF
import py7zr
import pickle

# Path to the .7z file
seven_z_file = "similarity.7z"

# Extract the .7z file
with py7zr.SevenZipFile(seven_z_file, mode='r') as archive:
    archive.extractall(path="extracted_files")  # Extracts to the specified directory

# Path to the extracted .pkl file
pkl_file_path = "similarity.pkl"  # Adjust if the .pkl file has a different name

EOF

