#!/bin/bash

for file in *.HTM; do
    name=$(basename "$file" .HTML)
    mv "$file" "$name.html"
done