#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/5 Card.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/5 Card.dmg" && rm "dist/5 Card.dmg"
create-dmg \
  --volname "5 Card" \
  --volicon "5CardAppIcon.icns" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "5 Card.app" 175 120 \
  --hide-extension "5 Card.app" \
  --app-drop-link 425 120 \
  "dist/5 Card.dmg" \
  "dist/dmg/"