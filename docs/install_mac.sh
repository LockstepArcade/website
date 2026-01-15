#!/bin/bash
cd ~/Downloads

echo "Downloading Lockstep Arcade 0.1.0..."
curl -LO https://locksteparcade.com/lockstep_arcade_0.1.0_mac.zip

echo "Extracting..."
unzip -o lockstep_arcade_0.1.0_mac.zip -d lockstep_arcade_0.1.0

echo "Cleaning up..."
rm lockstep_arcade_0.1.0_mac.zip

echo "Opening folder..."
open lockstep_arcade_0.1.0

echo "Done! Run LockstepArcade to play."
