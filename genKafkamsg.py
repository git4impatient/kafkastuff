#!/usr/bin/python
# (c) copyright Martin Lurie 2016
# sample code - not supported
import sys 
import time
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['10.142.0.5:9092'])
for line in sys.stdin:
        line = line.strip()
        producer.send('my-topic',bytes(line) )
        #print line
        # generate 100 events per second
        #time.sleep(.01)
        # generate 10 events per second
        #time.sleep(.5)
        # 
        #time.sleep(.001)
