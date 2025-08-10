BEGIN;

-- Make links unique so duplicates can’t reappear
ALTER TABLE books
  ADD CONSTRAINT books_link_key UNIQUE (link);

-- Useful indexes
CREATE INDEX IF NOT EXISTS idx_books_price   ON books(price);
CREATE INDEX IF NOT EXISTS idx_books_rating  ON books(rating);

-- Fuzzy search support on title
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX IF NOT EXISTS idx_books_title_trgm
  ON books USING gin (title gin_trgm_ops);

COMMIT;

