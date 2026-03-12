#!/bin/bash
cd ~/Downloads

echo "Downloading Lockstep Arcade 0.1.4..."
curl -LO https://locksteparcade.com/lockstep_arcade_0.1.4_mac.zip

echo "Extracting..."
unzip -o lockstep_arcade_0.1.4_mac.zip -d lockstep_arcade_0.1.4

echo "Cleaning up..."
rm lockstep_arcade_0.1.4_mac.zip

echo "Remove quarantine attribute, if present (needed in case the archive was first downloaded manually)..."
xattr -d com.apple.quarantine lockstep_arcade_0.1.4/LockstepArcade

echo "Opening folder..."
open lockstep_arcade_0.1.4

echo "Done! Run LockstepArcade to play."
