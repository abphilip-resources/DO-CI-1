# Ansible Commands

### Local 
    ansible localhost -m ping                                   --> Pings the localhost
    ansible localhost -m find -a "paths=<dir> file_type=<x>"    --> Finds all type 'x' files in directory

### Group
    ansible <group> -m -ping                                    --> Pings all hosts in the group
    ansible <group> -m setup | less                             --> Shows the host information
    ansible <group> -m user -a "name=<name> password=<x>"       --> Create a user 
    ansible <group> -m user -a "name=<name> state=absent"       --> Delete a user 

### Playbook 
    ansible-playbook x.yml                                      --> Runs the playbook
    >  x.yml -v                                                 --> Runs the playbook with more details
    >  x.yml –e                                                 --> Passes variables to the playbook
    >  -i y.ini x.yml                                           --> Runs the playbook with a different inventory
    ansible-playbook x.yml –list-hosts                          --> Lists the hosts
    ansible-playbook x.yml –list-tasks                          --> Lists the tasks
    ansible-playbook x.yml –syntax-check                        --> Checks syntax of the playbook
    ansible-playbook x.yml –e max_client=100                    --> Sets the max_client in the playbook
