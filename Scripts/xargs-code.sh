#!/bin/bash

#This is xargs code used to pass the sorted apps list to the apkpure-dl.sh file
xargs -n 1 ./apkpure-dl.sh < Apps-Top-100-Grossing-Sorted
