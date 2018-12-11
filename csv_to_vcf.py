#csv to vcf converter

read= open("contacts.csv","r")
text=read.readlines()
lines = [line.rstrip('\n') for line in text]
read.close

file= open("output.vcf","w")

for line in lines:

 nme=0
 name=""
 ph=""
 for char in line:
   if char==',':
      nme=1
   elif nme==0:
      name=name+char
   elif nme==1:
      ph=ph+char

 lname=""
 fname=""
 s=0
 for na in name:
  if na==" ":
   s=1
  elif s==0:
   fname=fname+na
  elif s==1:
   lname=lname+na
   
 file.write("BEGIN:VCARD\nVERSION:3.0\nN:")
 file.write(lname+";"+fname+";;;\n")
 file.write("FN:"+name+"\nTEL;VOICE:"+ph+"\n")
 file.write("END:VCARD\n")
print ("Conversion Finished Successfully")
file.close

file= open("output.vcf","a")
file.close

