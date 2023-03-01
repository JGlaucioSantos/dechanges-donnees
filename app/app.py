#!/home/renato/python/projeto-glaucio/.venv/bin/python3

import os

import requests
import pandas as pd
from sqlalchemy import create_engine

from dotenv import load_dotenv

load_dotenv()

# Retrieving data from the API

url_api = "https://my.api.mockaroo.com/open_job_posting_report.json?key=86a393a0"

try:
    req = requests.get(url_api, timeout=5)

    if req.status_code == 200:
        # request made successfully
        data = req.json()

    else:
        erro = req.raise_for_status()
        print(f"The following error occurred while accessing the API: {erro}")

except Exception as erro:
    print(f"The following error occurred in the request: {erro}")

# Structuring retrieved data

dataframe_offer_job = pd.DataFrame(data)

## data segmentation

#candidate_identification
dataframe_candidate_identification = (
    dataframe_offer_job[
        [
            "id_candidate",
            "candidate_first_name",
            "candidate_last_name",
            "gender"
        ]
    ]
)

#candidate_contact
dataframe_candidate_contact = (
    dataframe_offer_job[
        [
            "id_candidate",
            "candidate_email",
            "phone_number"
        ]
    ]
)

#candidate_location
dataframe_candidate_location = (
    dataframe_offer_job[
        [
            "id_candidate",
            "candidate_address",
            "postal_code",
            "city",
            "country",
            "code_country"
        ]
    ]
)

#job_information
dataframe_job_information = (
    dataframe_offer_job[
    [
        "id_candidate",
        "department",
        "job_title",
        "annual_salary"
        ]
    ]
)

#hiring_process
dataframe_hiring_process = (
    dataframe_offer_job
    [
        [
            "id_candidate",
            "position_type",
            "position_status",
            "poste_date",
            "hired_Date"
        ]
    ]
)

## database connection

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASS")
host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
database = os.getenv("MYSQL_DB")

try:
    db_connection = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    db_connection = create_engine(db_connection)

except Exception as erro:
    print(f"The following error occurred while creating the database connection:{erro}")

## write to the database

#candidate_identification
try:
    dataframe_candidate_identification.to_sql(
        con=db_connection,
        name="candidate_identification",
        if_exists="replace", #"append"
        index=False,
        chunksize=100
    )

except Exception as erro:
    print(f"An error occurred while writing table candidate_identification:{erro}")

#candidate_contact
try:
    dataframe_candidate_contact.to_sql(
        con=db_connection,
        name="candidate_contact",
        if_exists="replace", #"append"
        index=False,
        chunksize=100
    )

except Exception as erro:
    print(f"An error occurred while writing table candidate_contact:{erro}")

#candidate_location
try:
    dataframe_candidate_location.to_sql(
        con=db_connection,
        name="candidate_location",
        if_exists="replace", #"append"
        index=False,
        chunksize=100
    )

except Exception as erro:
    print(f"An error occurred while writing table candidate_location:{erro}")

#job_information
try:
    dataframe_job_information.to_sql(
        con=db_connection,
        name="job_information",
        if_exists="replace", #"append"
        index=False,
        chunksize=100
    )

except Exception as erro:
    print(f"An error occurred while writing table job_information:{erro}")

#hiring_process
try:
    dataframe_hiring_process.to_sql(
        con=db_connection,
        name="hiring_process",
        if_exists="replace", #"append"
        index=False,
        chunksize=100
    )

except Exception as erro:
    print(f"An error occurred while writing table hiring_process:{erro}")