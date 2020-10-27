#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "ERROR: The argument must be pw8 or pw9."
  exit 1
fi

if [ "$1" = "pw9" ]; then
  mkdir -p ~/PW9/ResNet_pets
  mkdir -p ~/PW9/ResNet_pets/acc
  for i in {0..9}; do
    sudo sync;sudo bash -c "echo 3 > /proc/sys/vm/drop_caches"
    perf stat -o ~/PW9/ResNet_pets/N${i}_PW9_ResNet_pets.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions,idle-cycles-backend,idle-cycles-frontend python3 resnetClassification.py >> ~/PW9/ResNet_pets/acc/PW9acc_pets${i}.txt
  done

  echo "Tests for POWER9 completed."
  exit
fi

if [ "$1" = "pw8" ]; then
  mkdir -p ~/PW8/ResNet_pets
  mkdir -p ~/PW8/ResNet_pets/acc
  for i in {0..9}; do
    sudo sync;sudo bash -c "echo 3 > /proc/sys/vm/drop_caches"
    perf stat -o ~/PW8/ResNet_pets/N${i}_PW8_ResNet_pets.txt -e branches,branch-misses,cache-misses,cache-references,cycles,instructions python3 resnetClassification.py >> ~/PW8/ResNet_pets/acc/PW8_acc_pets${i}.txt
  done

  echo "Tests for POWER8 completed."
  exit
fi

echo "ERROR: The argument must be pw8 or pw9."
exit 1
