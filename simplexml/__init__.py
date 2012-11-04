from encoder import XMLEncoder
from decoder import XMLDecoder


def dump(obj, fp, skipkeys=False, check_circular=True,
        cls=None,
        default=None,
        sort_keys=False, item_sort_key=None,
        text_tag=None, cdata_tag=None, attr_tag=None,
        return_element=False,
        **kw):
    pass


def dumps(obj, skipkeys=False, check_circular=True,
        cls=None,
        default=None,
        sort_keys=False, item_sort_key=None,
        text_tag=None, cdata_tag=None, attr_tag=None,
        return_element=False,
        **kw):

    if cls is None:
        cls = XMLEncoder

    return cls(
        skipkeys=skipkeys,
        check_circular=check_circular,
        default=default,
        sort_keys=sort_keys,
        item_sort_key=item_sort_key,
        text_tag=text_tag,
        cdata_tag=cdata_tag,
        attr_tag=attr_tag,
        return_element=return_element,
        **kw).encode(obj)


def load(fp, cls=None, dictclass=None,
        object_hook=None, object_pairs_hook=None,
        strip_cdata=True,
        text_tag=None, attr_tag=None,
        **kw):

    return loads(fp.read(), cls=cls,
        dictclass=dictclass,
        object_hook=object_hook,
        object_pairs_hook=object_pairs_hook,
        strip_cdata=strip_cdata,
        text_tag=text_tag, attr_tag=attr_tag,
        **kw)


def loads(s, cls=None, dictclass=None,
        object_hook=None, object_pairs_hook=None,
        strip_cdata=True,
        text_tag=None, attr_tag=None,
        **kw):

    if cls is None:
        cls = XMLDecoder

    return cls(
        dictclass=dictclass,
        object_hook=object_hook,
        object_pairs_hook=object_pairs_hook,
        strip_cdata=strip_cdata,
        text_tag=text_tag,
        attr_tag=attr_tag,
        **kw).decode(s)
