import sys
sys.path.insert(0, '/Users/wilsonkichoi/src/simplexml')
import simplexml
from lxml import etree


data = {
    'root' : {
        'child_a' : 'text_a',
        'child_b' : ['text_b1', 'text_b2'],
        'child_c' : [
            {'_attr' : {'id' : 'id_c1'}, '_text' : 'text_c1'},
            {'_text' : 'text_c2'},
            {'child_d' : [
                {'_attr' : {'id' : 'id_d1'}, '_text' : 'text_d1'},
                'text_d2',
            ]},
        ],
        'child_e' : {
            '_attr': {'id': 'id_e'}, '_text': 'text_e',
            'child_f' : {'_attr': {'class': 'class_f', 'id': 'id_f'}},
            'child_g' : {"_cdata": "<ha>haha</ha>"},
        }
    }
}

expected_xml = '''<root>
  <child_a>text_a</child_a>
  <child_b>text_b1</child_b>
  <child_b>text_b2</child_b>
  <child_c id="id_c1">text_c1</child_c>
  <child_c>text_c2</child_c>
  <child_c>
    <child_d id="id_d1">text_d1</child_d>
    <child_d>text_d2</child_d>
  </child_c>
  <child_e id="id_e">
    text_e
    <child_f class="class_f" id="id_f"/>
    <child_g><![CDATA[<ha>haha</ha>]]></child_g>
  </child_e>
</root>'''

parser = etree.XMLParser(remove_blank_text=True, strip_cdata=False)
root = etree.XML(expected_xml, parser)
etree.tostring(root)

xml = simplexml.dumps(data, sort_keys=True)


x = simplexml.dumps(data, sort_keys=True)
dx = simplexml.loads(x)

parser = etree.XMLParser(remove_blank_text=True)
root = etree.XML(expected_xml, parser)
etree.tostring(root)


root = simplexml.dumps(data, return_element=True, sort_keys=True)
print etree.tostring(root, pretty_print=True)



d = {'root': {
          'a': [{'_attr': {'id': 'a_id'}, '_text': 'a text'},
                {'_attr': {'id': 'a_id'}, '_text': 'a text'},],
          'b': {'_attr': {'id': 'b_id'},
                '_text': 'b text',
                'c': {'_attr': {'class': 'c_class', 'id': 'c_id'}},
                'd': [{'_attr': {'id': 'd_id'}, '_text': 'd text'},
                      'd text']},
          'f': ['f text', 'f text'],
          'g': {"_cdata": "<ha>haha</ha>", "a":"aaa"},
          }

}


simplexml.dumps(data)



import sys
sys.path.insert(0, '/Users/wilsonkichoi/src/simplexml')
import simplexml

data = {
    'root' : {
        'child_a' : 'text_a',
        'child_b' : {'_attr' : {'id' : "b"}, '_text' : 'text_b'},
        'child_c' : {'_attr' : {'id' : "c"}, '_text' : 'text_c'},
        'child_d' : "text_d",
        'child_1' : {'_attr' : {'id' : "1"}, '_text' : 'text_1'},
    }
}


root = simplexml.dumps(data, sort_keys=True, return_element=True)
print etree.tostring(root, pretty_print=True)


import sys
sys.path.insert(0, '/Users/wilsonkichoi/src/simplexml')
import simplexml


data = {
    'root' : {
        'child_a' : 'text_a'
    }
}
data['root']['child_b'] = data['root']

simplexml.dumps(data, check_circular=False)


d = {
    'b':{
        'c' : 'c'
    }
}
d['a'] = d

check(d['a'], )

def check(o, marker):
    if marker is not None:
        mid = id(d)
        if mid in marker:
            raise ValueError("Circular reference detected")


xml_string = '''
<root>
    <a id="a_id">a text</a>
    <b id="b_id">
        <d>d text</d>
    </b>
    <b>2b text</b>
    <f>f text</f>
</root>
'''

