"""
config.py

This module contains configuration settings for the project. It centralizes various configuration parameters that
are used throughout the codebase. Sensible defaults are provided, and some values can be overridden using
environment variables.

Configuration Parameters:
- DB_HOST: The host name of the database server.
- DB_PORT: The port number for the database connection.
- DB_USER: The username for authenticating to the database.
- DB_PASSWORD: The password for authenticating to the database. Can be set as an environment variable.
- DB_NAME: The name of the database to connect to.
- API_KEY: API key for an external service. Can be set as an environment variable.
- DATA_PATH: The path to the directory containing data files.
- MODEL_PATH: The path to the directory for storing trained models.
- DEBUG_MODE: A boolean flag indicating whether the application is in debug mode.
- MAX_RESULTS: Maximum number of results to be processed.

Example Usage:
    import config

    db_connection_string = f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"

    api_key = config.API_KEY

    data_path = config.DATA_PATH

Note:
- To enhance security, sensitive values like passwords and API keys are recommended to be stored as environment variables.
"""
import os

# Database configuration
DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'myuser'
DB_PASSWORD = os.environ.get('DB_PASSWORD')  # Use environment variable for password
DB_NAME = 'mydatabase'
PROJECT_NAME = 'mlflow-101'

# API key for external service
API_KEY = os.environ.get('API_KEY')  # Use environment variable for API key

# File paths
DATA_PATH = '/path/to/data'
MODEL_PATH = '/path/to/models'

# Other configuration options
DEBUG_MODE = True
MAX_RESULTS = 100
