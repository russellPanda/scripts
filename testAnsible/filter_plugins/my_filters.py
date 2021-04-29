#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'a_filter': self.a_filter,
            'another_filter': self.b_filter
        }

    def a_filter(self, a_variable):
        a_new_variable = a_variable + ' CRAZY NEW FILTER'
        return a_new_variable

    def b_filter(self, a_variable, another_variable, yet_another_variable):
        a_new_variable = a_variable + ' - ' + another_variable + ' - ' + yet_another_variable
        return a_new_variable

# ---
# - hosts: localhost
#   tasks:
#     - name: Print a message
#       debug:
#         msg: "{{'test'|another_filter('the','filters')}}"
#
#
# ansible-playbook test.yml
# [WARNING]: No inventory was parsed, only implicit localhost is available
#
# [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'
#
#
# PLAY [localhost] **************************************************************************************************************************************
#
# TASK [Gathering Facts] ********************************************************************************************************************************
# ok: [localhost]
#
# TASK [Print a message] ********************************************************************************************************************************
# ok: [localhost] => {
#     "msg": "test - the - filters"
# }
#
# PLAY RECAP ********************************************************************************************************************************************
# localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
