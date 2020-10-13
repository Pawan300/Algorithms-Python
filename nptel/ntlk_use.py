# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 11:21:19 2018

@author: pawan_300
"""

import ntlk
sentence="""I,Pawan bisht from 
uttarakhand 
this is my pc,
so please be aware of my fist """
tokens=ntlk.word_tokenize(sentence)
print(tokens)