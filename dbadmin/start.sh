#!/usr/bin/env bash

echo $POSTGRES_HOST:$POSTGRES_PORT:$POSTGRES_USER:$POSTGRES_PASSWORD > ~/.pgpass

pg_dumpall -w