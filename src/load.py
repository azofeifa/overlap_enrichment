import os
def _4bed(FILE):
	print "loading input bed file..."
	G,EXIT 	= dict(),False
	FH 		= open(FILE,"r")
	for i,line in enumerate(FH):
		if line[0]!="#":
			line_array 	= line.strip("\n").split("\t")
			if len(line_array)!=4:
				print "at line",i+1,"column number is not of length four"
				EXIT 		= True
			try:
				xs 		= map(int,line_array[1:])
				if xs[-1]!=0 and xs[-1]!=1:
					print "at line",i+1,"could not convert columns 2-4 to numbers"
					EXIT 	= True
			except:			
				print "at line",i+1,"could not convert columns 2-4 to numbers"
				EXIT 		= True

			if EXIT:
				break
			chrom=line_array[0]
			if chrom not in G:
				G[chrom]=list()
			G[chrom].append(xs)
	FH.close()
	for chrom in G:
		G[chrom].sort()
	return EXIT,G
def _3bed(FILE):
	EXIT 		= False
	G,FH 		= dict(),open(FILE,"r")
	for i,line in enumerate(FH):
		if line[0]!="#":
			line_array 	= line.strip("\n").split("\t")
			try:
				chrom,xs 	= line_array[0],map(int,line_array[1:3])
				if chrom not in G:
					G[chrom] = list()
				G[chrom].append(xs)
			except:
				print "line",i+1,"was not properly formatted as bed file"				
				EXIT 		= True
				break
	for chrom in G:
		G[chrom].sort()
	return EXIT,G
def _3beds(DIR):
	print "loading db of bed files..."
	A 	= list()
	for f in os.listdir(DIR):
		EXIT,G 	= _3bed(DIR+"/"+f)
		if not EXIT:
			A.append((f,G))
		else:
			print "ignoring",f
	return A


