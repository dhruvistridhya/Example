ls=[23,5,4,10,12,3,45,31,2]

def even(ls):
	if ls%2==0:
		return True
	else:
		return False

even_ls=filter(even,ls)
for i in even_ls:
	print(i)