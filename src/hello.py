#!/usr/bin/python3

from ansible.module_utils.basic import *

ANSIBLE_METADATA = {
    'metadata_version' : '1.0',
    'status': ['dev'],
    'supported_by': 'Gerasimos Alexiou'
}

DOCUMENTATION = '''
---
module: hello module

short_description: This is a test hello module

ansible version: "2.4"

description:
    - "This is a hello module that gets as an input your name and outputs a hello message"

options:
    name:
        description:
            - This is your name that must be passed as an input to the module
        required: true
    surname:
        description:
            - This is your surname that must be passed as an input to the module
        required: false


author:
    - Gerasimos Alexiou()
'''
EXAMPLES = '''
# print your name
- name: print your name
  hello:
    name: Gerasimos
    surname: Alexiou

# print your name with surname
- name: print your name
  hello:
    name: Gerasimos
    surname: Alexiou

# fail the module
no fail functionality has been developed.
'''

RETURN = '''
original_message:
    description: Gerasimos
    type: str
message:
    description: Hello Gerasimos
'''
#def hello(data):
#has_changed = True
#meta = 


def main():
    fields = {
        "name" : {"required":True, type:str} ,
        "surname" : {"required":False, type:str}
    }

    module = AnsibleModule(argument_spec=fields)

    if not module.params['surname']:
        response = {"Hello" + " " + module.params['name'] }
    else:
        response = {"Hello" + " " + module.params['name'] + " " + module.params['surname'] }

    module.exit_json(changed=True ,meta=response)
    module.fail_json(msg="Something fatal happened")


if __name__ == '__main__':
    main()