#Dictionary Comprehension

keys = [1,2,3,4]
values = ["a","b","c","d"]

mydict = {k:v  for(k,v) in zip(keys,values)}

print(mydict)#{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
