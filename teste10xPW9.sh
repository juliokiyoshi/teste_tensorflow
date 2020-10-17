#!/bin/bash

for i in {0..9}; do
  sudo su
  sync; echo 3 > /proc/sys/vm/drop_caches
  exit
  perf stat -o PW9/N${i}_PW9_results_convolu.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions,idle-cycles-backend,idle-cycles-frontend python3 rede_neural_convolucional.py
done

for i in {0..9}; do
  sudo su
  sync; echo 3 > /proc/sys/vm/drop_caches
  exit
  perf stat -o PW9/N${i}_PW9_results_image.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions,idle-cycles-backend,idle-cycles-frontend python3 image_classification.py
done

sudo su
sync; echo 3 > /proc/sys/vm/drop_caches
exit
exit
