#!/bin/bash

set -e && [[ "$DEBUG" == 'true' ]] && set -x

showHelp() {
cat << EOF
Usage: ./deployment/run-detect-empty-files.sh --help

Detect empty files in this project. Deployment of
the stack will fail if there are empty files.

EOF
}

while [[ $# -gt 0 ]]
do
key="$1"
case $key in
    -h|--help)
        showHelp
        exit 0
        ;;
esac
done

empty_files_found=""

for file in $(git ls-files)
do
  if [[ -f "$file" && ! -s "$file" ]]; then
    empty_files_found="yes"
    echo "$file is empty!"
  fi
done

if [[ $empty_files_found == "yes" ]]; then
  echo "############################################"
  echo "Empty files detected!"
  echo "############################################"
  exit 1;
fi
