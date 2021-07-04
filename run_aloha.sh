#!/bin/bash

reps=`seq 1`
#nDevices=`seq 10 10 20`
loss=`seq 3 0.5 5'

for p in $loss
do

      for r in $reps
      do
             ./waf --run "aloha-throughput --nDevices=7515 --pathloss=$p --RngRun=$r"
      done
done
