BEGIN;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    rating TEXT NOT NULL,
    link TEXT NOT NULL
);

COMMIT;
