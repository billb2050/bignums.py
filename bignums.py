#!/usr/bin/python3
"""
    This programs breaks down numbers into their word parts
    It assumes you can pronounce hundreds!

    By: Bill Blasingim
    On: 08/24/2007

  10/22/2020 Increase number part table from 20 to 101 parts.
            Can now describe numbers over 300 digits!
            This data came from:
            https://www.quora.com/What-comes-after-a-million-billion-trillion
  10/23/2020 Add generate huge random number test. 
  04/23/2024 Increase number part table from 101 to 104 parts    

"""
import string, random

random.seed()

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
  # this data came from https://www.quora.com/What-comes-after-a-million-billion-trillion
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
  tbl[21]="vigintillion"
  tbl[22]="unvigintillion"
  tbl[23]="duovigintillion"
  tbl[24]="trevigintillion"
  tbl[25]="quattuorvigintillion"
  tbl[26]="quinvigintillion"
  tbl[27]="sexvigintillion"
  tbl[28]="septenvigintillion"
  tbl[29]="octovigintillion"
  tbl[30]="novemvigintillion"
  tbl[31]="trigintillion"
  tbl[32]="untrigintillion"
  tbl[33]="duotrigintillion"
  tbl[34]="tretrigintillion"
  tbl[35]="quattuortrigintillion"
  tbl[36]="quintrigintillion"
  tbl[37]="sextrigintillion"
  tbl[38]="septtrigintillion"
  tbl[39]="octotrigintillion"
  tbl[40]="novemtrigintillion"
  tbl[41]="quardragintillion"
  tbl[42]="unquardragintillion"
  tbl[43]="duoquardragintillion"
  tbl[44]="trequardragintillion"
  tbl[45]="quattuorquardragintillion"
  tbl[46]="quinquardragintillion"
  tbl[47]="sexquardragintillion"
  tbl[48]="septquardragintillion"
  tbl[49]="octoquardragintillion"
  tbl[50]="novemquardragintillion"
  tbl[51]="quinquagintillion"
  tbl[52]="unquinquagintillion"
  tbl[53]="duoquinquagintillion"
  tbl[54]="trequinquagintillion"
  tbl[55]="quattuorquinquagintillion"
  tbl[56]="quinquinquagintillion"
  tbl[57]="sexquinquagintillion"
  tbl[58]="septquinquagintillion"
  tbl[59]="octoquinquagintillion"
  tbl[60]="novemquinquagintillion"
  tbl[61]="sexagintillion"
  tbl[62]="unsexagintillion"
  tbl[63]="duosexagintillion"
  tbl[64]="tresexagintillion"
  tbl[65]="quattuorsexagintillion"
  tbl[66]="quinsexagintillion"
  tbl[67]="sexsexagintillion"
  tbl[68]="septsexagintillion"
  tbl[69]="octosexagintillion"
  tbl[70]="novemsexagintillion"
  tbl[71]="septuagintillion"
  tbl[72]="unseptuagintillion"
  tbl[73]="duoseptuagintillion"
  tbl[74]="treseptuagintillion"
  tbl[75]="quattuorseptuagintillion"
  tbl[76]="quinseptuagintillion"
  tbl[77]="sexseptuagintillion"
  tbl[78]="septseptuagintillion"
  tbl[79]="octoseptuagintillion"
  tbl[80]="novemseptuagintillion"
  tbl[81]="octogintillion"
  tbl[82]="unoctogintillion"
  tbl[83]="duooctogintillion"
  tbl[84]="treoctogintillion"
  tbl[85]="quattuoroctogintillion"
  tbl[86]="quinoctogintillion"
  tbl[87]="sexoctogintillion"
  tbl[88]="septoctogintillion"
  tbl[89]="octooctogintillion"
  tbl[90]="novemoctogintillion"
  tbl[91]="nonagintillion"
  tbl[92]="unnonagintillion"
  tbl[93]="duononagintillion"
  tbl[94]="trenonagintillion"
  tbl[95]="quattuornonagintillion"
  tbl[96]="quinnonagintillion"
  tbl[97]="sexnonagintillion"
  tbl[98]="septnonagintillion"
  tbl[99]="octononagintillion"
  tbl[100]="novemnonagintillion"
  tbl[101]="centillion"
  tbl[102]="Uncentillion"
  tbl[103]="Duocentillion"
  tbl[104]="Trescentillion"

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
  PrintWords("00457")
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

    # Generate huge random number
  cnt=0
  bigNum=""
  while True:
    digit=random.randrange(0,10)
    bigNum+=str(digit)
    cnt+=1
    if cnt>=300:break

  print(len(bigNum))
  PrintWords(bigNum)  

  break
