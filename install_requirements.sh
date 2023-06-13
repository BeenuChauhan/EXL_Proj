#!/bin/bash

# this cmd will display the python verion intalled on the sytem(VM)
python --version
pip install --upgrade pip

# will install specific version of CLI (OR pip install azure-cli==2.0.69)
pip install azure-cli

#To install the Azure Databricks SDK and its CLI components to the latest version available
pip install --upgrade databricks-cli
# Azure ML SDK for Python
pip install azureml-sdk

#Python APIs for managing Databricks resources 
#programmatically, such as creating and managing workspaces, clusters, jobs, and notebooks.
pip install azure-mgmt-databricks
pip install msrest.authentication
pip install azure-devops
pip install azureml-core
pip install --upgrade azure-storage-blob

#The Azure Identity package provides authentication capabilities for interacting with Azure services securely. It is used for authenticating with Azure Databricks.
pip install azure-identity

# will refer the txt file and install all packages with specific verion
pip install -r requirements.txt
pip install miceforest
pip install -U imbalanced-learn
pip install azure-storage-blob --upgrade
pip install --upgrade seaborn
pip install --upgrade scikit-learn
pip install --upgrade statsmodels
pip install --upgrade imbalanced-learn


#By running this command, you will install the following packages:
#pytest: A testing framework for Python.
#requests: A package for making HTTP requests in Python.
#setuptools: A package that helps in packaging and distributing Python projects.
#wheel: A built-package format for Python, used for faster installation of packages.
#When you execute the command, pip will download the latest versions of these packages from the Python Package Index (PyPI) and install them on your system. These packages will be available for use in your Python projects or scripts.
pip install pytest requests setuptools wheel

# go to your databrick cluster to verify the number
pip install -U databricks-connect==12.2.*