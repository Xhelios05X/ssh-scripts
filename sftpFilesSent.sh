#!/bin/bash

function Help(){
    echo "Usage: "
    exit 0
}

# $1 - directory to archive
function archiveDirectory(){
    tar -czyf $1.tar.gz $1
}

# main function of script
# $1 - sftp server username
# $2 - sftp server ip address
# $3 - files directory to sent
function main(){
    if [ "$1" == "-h" ] || [ $# == 0 ]
    then
        Help
    fi

    archiveDirectory $3

    sftp $1@$2
}

main $1 $2 $3