#Filename fifo.py
from PRA import *


class fifo(PRA):
	 def __init__(self,faults,pageouts,size):
		PRA.__init__(self,faults,pageouts)
		self.size=size
		self.f=0#index of the frame number
		self.show=[]#to show the result of the frame situation every time
                self.frame=[]	
		#create the space to store the ref number
	        RowNum=size
                ColumnNum=2
                self.frame=[[0 for a in range(ColumnNum)] for b in range(RowNum)]
                for i in range(RowNum):
                
                    self.frame[i][0]="N"
	        for i in range(RowNum):
                
                    self.frame[i][1]=0
           
	 def ref(self,p,w):
		exist=False#all the pages are not in the frame now 
		
		for j in range(self.size):
			if p==self.frame[j][0]:#target has already been in the frame
				exist=True#Change the bool pageInFrame to be true
				if w==1:
					self.frame[j][1]=1
				for k1 in range(self.size):
                                    self.show.append(self.frame[k1][0])
				return j#nothing has been changed, return the reference number
		if (exist==False):#target is not in the frame, page fault occur
			self.faults=self.faults+1
			j=self.replace(p)#after replacing the page, record the position of the replacement
			if w==1:
				self.frame[j][1]=1#the page has been written
			
			for k2 in range(self.size):
                                    self.show.append(self.frame[k2][0])

			return j 

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
		

		if(full==False):#the frame is not full
			self.frame[position][0]=p
			return position
		
		if(full==True):#Frame is full.
			self.frame[self.f][0]=p#insert the new page into the position of reference
			self.f=self.f+1#move the index down to the next one
			if self.f==self.size:#move to the bottom of the frame stack
				self.f=0#index go back to the starting point
		return self.f
