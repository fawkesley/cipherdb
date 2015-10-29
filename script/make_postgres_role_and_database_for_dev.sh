#!/bin/bash -e

function create_postgresql_user_for_my_username {
    CREATE_USER="createuser --superuser ${USER}"
    sudo su -c "${CREATE_USER}" postgres
}

function create_postgresql_database_for_my_username {
    CREATE_DATABASE="createdb --owner ${USER} cipherdb"
    sudo su -c "${CREATE_DATABASE}" postgres
}


create_postgresql_user_for_my_username
create_postgresql_database_for_my_username
