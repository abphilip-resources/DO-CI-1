# Ansible Commands

### Inbuilt 
    ansible localhost -m ping                                   --> Pings the localhost
    ansible localhost -m find -a "paths=<dir> file_type=<x>"    --> Finds all directories in Github

### Playbook 
    ansible-playbook x.yml                                      --> Runs the playbook
    ansible-playbook x.yml -v                                   --> Runs the playbook with more details