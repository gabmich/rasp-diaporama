#!/bin/bash

# get current script path, no matter where it is located
SCRIPT_PATH=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# get current day of week - caution : depends of system language
CURRENT_DAY_OF_WEEK=$(date +%A)

echo "$CURRENT_DAY_OF_WEEK"

# set file_path shortcut
TARGET_DIR="$SCRIPT_PATH/$CURRENT_DAY_OF_WEEK"

echo "$TARGET_DIR"

if [ -d "$TARGET_DIR" ]
then
	rm -r "$TARGET_DIR"
fi

bash "$SCRIPT_PATH/lib/dropbox_uploader.sh" download "/$CURRENT_DAY_OF_WEEK" "$TARGET_DIR"
