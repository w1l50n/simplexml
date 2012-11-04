from lxml import etree

class XMLEncoder(object):
    
    def __init__(self, skipkeys=False,
            check_circular=True,
            default=None,
            sort_keys=False, item_sort_key=None,
            text_tag=None, cdata_tag=None, attr_tag=None,
            return_element=False):
        self.skipkeys = skipkeys
        if check_circular:
            self.markers = {}
        else:
            self.markers = None
        self.default = default
        self.sort_keys = sort_keys
        self.item_sort_key = item_sort_key
        self.text_tag = text_tag or '_text'
        self.cdata_tag = cdata_tag or '_cdata'
        self.attr_tag = attr_tag or '_attr'
        self.return_element = return_element


    def encode(self, o):

        roottag = o.keys()[0]
        root = etree.Element(roottag)
        self.convert(root, o[roottag])
        if self.return_element:
            return root
        else:
            return etree.tostring(root)


    def convert(self, parent, o):

        assert not isinstance(o, list)

        
        if self.markers is not None:
            markerid = id(o)
            if markerid in self.markers:
                raise ValueError("Circular reference detected %s, %s" % (parent, o))
            self.markers[markerid] = o
        
        if isinstance(o, dict):

            if self.item_sort_key:
                items = o.items()
                items.sort(key=self.item_sort_key)
            elif self.sort_keys:
                items = o.items()
                items.sort(key=lambda kv: kv[0])
            else:
                items = o.iteritems()

            for (tag, child) in items:
                if self.attr_tag and tag == self.attr_tag:
                    for attr_key, attr_value in child.iteritems():
                        parent.set(attr_key, attr_value)
                elif self.cdata_tag and tag == self.cdata_tag:
                    parent.text = etree.CDATA(child)
                elif self.text_tag and tag == self.text_tag:
                    parent.text = child
                elif isinstance(child, list):
                    for listchild in child:
                        elem = etree.Element(tag)
                        parent.append(elem)
                        self.convert(elem, listchild)
                else:
                    elem = etree.Element(tag)
                    parent.append(elem)
                    self.convert(elem, child)

        if isinstance(o, basestring):
            parent.text = o

        
        if self.markers is not None:
            del self.markers[markerid]
        


