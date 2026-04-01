DROP TABLE IF EXISTS Valuation;
DROP TABLE IF EXISTS Purchase;
DROP TABLE IF EXISTS Transaction;
DROP TABLE IF EXISTS Property_Feature;
DROP TABLE IF EXISTS Property;
DROP TABLE IF EXISTS Buyer;
DROP TABLE IF EXISTS Agent;
DROP TABLE IF EXISTS Location;

CREATE TABLE Location (
    location_id INT PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    area_name VARCHAR(100) NOT NULL,
    zipcode VARCHAR(10)
);

CREATE TABLE Agent (
    agent_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    license_number VARCHAR(50) UNIQUE NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE Buyer (
    buyer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_number VARCHAR(20),
    budget_range VARCHAR(20)
);

CREATE TABLE Property (
    property_id INT PRIMARY KEY,
    price FLOAT NOT NULL,
    size_sqft FLOAT NOT NULL,
    property_type VARCHAR(50) NOT NULL,
    year_built INT,
    status VARCHAR(50),
    location_id INT,
    agent_id INT,
    FOREIGN KEY (location_id) REFERENCES Location(location_id),
    FOREIGN KEY (agent_id) REFERENCES Agent(agent_id)
);

CREATE TABLE Property_Feature (
    feature_id INT PRIMARY KEY,
    property_id INT,
    feature_name VARCHAR(50),
    feature_value VARCHAR(100),
    FOREIGN KEY (property_id) REFERENCES Property(property_id)
);

CREATE TABLE Transaction (
    transaction_id INT PRIMARY KEY,
    sale_price FLOAT NOT NULL,
    sale_date DATE,
    payment_type VARCHAR(20),
    property_id INT,
    FOREIGN KEY (property_id) REFERENCES Property(property_id)
);

CREATE TABLE Purchase (
    purchase_id INT PRIMARY KEY,
    purchase_date DATE,
    ownership_percentage FLOAT,
    buyer_id INT,
    property_id INT,
    FOREIGN KEY (buyer_id) REFERENCES Buyer(buyer_id),
    FOREIGN KEY (property_id) REFERENCES Property(property_id)
);

CREATE TABLE Valuation (
    valuation_id INT PRIMARY KEY,
    valuation_amount FLOAT,
    valuation_date DATE,
    property_id INT,
    FOREIGN KEY (property_id) REFERENCES Property(property_id)
);
