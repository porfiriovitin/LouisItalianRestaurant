CREATE TABLE IF NOT EXISTS "customers"(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(100),
    cpf VARCHAR(13),
    cellphone VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS "tables"(
    table_number INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS "reservation"(
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_number INTEGER,
    booking_date VARCHAR(10),
    scheduled_time VARCHAR(8),
    customer_id INTEGER,
    FOREIGN KEY (table_number) REFERENCES "tables"(table_number),
    FOREIGN KEY (customer_id) REFERENCES "customers"(customer_id)
);

-- Inserir as mesas disponíveis
INSERT INTO "tables" (table_number)
VALUES (1), (2), (3), (4), (5), (6), (7);