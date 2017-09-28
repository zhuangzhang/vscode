# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 13:26:20 2017
123
@author: zhang
"""
print '-'*20, 'hello zz!', '-'*20

#==============================================================================
# f = open(r'F:\python_test\test1.txt','r')
# 
# f.readline()
#==============================================================================

def showmenu():
    pr="""
    p(U)sh
    p(O)p
    (V)iew
    
    Enter choice:"""
    choice = raw_input(pr).strip()[0].lower()
    print '\nYou picked: [%s]' % (choice)
    return True
if __name__=='__main__':
    showmenu()
    
#==============================================================================
# fdict = dict((['x',1],['y',2]))
# #for key in fdict.keys():
# #    print 'key=%s, value=%s' % (key, fdict[key])
# for key in fdict:
#     print 'key=%s, value=%s' % (key, fdict[key])
#==============================================================================
