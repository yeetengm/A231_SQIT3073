curriencies = []
curriencies.append('Yen')
curriencies_2 = 'Dollar'
curriencies.append(curriencies_2)
print(curriencies)

# Access tuple:      if print(buah[2]), answer = durian 
# Negative Indexing: if print (buah[-1]), answer = durian
# Index Range:       if print (buah[1:2]), answer = ('rambutan')


# Iteration in a tuple: for i in buah: 
#                           print(i),  answer = manggis
#                                               rambutan
#                                               durian 
#                       for i in range(len(buah)):
#                           print(buah[i]),  answer = manggis
#                                                     rambutan
#                                                     durian 
#                       i = 0
#                       while i<len(buah):
#                           print(buah[i])
#                           i+=1 ,  answer = manggis
#                                            rambutan
#                                            durian 


# Add item to tuple:  buah = ("manggis","rambutan","durian")
#                     buahbuahan = ("pisang",)        [逗号一定要写，不然会error]
#                     buah += buahbuahan
#                     print(buah),  answer = ('manggis', 'rambutan', 'durian', 'pisang')


# Remove Item (Tuple是unchangeable的，所以当我们要delete tuple里的东西时，需要把tuple换成list后才delete，不然会发生各种error）
#   1）TypeError:  buah = ("manggis","rambutan","durian")
#                 del(buah[1])
#                 print(buah),  answer: SyntaxError: cannot delete function call / TypeError: 'tuple' cnnt support item deletion
#   2) NameError:  buah = ("manggis","rambutan","durian")
#                  del (buah)
#                  print(buah),  answer: NameError: name 'buah' is not defined
# 所以我们需要换tuple去list才delete:  buah = ("manggis","rambutan","durian","pisang")
#                                  buahbuahan = list(buah)
#                                  print(buah)                       [在这一行run的话，answer: ('manggis', 'rambutan', 'durian', 'pisang') ]
#                                  buahbuahan.remove("pisang")       [这一行是删除的code:  b.remove("item")]
#                                  buah=tuple(buahbuahan)
#                                  print(buah) , answer: ('manggis', 'rambutan', 'durian')   [成功删除 “pisang”]


