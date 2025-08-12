BEGIN;

CREATE UNIQUE INDEX books_link_key ON public.books USING btree (link);
CREATE INDEX idx_books_price ON public.books USING btree (price);
CREATE INDEX idx_books_rating ON public.books USING btree (rating);
CREATE INDEX idx_books_title_trgm ON public.books USING gin (title gin_trgm_ops);

COMMIT;
