-- Create table for storing temperature data
CREATE TABLE IF NOT EXISTS temperature_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    temperature REAL
);

-- Create table for storing humidity data
CREATE TABLE IF NOT EXISTS humidity_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    humidity REAL
);

-- Create table for storing pressure data
CREATE TABLE IF NOT EXISTS pressure_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    pressure REAL
);

-- Create table for storing air quality data
CREATE TABLE IF NOT EXISTS air_quality_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    air_quality REAL
);

-- Create table for storing light level data
CREATE TABLE IF NOT EXISTS light_level_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    light_level REAL
);

-- Create table for storing API keys
CREATE TABLE IF NOT EXISTS api_keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE NOT NULL,
    owner TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert dummy temperature data
INSERT INTO temperature_data (temperature) VALUES 
(22.5), (24.1), (19.8), (23.0), (21.5);

-- Insert dummy humidity data
INSERT INTO humidity_data (humidity) VALUES 
(55.2), (60.3), (58.9), (62.1), (57.5);

-- Insert dummy pressure data
INSERT INTO pressure_data (pressure) VALUES 
(1012.3), (1010.5), (1015.2), (1008.7), (1011.8);

-- Insert dummy air quality data
INSERT INTO air_quality_data (air_quality) VALUES 
(35.2), (40.1), (38.5), (42.0), (37.8);

-- Insert dummy light level data
INSERT INTO light_level_data (light_level) VALUES 
(200.5), (220.1), (190.3), (210.7), (215.8);

-- Insert dummy API keys
INSERT INTO api_keys (key, owner) VALUES
('d2f8a9c4-3b6e-4f91-a2f7-8e5d1b4a6c3e', 'User1'),
('a9b8c7d6-e5f4-3a2b-1c0d-9e8f7g6h5i4j', 'User2'),
('f3e2d1c0-b9a8-7g6h-5i4j-3k2l1m0n9o8p', 'User3'),
('c2b1a0d9-e8f7-6g5h-4i3j-2k1l0m9n8o7p', 'User4'),
('b1a0d9c8-e7f6-5g4h-3i2j-1k0l9m8n7o6p', 'User5');
