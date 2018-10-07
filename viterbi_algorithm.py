# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 00:01:25 2017

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 23:40:03 2017

@author: Admin
"""
with open("sents.txt", 'r') as f:
   lines = f.readlines()
   lines = [x.strip() for x in lines] 
   l1=lines[0].split()
   l2=lines[1].split()
   l3=lines[2].split()

print("PROCESSING SENTENCE:")
print (l1)
#print (l3)
tag_list=['phi', 'noun', 'verb', 'inf', 'prep', 'fin']
q={}
e={} 
"""The word followed by its most frequent tag as value"""
word_tag_counts={}


with open('probs.txt', 'r') as f_s:
    f_sents=f_s.read()
words_probs=f_sents.split()
l=len(words_probs)
print (l)

wwp={}              #####dictionaru to store probablilities of all words and tags combined (q and e combined).
for i in range(0,l,3):
   # for j in range(3):
   #"""or words_probs[i].capitalize() or words_probs[i].upper()"""   
#    if ((words_probs[i]  in ('noun', 'verb', 'inf' , 'prep' , 'phi' , 'fin')) or  (words_probs[i].upper()  in ('noun', 'verb', 'inf' , 'prep' , 'phi' , 'fin'))
#    or  (words_probs[i].capitalize()  in ('noun', 'verb', 'inf' , 'prep' , 'phi' , 'fin'))):
#        q[words_probs[i]]={}
#        q[words_probs[i]][words_probs[i+1]]=words_probs[i+2]
#        
#    else:
#        e[words_probs[i]]={}
#        e[words_probs[i]][words_probs[i+1]]=words_probs[i+2]
#    
    #wwp[words_probs[i]]={}
    a = ()
    a = (words_probs[i],words_probs[i+1])
    wwp[a]=words_probs[i+2]
    #a.append(words_probs[i+1])
   
   # wwp[words_probs[i]][words_probs[i+1]]=words_probs[i+2]
    
    
    """Converting this into a list for future use"""
#word_tag_list=[]
#for k,v in wwp.items():
#    for k1, v1 in v.items():
#        word_tag_list.append([k,k1])
        
#word_tag_dict={}
#for k,v in wwp.items():
#    for k1, v1 in v.items():
#        word_tag_dict[k,k1]=v1
#print (word_tag_dict)
        
def viterbi_(a,sentence,tags):
    """Initializing With Correct Variables where n stands for number of words
        in the selected sentence. m stands for total number distinct Tags available
        and an array named dp to contain the probablity of the values stored. a is the nested dictionary. b is 
        the sentence...c is list of tags...dp is pi(k,u,v)..."""
    
    
    tag_len = 5
    n = len(sentence)
    pi = [[0.0 for x in range(tag_len)] for y in range(n+1)]
    forward=[[0.0 for x in range(tag_len)] for y in range(n+1)]
    bp = [[0 for x in range(tag_len)] for y in range(n+1)]
    pi[0][0] = 1            #####pi(0,0,0)=1 condition...

    #print ("Sentence in consideration")
    #print (sentence)
    
    for i in range(1,n+1):
        for j in range(0, tag_len-1):
           
            word = sentence[i-1]        ###current word
            pos_index = 0               ###index for list of tags        
            max_prob = 0.0
            max_prob_forward=0.0
            tag = tags[j]               ###current tag
            word_tag = (word,tag)
            temp_forward=0.0
                                                                                                    
            for k in range(0,tag_len-1):
                if (tag != 'phi'):
                    tag_tag = (tags[j],tags[k])
                    if (word_tag in a):
                        e_prob = a[word_tag]
                    else:
                        e_prob = 0.0001
                            
                    if(tag_tag in a):
                        t_prob = a[tag_tag]
                        
                    else:
                        t_prob = 0.0001
                  
                    temp = pi[i-1][k]*float(t_prob)*float(e_prob)
                    
                    temp_forward+=pi[i-1][k]*float(t_prob)*float(e_prob)
                    #print(e_prob)
                    if (temp > max_prob):  ###viterbi
                        max_prob = temp
                        pos_index = k
                     
                    if (temp_forward > max_prob):  ###forward algorithm
                        max_prob = temp_forward
                        #pos_index = k
                     
                    if (temp_forward>max_prob_forward):
                        max_prob_forward=temp_forward
                        
                    
                        
                else:
                    #print("hello")
                    tag_tag = (tag,'phi')
                    if (word_tag in a):
                        e_prob = a[word_tag]
                    else:
                        e_prob = 0.0001
                    
                    if(tag_tag in a):
                        t_prob = a[tag_tag]
                    else:
                        t_prob = 0.0001
                    #print(e_prob) 
                    #print(t_prob)
                    max_prob = float(t_prob)*float(e_prob)
                    max_prob_forward=max_prob
                    pos_index = k
                    break
                

            pi[i][j] = max_prob
            forward[i][j]=max_prob_forward
            bp[i][j] = pos_index
          
           
            #print("P(%s=%s)=%r" %(tags[i],tags[j],pi[i][j]))
            print("Viterbi values are: %r" %pi[i][j])
            print('#')
            print('forward values are: %r:'%forward[i][j])
            #print(bp[i][j])
            #print(pi[i][j])
    l=n
    find_prob = 0.0
    tag_num = -1
    last_tag = 0
    for i in range(l,0,-1):
        if (i == l):
            for j in range(0,tag_len-1):
                if (pi[i][j] > find_prob):
                    find_prob = pi[i][j]
                    tag_num = j
                    last_tag = bp[i][j]
            print (tag_list[tag_num])
            
        else:
            print (tag_list[last_tag])
            last_tag = bp[i][last_tag]
        
                
            
            
            
            
viterbi_(wwp, l1, tag_list)   
#def main():
#    import sys
#    args = sys.argv
#    #print (args[1])
#    #print (args[2])
#    tag_list=['phi', 'noun', 'verb', 'inf', 'prep', 'fin']
#    viterbi_(wwp,l1,tags_list)
#    
#
#if __name__ == "__main__":
#    main()          


       

         
            
            
        



    
    
    
