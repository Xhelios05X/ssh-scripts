#!/bin/bash

function Help(){
    echo "Usage: "
    exit 0
}

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

    scp $3.tar.gz $1@$2:$4

    rm $3.tar.gz
}

main $1 $2 $3