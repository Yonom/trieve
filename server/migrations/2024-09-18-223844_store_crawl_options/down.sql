-- This file should undo anything in `up.sql`
ALTER TABLE crawl_requests DROP COLUMN IF EXISTS crawl_options;