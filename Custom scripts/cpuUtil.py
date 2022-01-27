import subprocess

try: input = raw_input
except NameError: raw_input = input

#rawcommand = "sacct -a -r GPU -S2021-11-01 -E2021-12-01 -X -ojobid"
startTime = raw_input("Enter start time:\n")
endTime = raw_input("Enter end time\n")
command = rawcommand[:36] + startTime + rawcommand[36:39] + endTime + rawcommand[39:]
command = rawcommand


process = subprocess.Popen(command.split(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,encoding='utf-8')
rawdata = process.stdout.read()
data = rawdata.split()

result = []
progress = len(data)//10
l = progress
recordSize = 11
output = "Job ID,Array Job ID,Cluster,User/Group,State,Cores,CPU Utilized,CPU Efficiency,Job Wall-clock time,Memory Utilized,Memory Efficiency"
for i in range(2,len(data)):
    if '_' in str(i):
        x=5
    else:
        if i>progress:
            print("== "+ str(progress//l*10) + "%" + " of reading input is done ...")
            progress += l
        tmpString = "seff " + str(data[i])
        tmpCommand = subprocess.Popen(tmpString.split(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,encoding='utf-8')
        tmpRawData = tmpCommand.stdout.read()
        tmpData = tmpRawData.split('\n')
        for j in range(0,recordSize):
            result.append(tmpData[j])
        	
l = len(result)
print("== Writing output to file now")
for k in range(0,l):
    if k % recordSize == 0:
        output = output + "\n"    
        continue
    tempo = str(result[k][result[k].find(':')+1:])
    output = output + tempo.strip() + ','
    


file = open("data.txt", "w") 
file.writelines(output) 
file.close()    
print("== Completed!")
