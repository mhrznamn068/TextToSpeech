#!/bin/bash
TEXT="Hello What's up"
curl -X POST http://localhost:8089/tts -H 'Content-Type: application/json'  --data-raw "{\"text\":\"$TEXT\"}"
