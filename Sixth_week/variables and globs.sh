#!/bin/bash

line="-------------------------------"; echo $line
echo "Starting at: $(date)"; echo; echo $line

echo "UPTIME"; uptime; echo; echo $line

echo "FREE"; free; echo; echo $line

echo "WHO"; who; echo; echo $line

echo "Finishing at $(date)"; echo $line