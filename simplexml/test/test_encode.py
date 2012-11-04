import unittest
import simplexml
import re
from lxml import etree


class TestEncode(unittest.TestCase):
    
    def test_encode(self):
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
        xml = simplexml.dumps(data, sort_keys=True)

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
        expected_xml = re.sub('\n *', '', expected_xml)
        
        self.assertEqual(xml, expected_xml)


    def test_circular_reference(self):
        data = {
            'root' : {
                'child_a' : 'text_a'
            }
        }
        data['root']['child_b'] = data['root']

        with self.assertRaises(ValueError) as cm:
            simplexml.dumps(data)

        self.assertGreaterEqual(cm.exception.message.find('Circular reference detected'), 0)


    def test_circular_reference(self):
        data = {
            'root' : {
                'child_a' : 'text_a'
            }
        }
        data['root']['child_b'] = data['root']

        with self.assertRaises(RuntimeError) as cm:
            simplexml.dumps(data, check_circular=False)

        self.assertGreaterEqual(cm.exception.message.find('maximum recursion depth exceeded'), 0)


    def test_item_sort_key(self):
        data = {
            'root' : {
                'child_a' : 'text_a',
                'child_b' : {'_attr' : {'id' : "b"}, '_text' : 'text_b'},
                'child_c' : {'_attr' : {'id' : "c"}, '_text' : 'text_c'},
                'child_d' : 'text_d',
                'child_1' : {'_attr' : {'id' : "1"}, '_text' : 'text_1'},
            }
        }

        def get_attr(kv):
            key, value = kv
            if isinstance(value, dict):
                if value.has_key('_attr'):
                    return value['_attr']['id']
            return key

        item_sort_key = lambda kv : get_attr(kv)
        xml = simplexml.dumps(data, item_sort_key=get_attr)

        expected_xml = '''<root>
            <child_1 id="1">text_1</child_1>
            <child_b id="b">text_b</child_b>
            <child_c id="c">text_c</child_c>
            <child_a>text_a</child_a>
            <child_d>text_d</child_d>
        </root>'''
        expected_xml = re.sub('\n *', '', expected_xml)

        self.assertEqual(xml, expected_xml)

        
    def test_return_element(self):
        data = {
            'root' : {
                'child_a' : 'text_a',
                'child_b' : {'_attr' : {'id' : "b"}, '_text' : 'text_b'},
                'child_c' : {'_attr' : {'id' : "c"}, '_text' : 'text_c'},
                'child_d' : 'text_d',
                'child_1' : {'_attr' : {'id' : "1"}, '_text' : 'text_1'},
            }
        }
        root = simplexml.dumps(data, sort_keys=True, return_element=True)

        expected_xml = '''<root>
            <child_1 id="1">text_1</child_1>
            <child_a>text_a</child_a>
            <child_b id="b">text_b</child_b>
            <child_c id="c">text_c</child_c>
            <child_d>text_d</child_d>
        </root>'''
        expected_xml = re.sub('\n *', '', expected_xml)

        self.assertEqual(etree.tostring(root), expected_xml)