xml_string = '''
<root>
    <a id="a_id">a text</a>
    <b id="b_id">
        b text
        <c id="c_id" class="c_class"/>
        <d id="d_id">d text</d>
        <d>d text</d>
    </b>
    <b>2b text</b>
    <f>f text</f>
    <f>
        f text
        <x>x text</x>
    </f>
    <g>
        <![CDATA[<ha>haha</ha>]]>
        <a>aaa</a>
    </g>
</root>
'''
import pprint
import simplexml
reload(simplexml)
dx = simplexml.loads(xml_string)
pprint.pprint(d)



from collections import OrderedDict
from lxml import etree
import pprint
import simplexml
reload(simplexml)
d = simplexml.loads(xml_string)
pprint.pprint(d)
x = simplexml.dumps(d, indent=4)
x
print etree.tostring(x)
b = x.getchildren()[1]


from collections import OrderedDict
from lxml import etree
import pprint
import simplexml
reload(simplexml)
d = {'root': {
          'a': [{'_attr': {'id': 'a_id'}, '_text': 'a text'},
                {'_attr': {'id': 'a_id'}, '_text': 'a text'},],
          'b': {'_attr': {'id': 'b_id'},
                '_text': 'b text',
                'c': {'_attr': {'class': 'c_class', 'id': 'c_id'}},
                'd': [{'_attr': {'id': 'd_id'}, '_text': 'd text'},
                      'd text']},
          'f': ['f text', 'f text'],
          'g': {"_cdata": "<ha>haha</ha>", "a":"aaa"},
          }

}
x = simplexml.dumps(d, sort_keys=True)

dx = simplexml.loads(x)

d['root']['g']['a'] = d['root']['a']
simplexml.dumps(d)


x = simplexml.dumps(d, return_element=True)
x
print etree.tostring(x, pretty_print=True)

y = simplexml.dumps(d)
y
etree.tostring(y)
print etree.tostring(y)


z = simplexml.dumps(d, indent=4)
z

d4 = simplexml.loads(xml_string, dictclass=OrderedDict)
d4
x4 = simplexml.dumps(d4, indent=4)
x4


d2 = simplexml.loads(xml_string, object_hook=OrderedDict)
d3 = simplexml.loads(xml_string, object_pairs_hook=OrderedDict)
d4 = simplexml.loads(xml_string, dictclass=OrderedDict)
d4
d
d2
d3

d = {'root': {'_text': 'text',
          'a': {'_attr': {'id': 'a_id'}, '_text': 'a text'},
          'b': {'_attr': {'id': 'b_id'},
                '_text': 'b text',
                'c': {'_attr': {'class': 'c_class', 'id': 'c_id'}},
                'd': [{'_attr': {'id': 'd_id'}, '_text': 'd text'},
                      'd text']},
          'f': ['f text', 'f text'],
          'g': {"_cdata": "<ha>haha</ha>", "a":"aaa"}
          }

}


from collections import namedtuple

i = namedtuple("i", "a b c")
j = namedtuple("j", "x y")

t = i(j("x", "y"), 2, 3)



xml_string = '''
<root>
    <a id="a_id">a text</a>
    <b id="b_id">
        b text
        <c id="c_id" class="c_class"/>
        <d id="d_id">d text</d>
        <d>d text</d>
    </b>
    <b>2b text</b>
    <f>f text</f>
    <f>
        f text
        <x>x text</x>
    </f>
    <g>
        <![CDATA[<ha>haha</ha>]]>
        <a>aaa</a>
    </g>
</root>
'''

from lxml import etree
root = etree.Element('root')
elem = etree.Element('elem')
root.append(elem)
print etree.tostring(root, pretty_print=True)

parser = etree.XMLParser(strip_cdata=True)
root = etree.XML(xml_string, parser)

root.getchildren()[-1].text

from xml.etree import ElementTree

xroot = ElementTree.XML(xml_string)


import simplejson
from collections import OrderedDict

d = {
    "a" : {
        "b" : 2,
        "f" : 4,
    },
    "c" : 3,
}
j = simplejson.dumps(d)

simplejson.loads(j, object_hook=OrderedDict)
