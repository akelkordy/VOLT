from __future__ import unicode_literals
import unittest
import codecs
from get_chars import get_chars
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

class TestVoltCharsMethod(unittest.TestCase):

    def test_get_chars_simple(self):
        source = codecs.open(os.path.join(currentdir,'testData','simpleSource.txt'),encoding='utf-8')
        target = codecs.open(os.path.join(currentdir,'testData','simpleTarget.txt'),encoding='utf-8')
        chars = get_chars(source, target);

        result = codecs.open(os.path.join(currentdir,'testData','simpleResult.txt'),encoding='utf-8')
        resultLines = result.readlines()
        count = 0
        for line in resultLines:
            charsString = list(chars.items())[count][0] + ':' + list(chars.items())[count][0]
            self.assertEqual(line,charsString)
            count += 1
        
        source.close()
        target.close()
        result.close()


    def test_get_chars_complex(self):
        source = codecs.open(os.path.join(currentdir,'testData','charSource.txt'),encoding='utf-8')
        target = codecs.open(os.path.join(currentdir,'testData','charTarget.txt'),encoding='utf-8')
        chars = get_chars(source, target);

        result = codecs.open(os.path.join(currentdir,'testData','charResult.txt'),encoding='utf-8')
        resultLines = result.readlines()
        count = 0
        for line in resultLines:
            charsString = list(chars.items())[count][0] + ':' + list(chars.items())[count][0]
            self.assertEqual(line,charsString)
            count += 1
        
        source.close()
        target.close()
        result.close()

class TestVoltTokensMethod(unittest.TestCase):

    def test_read_tokens(self):
        source = codecs.open(os.path.join(currentdir,'testData','tokenTrain.en'),encoding='utf-8')
        target = codecs.open(os.path.join(currentdir,'testData','tokenTrain.en'),encoding='utf-8')
        candidate = codecs.open(os.path.join(currentdir,'testData','tokenCode'),encoding='utf-8')

        

        

if __name__== '__main__':
    unittest.main()
