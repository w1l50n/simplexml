import unittest
import simplexml

class TestDecode(unittest.TestCase):
    
    def test_decode(self):
        xml = '''<root>
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

        data = simplexml.loads(xml)


import pprint
import simplexml

xml = '''<root>
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

data = simplexml.loads(xml, strip_cdata=False)
pprint.pprint(data)


{'root': {'child_a': 'text_a',
          'child_b': ['text_b1', 'text_b2'],
          'child_c': [{'_attr': {'id': 'id_c1'}, '_text': 'text_c1'},
                      'text_c2',
                      {'child_d': [{'_attr': {'id': 'id_d1'},
                                    '_text': 'text_d1'},
                                   'text_d2']}],
          'child_e': {'_attr': {'id': 'id_e'},
                      '_text': 'text_e',
                      'child_f': {'_attr': {'class': 'class_f', 'id': 'id_f'}},
                      'child_g': '<ha>haha</ha>'}}}

ed = {
            'root' : {
                'child_a' : 'text_a',
                'child_b' : ['text_b1', 'text_b2'],
                'child_c' : [
                    {'_attr' : {'id' : 'id_c1'}, '_text' : 'text_c1'},
                    'text_c2',
                    {'child_d' : [
                        {'_attr' : {'id' : 'id_d1'}, '_text' : 'text_d1'},
                        'text_d2',
                    ]},
                ],
                'child_e' : {
                    '_attr': {'id': 'id_e'}, '_text': 'text_e',
                    'child_f' : {'_attr': {'class': 'class_f', 'id': 'id_f'}},
                    'child_g' : "<ha>haha</ha>",
                }
            }
        }





