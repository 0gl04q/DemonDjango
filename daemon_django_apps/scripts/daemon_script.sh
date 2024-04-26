#!/bin/bash

IP="127.0.0.1"
PORT="8001"

INFO=$(sar 1 1 | tail -n 1 | head -n 1 | awk '{print $NF}' | sed 's/,/./g')

CPU=$(echo "100.00 - $INFO" | bc)

curl -X POST -H 'Content-Type: application/json' -d '{
  "cpu": '$CPU'
}' http://"$IP":"$PORT"/api/