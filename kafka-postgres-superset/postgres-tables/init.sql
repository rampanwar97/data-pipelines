-- init.sql
CREATE TABLE IF NOT EXISTS salse (
    user_id INT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    full_name VARCHAR(255),
    address TEXT,
    phone_number VARCHAR(20)
);
