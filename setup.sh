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




