import sys
import os
sys.path.insert(1, os.getcwd())
import unittest
from unittest.mock import patch
import src.domain.classes as classes
import src.repository.repo as repo
import src.services.serv as serv
import src.ui.ui as ui

print("test.py")
class test_repo(unittest.TestCase):
    def setUp(self):
        self.book1 = classes.book({'uuid':'1','name':'book1','author':'author1'})
        self.book2 = classes.book({'uuid':'2','name':'book2','author':'author2'})
        self.book3 = classes.book({'uuid':'3','name':'book3','author':'author3'})
        
        self.client1 = classes.client({'uuid':'1','name':'client1'})
        self.client2 = classes.client({'uuid':'2','name':'client2'})
        self.client3 = classes.client({'uuid':'3','name':'client3'})

        
        self.repo = repo.repository('noload')
        self.repo.add(self.book1)
        self.repo.add(self.book2)
        self.repo.add(self.book3)
        self.repo.add(self.client1)
        self.repo.add(self.client2)
        self.repo.add(self.client3)
        
        
    def test_add(self):
        self.assertEqual(self.repo.add(self.book1),True)
        self.assertEqual(self.repo.add(self.client1),True)
        self.assertEqual(self.repo.add(self.book2),True)
        self.assertEqual(self.repo.add(self.client2),True)
        
    def test_remove(self):
        self.assertEqual(self.repo.removeBook(['book1']),True)
        self.assertEqual(self.repo.removeClient(['client1']),True)
        try:
            self.assertEqual(self.repo.removeBook(['book1']),False)
            self.assertEqual(True,False)
        except:
            self.assertEqual(True,True)
        try:
            self.assertEqual(self.repo.removeClient(['client1']),False)
            self.assertEqual(True,False)
        except:
            self.assertEqual(True,True)
        
    def test_update(self):
        self.assertEqual(self.repo.updateBook(['#2','name','carte2']),True)
        self.assertEqual(self.repo.updateClient(['#2','name','clientul2']),True)
        self.assertEqual(self.repo.updateBook(['#2','uuid','1']),True)
        self.assertRaises(ValueError,self.repo.updateBook,['#2','uuid','1'])

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

for i in range(200):
    print()
unittest.main(argv=[''], verbosity=2, exit=False)
    
            
        
        










        
        
        
        