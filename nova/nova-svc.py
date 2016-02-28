# -*- encoding: utf-8 -*-
'''
pkg auditing
'''
import logging
import yaml

DISTRO = 'CentOS Linux-7'

__virtualname__ = 'hubble.svc'
log = logging.getLogger(__name__)

def __virtual__():
    '''
    Load the module
    '''
    return True


def audit():

    ret = {}

    with open('/srv/salt/_nova/nova-svc.yaml') as fh_:
        audit = yaml.safe_load(fh_)
    
    for k,v in audit['service']['blacklist'].iteritems():
        if DISTRO in v['data']:
            for benchmark in v['data'][DISTRO]:
                for item in benchmark.items():
                    check = item[0]
                    tags = item[1]
                    ret[check] = __salt__['service.status'](check)
                    if ret[check]:
                        ret[check] = 'Failed %s' % tags
                    else:
                        ret[check] = 'Passed %s' % tags
        else:
            log.debug('Platform not supported for check: %s' % k)

    return ret
