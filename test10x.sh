#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "ERROR: The argument must be pw8 or pw9."
  exit 1
fi

if [ "$1" = "pw9" ]; then
  mkdir -p PW9/convolu_results
  for i in {0..9}; do
    sudo sync;sudo bash -c "echo 3 > /proc/sys/vm/drop_caches"
    perf stat -o PW9/N${i}_PW9_convolu_results.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions,idle-cycles-backend,idle-cycles-frontend python3 rede_neural_convolucional.py
  done

  mkdir -p PW9/image_results
  for i in {0..9}; do
    sudo sync;sudo bash -c "echo 3 > /proc/sys/vm/drop_caches"
    perf stat -o PW9/N${i}_PW9_image_results.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions,idle-cycles-backend,idle-cycles-frontend python3 image_classification.py
  done

  echo "Tests for POWER9 completed."
  exit
fi

if [ "$1" = "pw8" ]; then
  mkdir -p PW8/convolu_results
  for i in {0..9}; do
    sudo sync;sudo bash -c "echo 3 > /proc/sys/vm/drop_caches"
    perf stat -o PW8/N${i}_PW8_convolu_results.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions python3 rede_neural_convolucional.py
  done

  mkdir -p PW8/image_results
  for i in {0..9}; do
    sudo sync;sudo bash -c "echo 3 > /proc/sys/vm/drop_caches"
    perf stat -o PW8/N${i}_PW8_image_results.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions python3 image_classification.py
  done

  echo "Tests for POWER8 completed."
  exit
fi

echo "ERROR: The argument must be pw8 or pw9."
exit 1
