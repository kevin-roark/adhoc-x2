#!/bin/bash
now=$(date +"%m_%d_%Y")
fname="adhoc-data-backup-$now.sql"

echo "doing backup to $fname"
sudo -u postgres pg_dump adhocdb > $fname
echo "backup complete"

echo "uploading backup to cloudup"
up $fname
wait
echo "upload complete"

echo "deleting local file"
rm $fname
echo "file deleted, bye bye"
