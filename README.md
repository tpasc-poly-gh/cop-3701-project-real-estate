# Real Estate Market Intelligence Database

## Scope:
- Storing housing prices, and property features
- Location based indexing
- Trends in housing prices over time

## Targeted Users:
- Real Estate Agents
- Real Estate Development Companies

## Data Sources:
- Kaggle Bengaluru House Price Data (https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)

## Entities
- Property (strong entity)  
- Location (strong entity)  
- Agent (strong entity)  
- Buyer (strong entity)  
- Transaction (weak entity)  
- Purchase (associative entity)  
- Property_Feature (associative entity)  
- Valuation  

## Relationships
- One-to-many: Location -> Property, Agent -> Property, Property -> Transaction  
- Many-to-many: Buyer <-> Property  
- One-to-one: Property - Valuation  

## Attributes
- Identifier: property_id, agent_id  
- Mandatory: price, size_sqft  
- Optional: year_built, email  
- Single-value: price  

## User Groups
- Real Estate Agents  
- Development Companies  
- Market Analysts  
- Property Investors  
