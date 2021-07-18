# ansible-helloplugin
A sample hello world module written for Ansible

## Variables:

- name: required (string)
- surname: not required (string)

## Documentation

`ansible-doc hello`

## Examples:

Example playbook:
```
---
- name: test playbook using custom code
  hosts: localhost
  tasks:
    - name: using my custom module
      hello:
        name: Gerasimos
      register: result
      
    - name: show output
      debug:
        var: result
```