#!/bin/bash

#The script should take the directory name as a variable, compress the directory, and save the backup with a timestamp.

directory_to_backup="/Users/bhbandi/Desktop/Bash Scripting/Auto Backup Files/DirectoryToBackup"

backup_location="/Users/bhbandi/Desktop/Bash Scripting/Auto Backup Files/Backup"

current_date=$(date +%Y-%m-%d)

#Appending date in backup file name
tar -czf "$backup_location/backup-$current_date.tar.gz" "$directory_to_backup"

echo "backup of $directory_to_backup completed successfully on $current_date inside $backup_location"