#!/bin/bash
for i in $(seq 1 500); do
    curl -s localhost:83
done | sort | uniq -c
