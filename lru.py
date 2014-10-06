#Filename lru.py
from PRA import *


class lru(PRA):
	def __init__(self,faults,pageouts,size):
		PRA.__init__(self,faults,pageouts)
		self.size=size
		self.frame=[]
		self.priority=[]		#store the reference of the frame with the order of priority to be removed, the first one should be the one removed
		self.show=[]#to show the result of the frame situation every time
                #create the space to store the ref number
		RowNum=size
                ColumnNum=2
                self.frame=[[0 for a in range(ColumnNum)] for b in range(RowNum)]
                for i in range(RowNum):
                
                    self.frame[i][0]="N"
	        for i in range(RowNum):
                
                    self.frame[i][1]=0
	
	def ref(self,p,w):
		exist= False 
		#check if the new page has already been in the frame list 
		for j in range(self.size):
			if p==self.frame[j][0]:
				exist= True 
				if w==1:
					self.frame[j][1]=1
				self.priority.remove(j)#remove the latest used one and put it to the end of the list
				self.priority.append(j)#put the latest referenecd one to the end of the list
				for k1 in range(self.size):#store the element currently in the frame list one by one 
                                    self.show.append(self.frame[k1][0])
				return j
		if(exist == False):
			self.faults=self.faults+1
			f=self.replace(p)
			if w==1:
				self.frame[j][1]=1
			for k2 in range(self.size):#store the element currently in the frame list one by one 
                                    self.show.append(self.frame[k2][0])
			return j


	def replace(self,p):
		#check the frame is full or not
		full=True#assume the frame is full
                position=0#the position to insert the new page
		#find the correct position
		for i in range(self.size):
			if(self.frame[i][0]=="N"):#the frame that have not been occupied
                                position=i
                                full=False
				break;#the reference of the empty frame is i
		if(full==False):
			self.frame[position][0]=p
			self.priority.append(position)
			return position
		
		if(full==True):#Frame is full.
			position =self.priority.pop(0)#the first one at the priority list should be the frame that has not been referenced for the longest period
			self.frame[position][0]=p
			self.priority.append(position)
			return position
