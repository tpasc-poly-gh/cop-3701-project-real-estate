import os
import random

import numpy as np
import pandas as pd

os.makedirs("data", exist_ok=True)

df = pd.read_csv("Bengaluru_House_Data.csv")

locations = df['location'].dropna().unique()
location_df = pd.DataFrame({
    'location_id': range(len(locations)),
    'city': 'Bengaluru',
    'area_name': locations,
    'zipcode': np.random.randint(10_000, 50_000, len(locations))
})

df['location_id'] = df['location'].map(dict(zip(locations, location_df['location_id'])))
location_df.to_csv('data/location.csv', index=False)

property_df = pd.DataFrame({
    'property_id': range(len(df)),
    'price': df['price'],
    'size_sqft': df['total_sqft'],
    'property_type': df['area_type'],
    'year_built': np.random.randint(2000, 2023, len(df)),
    'status': df['availability'],
    'location_id': df['location_id'],
    'agent_id': np.random.randint(0, 100, len(df))
})
property_df.to_csv('data/property.csv', index=False)

features = []
fid = 1
i = 0
for _, row in df.iterrows():
    pid = i + 1
    for f_name in ['bath', 'balcony', 'society']:
        features.append([fid, pid, f_name, row[f_name]])
        fid += 1
    i += 1
feature_df = pd.DataFrame(features, columns=['feature_id', 'property_id', 'feature_name', 'feature_value'])
feature_df.to_csv('data/property_Feature.csv', index=False)

agent_df = pd.DataFrame({
    'agent_id': range(100),
    'name': [f'Agent_{i}' for i in range(100)],
    'license_number': [f'{i}' for i in range(100)],
    'phone': [f'{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9_999)}' for _ in
              range(100)],
    'email': [f'agent_{i}@gmail.com' for i in range(100)]
})
agent_df.to_csv('data/agent.csv', index=False)

buyer_df = pd.DataFrame({
    'buyer_id': range(100),
    'name': [f'Buyer_{i}' for i in range(100)],
    'contact_number': [f'{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9_999)}' for _ in
                       range(100)],
    'budget_range': [random.choice(['Low', 'Medium', 'High']) for _ in range(100)]
})
buyer_df.to_csv('data/buyer.csv', index=False)

transaction_df = pd.DataFrame({
    'transaction_id': range(len(property_df)),
    'sale_price': property_df['price'],
    'sale_date': [f"{random.randint(1, 12)}-{random.randint(1, 30)}-{random.randint(2000, 2025)}" for _ in
                  range(len(property_df))],
    'payment_type': [random.choice(['Cash', 'Loan']) for _ in range(len(property_df))],
    'property_id': property_df['property_id']
})
transaction_df.to_csv('data/transactions.csv', index=False)

purchase_df = pd.DataFrame({
    'purchase_id': range(len(property_df)),
    'purchase_date': [f"{random.randint(1, 12)}-{random.randint(1, 30)}-{random.randint(2000, 2025)}" for _ in
                      range(len(property_df))],
    'ownership_percentage': [float(random.randint(50, 100)) / 100. for _ in range(len(property_df))],
    'buyer_id': np.random.randint(0, 100, len(property_df)),
    'property_id': property_df['property_id']
})
purchase_df.to_csv('data/purchase.csv', index=False)

valuation_df = pd.DataFrame({
    'valuation_id': range(len(property_df)),
    'valuation_amount': property_df['price'] * np.random.randint(-10, 50),
    'valuation_date': [f"{random.randint(1, 12)}-{random.randint(1, 30)}-{random.randint(2000, 2025)}" for _ in
                       range(len(property_df))],
    'property_id': property_df['property_id']
})
valuation_df.to_csv('data/valuation.csv', index=False)
