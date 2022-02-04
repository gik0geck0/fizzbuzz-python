#!/usr/bin/bash

command=$1

for f in $(ls input*.txt);
do
	if [[ "$f" =~ ^input([^.]*)\.txt$ ]]; then
		index=${BASH_REMATCH[1]}
		expectedFile="output$index.txt"
		# echo "Testing $f against $expectedFile"
		result=$(cat "$f" | $1 | diff "$expectedFile" -)
		if [ $? -ne 0 ]; then
			echo "Failed $f to produce $expectedFile"
			echo "$result" | sed 's/^/    /'
		else
			echo "Pass $f"
		fi
	else
		echo "Invalid file picked up: $f"
	fi
done