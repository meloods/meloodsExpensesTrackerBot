#!/bin/bash

# Get the list of conda environments and parse it
env_list=$(conda env list | awk '{print $1}' | tail -n +4)

# Loop through each environment and export its package list
for env in $env_list; do
  conda list --export -n $env > "${env}_packages.txt"
done
