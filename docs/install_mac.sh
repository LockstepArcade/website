#!/bin/bash
cd ~/Downloads

echo "Downloading Lockstep Arcade 0.0.9..."
curl -LO https://locksteparcade.com/lockstep_arcade_0.0.9_mac.zip

echo "Extracting..."
unzip -o lockstep_arcade_0.0.9_mac.zip -d lockstep_arcade_0.0.9

echo "Cleaning up..."
rm lockstep_arcade_0.0.9_mac.zip

echo "Opening folder..."
open lockstep_arcade_0.0.9

echo "Done! Run LockstepArcade to play."
