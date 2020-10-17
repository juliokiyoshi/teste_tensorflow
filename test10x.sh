#!/bin/bash

ISUDO=$(id root)
if [ "$ISUDO" != "0" ]; then
  echo "You must run this script as root."
  exit
fi

if [ "$#" -ne 1 ]; then
  echo "The argument must be pw8 or pw9."
  exit
fi

if [ "$1" = "pw9" ]; then
  for i in {0..9}; do
    sync; echo 3 > /proc/sys/vm/drop_caches
    perf stat -o PW9/N${i}_PW9_results_convolu.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions,idle-cycles-backend,idle-cycles-frontend python3 rede_neural_convolucional.py
  done

  for i in {0..9}; do
    sync; echo 3 > /proc/sys/vm/drop_caches
    perf stat -o PW9/N${i}_PW9_results_image.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions,idle-cycles-backend,idle-cycles-frontend python3 image_classification.py
  done

  echo "Tests for POWER9 completed."
  exit
fi

if [ "$1" = "pw8" ]; then
  for i in {0..9}; do
    sync; echo 3 > /proc/sys/vm/drop_caches
    perf stat -o PW8/N${i}_PW8_results_convolu.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions python3 rede_neural_convolucional.py
  done

  for i in {0..9}; do
    sync; echo 3 > /proc/sys/vm/drop_caches
    perf stat -o PW8/N${i}_PW8_results_image.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions python3 image_classification.py
  done

  echo "Tests for POWER8 completed."
  exit
fi

echo "The argument must be pw8 or pw9."
exit
