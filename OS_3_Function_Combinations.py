import collections
import itertools

#creating globals for the vars in functions
a = 0
booli = False
result = a
i2 = 0
i3 = 0
#define each line as a function 
def f1_1():
    global a,booli
    booli = (a==0)

def f1_2():
    global a,booli
    if(booli == True):
        a = 10

def f1_3():
    global a,booli
    if(booli == False):
        a = 0

def f2_1():
    return None

def f2_2():
    global a
    global i2
    i2 = a

def f2_3():
    global i2 
    i2 = a+i2+2

def f2_4():
    global a
    global i2
    a = i2

def f3_1():
    return None
    
def f3_2():
    global a,i3
    i3 = a+1

def f3_3():
    global a,i3
    a = i3

def f3_4():
    global a,result
    result = a

#init the vars as needed and produce result 
#created by the combination of lines
def produce(dicti):
    global a,i2,i3,result,booli
    a = 0 
    i2 = 0
    i3 = 0
    result = 0
    booli = False
    for t in range(11):
        dicti[t]()
    
# 2d array of each line of each function 
lines = [[f1_1,f1_2,f1_3],
        [f2_1,f2_2,f2_3,f2_4],
        [f3_1,f3_2,f3_3,f3_4]]


if __name__ == "__main__":
    results = set() #set of results
    placements = [0,1,2,3,4,5,6,7,8,9,10] #avalable spots 
    # all the sorted sub groups of the size of 3
    # of the available placements 
    p1 = itertools.combinations(placements,3) 
    counter = 0 #counts the amount of results 
    for combi in p1:
        order = dict() #hash table: key = actual line , val = function  
        index = 0
        for i in combi:# fit the currect line to the placement that have been chosen
            order[i] = lines[0][index]
            index = index + 1
        p_c = [x for x in placements if x not in combi]# placements/combi (group sub)
        p2 = itertools.combinations(p_c,4)#choose another 4 spots
        for combi2 in p2:
            index = 0
            for i in combi2:
                order[i] = lines[1][index]
                index = index + 1
            # p_c  = placements/(combi union combi2)
            p_c = [x for x in placements if x not in combi2 and x not in combi]
            p2 = itertools.combinations(p_c,4)
            for combi3 in p2:
                index = 0
                for i in combi3:
                    order[i] = lines[2][index]
                    index = index + 1
            #produce result
            produce(order)
            counter += 1 #add the attempt
            results.add(result) #add the result to the set 
    #prints 
    print("results = " + str(results))
    print("|results| = "+str(len(results)))
    print("counter: " + str(counter))


        
        


