# Bouilding a ChatBot with Deep NLP

import numpy as np
import tensorflow as tf
import re
import time

# Importing the dataset

lines = open('movie_lines.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
conversations = open('movie_conversations.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')

id2line = {}
for line in lines:
    _line =  line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]

conversations_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'",'')
    conversations_ids.append(_conversation.split(','))
    
    