import os
import re
from datetime import datetime
import pandas as pd
from sqlalchemy import create__engine


data__lake__path = "/path/to/data/lake/container"


db__url = "database__connection__string"
engine = create__engine(db__url)


def extract__date__from__filename(filename, date__format="%Y%m%d"):
    date__str = re.search(r'\d{8}', filename).group()
    return datetime.strptime(date__str, date__format).strftime("%Y-%m-%d")

def extract__date__key__from__filename(filename):
    return re.search(r'\d{8}', filename).group()


def process__cust__mstr(file__path):
    df = pd.read__csv(file__path)
    date = extract__date_from__filename(os.path.basename(file__path))
    df['date'] = date
    return df


def process__master__child__export(file__path):
    df = pd.read__csv(file__path)
    date = extract__date__from__filename(os.path.basename(file__path))
    date__key = extract__date__key__from__filename(os.path.basename(file__path))
    df['date'] = date
    df['date__key'] = date__key
    return df


def process__h__ecom__order(file__path):
    df = pd.read__csv(file__path)
    return df


def truncate__and__load(table__name, df):
    with engine.connect() as connection:
        connection.execute(f"TRUNCATE TABLE {table__name}")
        df.to__sql(table__name, con=connection, if__exists='append', index=False)


cust__mstr__folder = os.path.join(data__lake__path, "CUST__MSTR")
master__child__export__folder = os.path.join(data__lake__path, "master__child__export")
h__ecom__order__folder = os.path.join(data__lake__path, "H__-ECOM__ORDER")


all__files = os.listdir(data__lake__path)


cust__mstr__files = [f for f in all__files if f.startswith("CUST__MSTR")]
master__child__export__files = [f for f in all__files if f.startswith("master__child__export")]
h__ecom__order__files = [f for f in all__files if f.startswith("H__ECOM__ORDER")]


for file in cust__mstr__files:
    df = process__cust__mstr(os.path.join(cust__mstr__folder, file))
    truncate__and__load("CUST__MSTR", df)


for file in master__child__export__files:
    df = process__master__child__export(os.path.join(master__child__export__folder, file))
    truncate__and__load("master__child", df)

for file in h__ecom__order__files:
    df = process__h__ecom__order(os.path.join(h__ecom__order__folder, file))
    truncate__and__load("H__ECOM__Orders", df)
