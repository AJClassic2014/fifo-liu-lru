#filename liu.py
from PRA import *


class liu(PRA):
        def __init__(self,faults,pageouts,size):
	   PRA.__init__(self,faults,pageouts)
	   self.round=0
	   self.size=size
	   self.frame=[]
	   self.cntNo=[]
	   self.order=[]#store the order between two same count number to determine which one is smaller to be removed
           self.show=[]#to show the result of the frame situation every time
           #create the space to store the ref number
	   RowNum=size
           ColumnNum=2
           self.frame=[[0 for a in range(ColumnNum)] for b in range(RowNum)]
           for i in range(RowNum):
                
                    self.frame[i][0]="N"
	   for i in range(RowNum):
                
                    self.frame[i][1]=0
	   
	   for i in range(size):
	       self.cntNo.append(0)#frame is not dirty
	   
	   for i in range(size):
	       self.order.append(0)
	#Check if the target page we want to insert has already been in frame or not
        def ref(self,p,w):
	   for i in range(self.size):
	       if p==self.frame[i][0]:#the target page we want to insert has already been in frame
		   self.round=self.round+1#accumulate the times of being reference regardless of replacement and frame updated
		   self.order[i]=self.round
		   self.cntNo[i]=self.cntNo[i]+1#accumulate the times of being reference 
		   if w==1:
			self.frame[i][1]=1
		   for k1 in range(self.size):
                                    self.show.append(self.frame[k1][0])
	           return i
	   # if the page is not in frame, page fault occur
	   self.faults=self.faults+1
	   f=self.replace(p)
	   if w==1:
		self.frame[f][1]=1
	   for k2 in range(self.size):
                                    self.show.append(self.frame[k2][0])
	   return f

        #inherited from PRA
        def replace(self,p):
	        full=True#assume the frame is full
                position=0#the position to insert the new page
		#find the correct position
		for i in range(self.size):
			if(self.frame[i][0]=="null"):#the frame that have not been occupied
                                position=i
                                full=False
				break;#the reference of the empty frame is i
	        if(full==False):#The set of frames are not full, put the new one into empty frame
	           self.frame[position][0]=p
	           self.round=self.round+1
	           self.order[position]=self.round
	           self.cntNo[position]=1
	           return position
	        if(full==True):#Frame is full. replace the pages
	           f=self.choose2()
	           self.frame[f][0]=p
	           self.cntNo[f]=1
	           self.round=self.round+1
	           self.order[f]=self.round
	           return f
	#choose the one replaced by the new one
	def choose1(self):#choose the one that has the smallest cntNo., but do not consider the round
           f1=0
	   for i in range(self.size):
	      if(self.cntNo[i]<self.cntNo[f1]):
	         f1=i
	   return f1
	def choose2(self): #after the first choose method, choose the correct one if the cntNo. are equal
	   f2=self.choose1()
	   for j in range(self.size):
		if(self.cntNo[f2]==self.cntNo[j]):#numbers of cntNo. are equal, but they are not from the same frame
		   if(f2!=j):
		      if(self.order[j]<self.order[f2]):
		         return j
           return f2
