import  unittest

from learn.two.测试.mydict import Dict


class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a = 1, b = '测试')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, '测试')
        self.assertTrue(isinstance(d, dict))

    # def test_key(self):                  #这部分是测试用例通不过的例子
    #     d = Dict()
    #     d['key'] = 'value'
    #     self.assertSetEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()