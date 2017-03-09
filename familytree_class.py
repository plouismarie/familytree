class member(object):
    def __init__(self,name,status,of):
        self.name=name
        self.status=status
        self.of=of

    def mysearch(self,first,middle,last):
    	'''
    	searching for matching entry
    	'''
    	if (self.of == last) & (self.status == middle):
    		print "{} has been identified as {} of {}".format(self.name,self.status,last)
    		return 1
    	else:
    		return 0

def getparentlink(f,m,l):
	'''
	return obvious relative
	'''
	middle=m # will take care of brother sister cousin status
	if m == "son":
		middle="father"
	if m == "father":
		middle="son"
	if m == "daughter":
		middle="mother"
	if m == "mother":
		middle="daughter"
	return l,middle,f

if __name__ == '__main__':

	entry="Null"
	familytree=[]
	while entry != "Quit":
		entry=raw_input('Input: [ E.g.: Abel is the brother of Cain / Who is the brother of Cain / \'Quit\' to Exit ]\n => ')
		if entry != "Quit":

			try:
				first=entry.split(' is the ')[0]
				last=entry.split(' of ')[1]
				middle=entry.split(' ')[3]
			
			except IndexError:
				print('This syntax was not expected')
		
			else:
				if first != "Who":
					print " ## Updating the Base +2"
					familytree.append(member(first,middle,last))
					f,m,l=getparentlink(first,middle,last)
					familytree.append(member(f,m,l))


				if first == "Who":
					print " ## Checking the Base:",len(familytree)
					result=0
					for elem in familytree:
						result+=elem.mysearch(first,middle,last)
					if (result == 0):
						print('No one has been identied as {} of {}'.format(middle,last))

