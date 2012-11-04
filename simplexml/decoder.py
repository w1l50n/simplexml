from lxml import etree


class XMLDecoder(object):

    def __init__(self, dictclass=None, object_hook=None,
            object_pairs_hook=None, strip_cdata=True,
            text_tag=None, attr_tag=None):

        if dictclass is not None:
            self.dictclass = dictclass
        else:
            self.dictclass = dict
        self.object_hook = object_hook
        self.object_pairs_hook = object_pairs_hook
        self.strip_cdata = strip_cdata
        self.text_tag = text_tag or '_text'
        self.attr_tag = attr_tag or '_attr'


    def decode(self, s):

        parser = etree.XMLParser(strip_cdata=self.strip_cdata)
        root = etree.XML(s, parser)

        if self.object_pairs_hook is not None:
            return self.object_pairs_hook([(root.tag, self.convert(root))])
        elif self.object_hook is not None:
            return self.object_hook(self.dictclass([(root.tag, self.convert(root))]))
        else:
            return self.dictclass([(root.tag, self.convert(root))])


    def convert(self, node):

        data = self.dictclass()

        # childern
        for child in node:
            newitem = self.convert(child)

            if data.has_key(child.tag):
                if isinstance(data[child.tag], list):
                    data[child.tag].append(newitem)
                else:
                    data[child.tag] = [data[child.tag], newitem]
            else:
                data[child.tag] = newitem

        # attribute
        if node.attrib:
            data[self.attr_tag] = node.attrib

        # text
        text = node.text and node.text.strip()
        if not node.attrib and not node.getchildren() and text:
            data = node.text
        elif text:
            data[self.text_tag] = text

        elif self.object_pairs_hook is not None:
            data = self.object_pairs_hook(data.items())

        elif self.object_hook is not None:
            data = self.object_hook(data)

        return data

