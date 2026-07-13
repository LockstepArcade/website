#!/bin/bash
cd ~/Downloads

echo "Downloading Lockstep Arcade 1.1.1..."
curl -LO https://locksteparcade.com/lockstep_arcade_1.1.1_mac.zip

echo "Extracting..."
unzip -o lockstep_arcade_1.1.1_mac.zip -d lockstep_arcade_1.1.1

echo "Cleaning up..."
rm lockstep_arcade_1.1.1_mac.zip

echo "Remove quarantine attribute, if present (needed in case the archive was first downloaded manually)..."
xattr -d com.apple.quarantine lockstep_arcade_1.1.1/LockstepArcade

echo "Opening folder..."
open lockstep_arcade_1.1.1

echo "Done! Run LockstepArcade to play."
