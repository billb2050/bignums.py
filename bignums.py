#!/usr/bin/python3
"""
    This programs breaks down numbers into their word parts

    By: Bill Blasingim
    On: 08/24/2007

"""
import string

def FormatNumberWords(str1):
  if str1=="":return
  p=str1.find(",")
  if p<0:
    temp=""
    sep=""
    str1=str(int(str1))
    i=len(str1)-1
    j=0
    while i>=0:
      temp=str1[i]+sep+temp
      j+=1
      if j%3==0:
        sep=","
      else:
        sep=""      
      i-=1
    str1=temp
    
  tbl = {}
  tbl[0]=""
  tbl[1]="Thousand"  
  tbl[2]="Million"  
  tbl[3]="Billion"  
  tbl[4]="Trillion"  
  tbl[5]="Quadrillion"  
  tbl[6]="Quintillion"  
  tbl[7]="Sextillion"  
  tbl[8]="Septillion"  
  tbl[9]="Octillion"  
  tbl[10]="Nonillion"  
  tbl[11]="Decillion"  
  tbl[12]="Undecillion"  
  tbl[13]="Duodecillion"  
  tbl[14]="Tredecillion"  
  tbl[15]="Quattuordecillion"  
  tbl[16]="Quindecillion"  
  tbl[17]="Sexdecillion"  
  tbl[18]="Septendecillion"  
  tbl[19]="Octodecillion"  
  tbl[20]="Novemdecillion"

  NumWords=""
  lst=str1.split(",")
  #print min(lst), max(lst)
  j=len(lst)-1
  #print j

  sep=""
  for i in lst:
    if len(i)>3:return
    #if i=="000":
    if int(i)==0:      
      j-=1
      continue
    NumWords=NumWords+sep+ str(int(i)).strip()
    NumWords=NumWords+ " "+tbl[j]
    sep=","
    j-=1

  return(NumWords.rstrip())

def PrintWords(str1):
  print(str1)
  lst=FormatNumberWords(str1).split(",")
  print("     or...")
  for i in lst: print(i)
  print("")

while 1:
  PrintWords("0045")
  PrintWords("789,456,123,147,852")  
  PrintWords("12,345")

  PrintWords("12345")
  PrintWords("75336915995178945612314785")

  PrintWords("789,456,123")

  PrintWords("789,000,123")

  PrintWords("789,456,123,147,852")

  PrintWords("789,000,023,000,852")

  PrintWords("789,456,000,000,852")

  PrintWords("789,456,123,000,000")

  PrintWords("789,456,123,147,000")

  PrintWords("951,789,456,123,147,852")

  PrintWords("159,951,789,456,123,147,852")

  PrintWords("369,159,951,789,456,123,147,852")

  PrintWords("753,369,159,951,789,456,123,147,852")

  PrintWords("753,369,000,951,789,000,123,147,852")

  break
