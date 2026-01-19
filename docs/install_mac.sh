#!/bin/bash
cd ~/Downloads

echo "Downloading Lockstep Arcade 0.1.1..."
curl -LO https://locksteparcade.com/lockstep_arcade_0.1.1_mac.zip

echo "Extracting..."
unzip -o lockstep_arcade_0.1.1_mac.zip -d lockstep_arcade_0.1.1

echo "Cleaning up..."
rm lockstep_arcade_0.1.1_mac.zip

echo "Removing quarantine attribute (in case this was added)..."
xattr -d com.apple.quarantine LockstepArcade

echo "Opening folder..."
open lockstep_arcade_0.1.1

echo "Done! Run LockstepArcade to play."
