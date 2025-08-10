CREATE TABLE IF NOT EXISTS books (
  id SERIAL PRIMARY KEY,
  title        TEXT NOT NULL,
  price        NUMERIC(10,2),
  availability TEXT,
  rating       TEXT,
  link         TEXT UNIQUE,
  image_url    TEXT,
  created_at   TIMESTAMP DEFAULT NOW()
);
