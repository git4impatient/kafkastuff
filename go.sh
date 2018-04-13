#!/usr/bin/bash

# copyright (c) 2018 Martin Lurie

for x in {0..1000000}  
do 
echo $$ "hello world " $(date)  
done  | ./genKafkamsg.py 
