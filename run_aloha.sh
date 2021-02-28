#!/bin/bash

reps=`seq 1`
nDevices=`seq 10 10 20`

for r in $reps
do

      for n in $nDevices
      do
             ./waf --run "aloha-throughput --nDevices=$n --RngRun=$r"
      done
done
