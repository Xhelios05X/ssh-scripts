#!/bin/bash

# function returns the help of this script
function Help(){
    echo "sftpFilesSent.sh - script to sending files into host via ssh

usage: ./sftpFilesSent.sh [USERNAME] [IP] [FILES] [DIRECTORY]
options:
    -h          help

scipt is created by Xhelios05X
github.com/Xhelios05X"
    exit 0
}

# function archives and compress directory
# $1 - directory to archive
function archiveDirectory(){
    tar -czvf $1.tar.gz $1
}

# main function of script
# $1 - sftp server username
# $2 - sftp server ip address
# $3 - files directory to sent
# $4 - directory on ftp server
function main(){
    if [ "$1" == "-h" ] || [ $# == 0 ]
    then
        Help
    fi

    archiveDirectory $3

    # sending files via ssh connection
    scp $3.tar.gz $1@$2:$4

    # removing .tar.gz file from local directory
    rm $3.tar.gz
}

main $1 $2 $3