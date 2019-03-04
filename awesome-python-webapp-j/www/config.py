




import config_default


class Dict(dict):

    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('Dict object has no attribute %s' % key)

    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults, overrite):
    r = {}
    for k, v in defaults.iteritems():
        if k in overrite and isinstance(v, dict):
            if isinstance(v, dict):
                r[k] = merge(v, overrite[k])
            else:
                r[k] = overrite[k]
        else:
            r[k] = v
    return r

def toDict(d):
    D = Dict()
    for k, v in d.iteritems():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D

configs = config_default.configs

try:
    import config_overrite
    configs = merge(configs, config_overrite.configs)
except ImportError:
    pass

configs = toDict(configs)

print(configs)

