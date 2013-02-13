# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
	
map={"GIST1":"GIST_ID1","GIST2":"GIST_ID2"}

import sys
from subprocess import call
import string
index=0
files=[]
changed=[]
if (len(sys.argv) > 1):
	for x in range(1,len(sys.argv)):
		files.append(sys.argv[x])
else:
	print "Needs filenames as arguments"
        

for f in files:
	read=open(f)
	readVal="start"
	test="GIST_START"
	while readVal != "":
		readVal=read.readline()
		if test in readVal:
			sub=readVal[string.find("GIST_START",readVal)+12:].strip()
			test="GIST_END"
			readVal=read.readline()
			write=open("GIST_"+sub+".json","w")
			changed.append(sub)
			while not test in readVal:
				write.write(readVal)
				readVal=read.readline()
			write.close()
			index=index+1
			test="GIST_START"
	read.close()

for key in changed:
	call(["jist","-u",map[key],"GIST_"+key+".json"])
	call(["rm","GIST_"+key+".json"])
