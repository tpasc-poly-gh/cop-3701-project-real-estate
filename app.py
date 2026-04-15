import pandas as pd
import streamlit as st
import sqlite3

st.set_page_config(page_title="Real Estate Intel", layout="wide")
st.header("Real Estate Market Intelligence Database")

#connecting to the database
conn = sqlite3.connect("db/real_estate.db")

#sidebar filter options
st.sidebar.header("Filter Options")

#feature 2
min_price = st.sidebar.number_input("Min Price", value=0)
max_price = st.sidebar.number_input("Max Price", value=10000000)

min_size = st.sidebar.number_input("Min Size (sqft)", value=0)
max_size = st.sidebar.number_input("Max Size (sqft)", value=10000)

property_type = st.sidebar.text_input("Property Type")

#feature 4
zip_code = st.sidebar.text_input("Zip Code")
area_name = st.sidebar.text_input("Area Name")

#feature 5
agent_name = st.sidebar.text_input("Agent Name")

#feature 2
min_year = st.sidebar.number_input("Min Year Built", value=1900)
max_year = st.sidebar.number_input("Max Year Built", value=2025)

#feature 3
bath_min = st.sidebar.number_input("Min Baths", value=0)
balcony_min = st.sidebar.number_input("Min Balconies", value=0)
society = st.sidebar.text_input("Society Name")

#main query
#feature 1
#with all the sqls combined
query = """
SELECT 
    l.area_name,
    l.zipcode,
    p.status,
    p.price,
    p.size_sqft,
    p.property_type,
    p.year_built,
    a.name AS agent_name,
    GROUP_CONCAT(pf.feature_name || ': ' || pf.feature_value, ', ') AS features
FROM Property p
LEFT JOIN Property_Feature pf ON p.property_id = pf.property_id
LEFT JOIN Location l ON p.location_id = l.location_id
LEFT JOIN Agent a ON p.agent_id = a.agent_id
WHERE 
    p.price BETWEEN ? AND ?
    AND p.size_sqft BETWEEN ? AND ?
    AND p.year_built BETWEEN ? AND ?
    AND (p.property_type LIKE ? OR ? = '')
    AND (l.zipcode LIKE ? OR ? = '')
    AND (l.area_name LIKE ? OR ? = '')
    AND (a.name LIKE ? OR ? = '')
GROUP BY p.property_id
HAVING
    (? = 0 OR SUM(CASE WHEN pf.feature_name = 'bath' AND CAST(pf.feature_value AS REAL) >= ? THEN 1 ELSE 0 END) > 0)
    AND
    (? = 0 OR SUM(CASE WHEN pf.feature_name = 'balcony' AND CAST(pf.feature_value AS REAL) >= ? THEN 1 ELSE 0 END) > 0)
    AND
    (? = '' OR SUM(CASE WHEN pf.feature_name = 'society' AND pf.feature_value LIKE ? THEN 1 ELSE 0 END) > 0)
ORDER BY l.area_name;
"""
#running query
df = pd.read_sql_query(
    query,
    conn,
    params = (
    min_price, max_price,
    min_size, max_size,
    min_year, max_year,
    f"%{property_type}%", property_type,
    f"%{zip_code}%", zip_code,
    f"%{area_name}%", area_name,
    f"%{agent_name}%", agent_name,
    bath_min, bath_min,
    balcony_min, balcony_min,
    society, f"%{society}%"
    )
)

#display table
st.subheader("Available Property Listings")
st.dataframe(df)

#close connection
conn.close()