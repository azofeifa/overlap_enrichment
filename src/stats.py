import time
from load import _3bed
import scipy.stats as ss
def overlap(A,B):
	O,OH = 0,0
	for chrom in A:
		if chrom in B:
			a,b 	= A[chrom],B[chrom]
			j,N 	= 0,len(b)
			for start,stop,state in a:
				while j < N and b[j][1] < start:
					j+=1
				k 	= j
				while k < N and b[k][0] < stop:
					O+=1;k+=1
					if state:
						OH+=1
	return O,OH

def eval(IN,DB,OUT):
	print "computing overlaps..."
	F 			= lambda x: x[-1]
	FHW 		= open(OUT, "w")
	FHW.write("fileID,k,K,n,N,pvalue\n")
	for f,B in DB:
		'''count total number features
		'''
		N 		= float(sum([len(IN[chrom]) for chrom in IN if chrom in B ]))
		'''count the number "special cases"
		'''
		n 		= float(sum([sum(map(F,IN[chrom])) for chrom in IN if chrom in B ]))

		K,k 	= overlap(IN,B)
		hg1 	= ss.hypergeom(N,K,n)
		pv 	= min(hg1.cdf(k),0.5)*2
		FHW.write(f+","+str(k) + "," + str(K) + "," + str(n) + "," + str(N) + "," + str(pv) + "\n")













