from pagerefgen import *

algs=['fifo','lru','liu']
refstring=[3,4,6,8,7,5,1,3,1,5,6,0,4,5,2,7,4,3,2,7,0,3,3,6,3]
framesizes=[3,4,5]
algrithm={}
for each in algs:
	execfile(each+'.py')# define the replacement class
	print " "
	print "XXXXXXXXXXXXXXXX   Test     XXXXXXXXXXXXXXXXXXXXX"
	print "Current algorithm for test:", each
	print "The reference string for test is:"
	print refstring
	print "XXXXXXXXXXXXXXXX   Summary  XXXXXXXXXXXXXXXXXXXXX"
	for eachsize in framesizes:
		algrithm[each]=eval(each+'(0,0,eachsize)')
		for p in refstring:
			algrithm[each].ref(p,0)# invoke the ref method dynamically
		print "current size:",eachsize,"the total number of page fault:",algrithm[each].faults
                                                             
                                               
                               
		    
