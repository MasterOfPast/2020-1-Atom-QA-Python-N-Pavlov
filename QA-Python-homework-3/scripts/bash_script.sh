#!/bin/bash
echo "all requests"
a=$(cat $1 | wc -l)
b=$(($a + 1))
echo $b
echo "POST"
cat $1 | grep POST | wc -l
echo "GET"
cat $1 | grep GET | wc -l
echo 'top 10 client'
grep ' 4[01]. ' $1 | sort -nrk10 | head -n 10 | awk '{print $7, $9, $1}'
