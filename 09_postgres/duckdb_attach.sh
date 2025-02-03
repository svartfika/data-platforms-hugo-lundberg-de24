#!/bin/bash

# Load and convert PostgreSQL env vars to DuckDB format
source .env
export PGPASSWORD="${POSTGRES_PASSWORD}"
export PGUSER="${POSTGRES_USER}"
export PGDATABASE="${POSTGRES_DB}"
export PGHOST="localhost"

duckdb -cmd "ATTACH '' AS postgres_db (TYPE POSTGRES);"