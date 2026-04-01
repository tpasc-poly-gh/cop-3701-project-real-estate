PRAGMA foreign_keys = ON;

--DROP TABLE IF EXISTS Valuation;
--DROP TABLE IF EXISTS Purchase;
--DROP TABLE IF EXISTS Transactions;
--DROP TABLE IF EXISTS Property_Feature;
--DROP TABLE IF EXISTS Property;
--DROP TABLE IF EXISTS Buyer;
--DROP TABLE IF EXISTS Agent;
--DROP TABLE IF EXISTS Location;

CREATE TABLE Location (
    location_id INTEGER PRIMARY KEY,
    city TEXT NOT NULL,
    area_name TEXT NOT NULL,
    zipcode TEXT
);

CREATE TABLE Agent (
    agent_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    license_number TEXT UNIQUE NOT NULL,
    phone TEXT,
    email TEXT
);

CREATE TABLE Buyer (
    buyer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    contact_number TEXT,
    budget_range TEXT
);

CREATE TABLE Property (
    property_id INTEGER PRIMARY KEY,
    price REAL NOT NULL,
    size_sqft REAL NOT NULL,
    property_type TEXT NOT NULL,
    year_built INTEGER,
    status TEXT,
    location_id INTEGER,
    agent_id INTEGER,
    FOREIGN KEY (location_id) REFERENCES Location(location_id),
    FOREIGN KEY (agent_id) REFERENCES Agent(agent_id)
);

CREATE TABLE Property_Feature (
    feature_id INTEGER PRIMARY KEY,
    property_id INTEGER,
    feature_name TEXT,
    feature_value TEXT,
    FOREIGN KEY (property_id) REFERENCES Property(property_id)
);

CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY,
    sale_price REAL NOT NULL,
    sale_date TEXT,
    payment_type TEXT,
    property_id INTEGER,
    FOREIGN KEY (property_id) REFERENCES Property(property_id)
);

CREATE TABLE Purchase (
    purchase_id INTEGER PRIMARY KEY,
    purchase_date TEXT,
    ownership_percentage REAL,
    buyer_id INTEGER,
    property_id INTEGER,
    FOREIGN KEY (buyer_id) REFERENCES Buyer(buyer_id),
    FOREIGN KEY (property_id) REFERENCES Property(property_id)
);

CREATE TABLE Valuation (
    valuation_id INTEGER PRIMARY KEY,
    valuation_amount REAL,
    valuation_date TEXT,
    property_id INTEGER,
    FOREIGN KEY (property_id) REFERENCES Property(property_id)
);