# coding: utf-8

'''Unit tests for the sort.py library'''

__author__  = 'mystblue'
__version__ = '0.1-devel'
__date__    = '2013/11/12'

import unittest

import cbz_compress

class SortTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCompare(self):
        self.assertEqual(0, cbz_compress.compare("a", "a"))
        self.assertEqual(1, cbz_compress.compare("b", "a"))
        self.assertEqual(-1, cbz_compress.compare("a", "b"))
        self.assertEqual(0, cbz_compress.compare("1", "1"))
        self.assertEqual(-1, cbz_compress.compare("1", "2"))
        self.assertEqual(1, cbz_compress.compare("2", "1"))
        self.assertEqual(0, cbz_compress.compare("111", "111"))
        self.assertEqual(0, cbz_compress.compare("_", "_"))
        self.assertEqual(-1, cbz_compress.compare("!", "_"))
        self.assertEqual(-1, cbz_compress.compare("-.jpg", "1.jpg"))
        self.assertEqual(-1, cbz_compress.compare("001.jpg", "01.jpg"))
        self.assertEqual(1, cbz_compress.compare(u"001.jpg".encode("cp932"), u"_001.jpg".encode("cp932")))
        self.assertEqual(1, cbz_compress.compare(u"001.jpg".encode("cp932"), u"-001.jpg".encode("cp932")))
        self.assertEqual(1, cbz_compress.compare(u"001.jpg".encode("cp932"), u"+001.jpg".encode("cp932")))
        self.assertEqual(1, cbz_compress.compare(u"001.jpg".encode("cp932"), u"##001.jpg".encode("cp932")))
        self.assertEqual(1, cbz_compress.compare(u"001.jpg".encode("cp932"), u"^001.jpg".encode("cp932")))
        self.assertEqual(1, cbz_compress.compare(u"001.jpg".encode("cp932"), u":001.jpg".encode("cp932")))
        self.assertEqual(1, cbz_compress.compare(u"001.jpg".encode("cp932"), u"(001.jpg".encode("cp932")))
        self.assertEqual(-1, cbz_compress.compare("001.jpg", "a001.jpg"))
        self.assertEqual(-1, cbz_compress.compare("00001.jpg", "001.jpg"))
        self.assertEqual(-1, cbz_compress.compare("001-256.jpg", "001.jpg"))
        self.assertEqual(1, cbz_compress.compare("SCAN_A0001C.jpg", "SCAN_A0001A1.jpg"))
        self.assertEqual(-1, cbz_compress.compare("SCAN_A0001C.jpg", "SCAN_A0001D1.jpg"))
        self.assertEqual(-1, cbz_compress.compare("img1.jpg", "img10.jpg"))
        self.assertEqual(-1, cbz_compress.compare("img9.jpg", "img10.jpg"))
        self.assertEqual(-1, cbz_compress.compare("img1.jpg", "img11.jpg"))
        self.assertEqual(-1, cbz_compress.compare("img11.jpg", "img111.jpg"))
        self.assertEqual(-1, cbz_compress.compare("img01.jpg", "img11.jpg"))
        self.assertEqual(-1, cbz_compress.compare("img-11.jpg", "img-12.jpg"))
        self.assertEqual(-1, cbz_compress.compare("img11.jpg", "img100.jpg"))
        
    def testSort1(self):
        file_list = ['88.txt', '5.txt', '11.txt']
        sorted_list = cbz_compress.sort(file_list)
        success_file_list = ['5.txt', '11.txt', '88.txt']
        self.assertEqual(success_file_list, sorted_list)

    def testSort2(self):
        file_list = ['Ie5', 'Ie6', 'Ie4_01', 'Ie401sp2', 'Ie4_128', 'Ie501sp2']
        sorted_list = cbz_compress.sort(file_list)
        success_file_list = ['Ie4_01', 'Ie4_128', 'Ie5', 'Ie6', 'Ie401sp2', 'Ie501sp2']
        self.assertEqual(success_file_list, sorted_list)

    def testSort3(self):
        file_list = ['1.txt', '5.txt', '11.txt']
        sorted_list = cbz_compress.sort(file_list)
        success_file_list = ['1.txt', '5.txt', '11.txt']
        self.assertEqual(success_file_list, sorted_list)

    def testSort4(self):
        file_list = ['img-1.txt', 'img-9.txt', 'img-10.txt', 'img-11.txt', 'img-12.txt', 'img-100.txt']
        sorted_list = cbz_compress.sort(file_list)
        success_file_list = ['img-1.txt', 'img-9.txt', 'img-10.txt', 'img-11.txt', 'img-12.txt', 'img-100.txt']
        self.assertEqual(success_file_list, sorted_list)

if __name__ == '__main__':
    unittest.main()
