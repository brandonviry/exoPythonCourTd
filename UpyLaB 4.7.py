
billet= [56,5 *20, 0 *10,0 * 5, 0*2, 0* 1]
somme = 0
for i in range (1,len(billet)):
    somme = somme + billet[i]
if somme < billet[0]:
  print((None, None, None, None, None))
elif somme == billet[0]:
  print((0, 0, 0, 0, 0))
else :
  print(somme-billet[0])
