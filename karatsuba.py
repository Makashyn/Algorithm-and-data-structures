# formula
# ad + bc = (a+b)(c+d) - ac - bd
# XY = 10**n * ac + 10 ** (n/2) * (ad + bc) + bd
# total : XY =  10**n * ac + 10 ** (n/2) * ((a+b)(c+d) - ac - bd) + bd

def karatsuba(x, y):
	print(type(x))
	if len(x) < 5:
		return str(int(x) * int(y))
	z =	int(max(len(x), len(y))/2) 
	a = int(int(x) / 10 ** z)
	b = int(int(x) % 10 ** z)
	c = int(int(y) / 10 ** z)
	d = int(int(y) % 10 ** z)
	ac = int(karatsuba(str(a), str(c)))
	bd = int(karatsuba(str(b), str(d)))
	abcd = int(karatsuba(str(a + b), str(c + d)))
	return str((10  ** max(len(x), len(y))) * ac + (10 ** z) * ( abcd - ac - bd) + bd)

if __name__ == '__main__':
	x = '21625695688898558125310188636840316594920403182768'
	y = '13306827740879180856696800391510469038934180115260'	
	print(karatsuba(x, y))



