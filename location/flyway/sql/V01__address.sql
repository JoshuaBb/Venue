CREATE TABLE address (
	address_id serial PRIMARY KEY,
	address_line_one VARCHAR (1024 ) UNIQUE NOT NULL,
    address_line_two VARCHAR ( 1024 ),
    address_line_three VARCHAR ( 1024 ),
    address_line_four VARCHAR ( 1024 ),
	city VARCHAR ( 256 ) NOT NULL,
	state_or_province VARCHAR(256) NOT NULL,
	zip_or_postal VARCHAR(256) NOT NULL,
	country_code VARCHAR(256) NOT NULL,
	address_key VARCHAR(36) NOT NULL UNIQUE,
	latitude NUMERIC,
	longitude NUMERIC,
	created_at TIMESTAMP NOT NULL
)