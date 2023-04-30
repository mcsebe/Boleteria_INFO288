python3 main.py config/config0.json
python3 main.py config/config1.json
python3 main.py config/config2.json
python3 main.py config/configMaster.json

SELECT id, pname, price, create_date, last_update_date, current_status, server_name, subscriber_name
FROM public.products order by server_name ;

SELECT id, pname, price, create_date, last_update_date, current_status, server_name, subscriber_name
FROM public.products order by create_date  ;


delete  FROM public.products;

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    pname VARCHAR(100) NOT NULL,
    price NUMERIC(5,2),
    create_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_update_date timestamp,
    current_status VARCHAR(100) NOT NULL,
    server_name VARCHAR(100) NOT NULL,
    subscriber_name VARCHAR(100) NOT NULL 
);

Mu202t#U!Q4R