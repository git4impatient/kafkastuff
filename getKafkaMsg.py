#!/usr/bin/python
# (c) copyright Martin Lurie 2016
# sample code - not supported
import sys 
import time
from kafka import KafkaConsumer
consumer = KafkaConsumer(bootstrap_servers='ip-10-0-0-154.ec2.internal:9092',
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
consumer.subscribe(['mylogs'])
for message in consumer:
                print(message)
