from random import choice
import random
ctmax=5000
cntmax=250
p=[0]*81
base=[1,2,3,4,5,6,7,8,9]
# Create Numbers in Row 1 and Empty "Not Allowed" List
random.shuffle(base)
p[0]=base[0]
p[1]=base[1]
p[2]=base[2]
p[3]=base[3]
p[4]=base[4]
p[5]=base[5]
p[6]=base[6]
p[7]=base[7]
p[8]=base[8]
base=[1,2,3,4,5,6,7,8,9]


def chk():
  global r1,r2,r3,r4,r5,r6,r7,r8,r9,c1,c2,c3,c4,c5,c6,c7,c8,c9,g1,g2,g3,g4,g5,g6,g7,g8,g9,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72,a73,a74,a75,a76,a77,a78,a79,a80,la09,la10,la11,la12,la13,la14,la15,la16,la17,la18,la19,la20,la21,la22,la23,la24,la25,la26,la27,la28,la29,la30,la31,la32,la33,la34,la35,la36,la37,la38,la39,la40,la41,la42,la43,la44,la45,la46,la47,la48,la49,la50,la51,la52,la53,la54,la55,la56,la57,la58,la59,la60,la61,la62,la63,la64,la65,la66,la67,la68,la69,la70,la71,la72,la73,la74,la75,la76,la77,la78,la79,la80,aall,p,aall2,length_aall2,y,yy,min_len_aall2
  
  
  i1=0
  i2=9
  i3=18
  i4=27
  i5=36
  i6=45
  i7=54
  i8=63
  i9=72
  
  r1=(p)[i1:i2]
  r2=(p)[i2:i3]
  r3=(p)[i3:i4]
  r4=(p)[i4:i5]
  r5=(p)[i5:i6]
  r6=(p)[i6:i7]
  r7=(p)[i7:i8]
  r8=(p)[i8:i9]
  r9=(p)[i9:len(p)]
  
  c1=[p[i1+0],p[i2+0],p[i3+0],p[i4+0],p[i5+0],p[i6+0],p[i7+0],p[i8+0],p[i9+0]]
  c2=[p[i1+1],p[i2+1],p[i3+1],p[i4+1],p[i5+1],p[i6+1],p[i7+1],p[i8+1],p[i9+1]]
  c3=[p[i1+2],p[i2+2],p[i3+2],p[i4+2],p[i5+2],p[i6+2],p[i7+2],p[i8+2],p[i9+2]]
  c4=[p[i1+3],p[i2+3],p[i3+3],p[i4+3],p[i5+3],p[i6+3],p[i7+3],p[i8+3],p[i9+3]]
  c5=[p[i1+4],p[i2+4],p[i3+4],p[i4+4],p[i5+4],p[i6+4],p[i7+4],p[i8+4],p[i9+4]]
  c6=[p[i1+5],p[i2+5],p[i3+5],p[i4+5],p[i5+5],p[i6+5],p[i7+5],p[i8+5],p[i9+5]]
  c7=[p[i1+6],p[i2+6],p[i3+6],p[i4+6],p[i5+6],p[i6+6],p[i7+6],p[i8+6],p[i9+6]]
  c8=[p[i1+7],p[i2+7],p[i3+7],p[i4+7],p[i5+7],p[i6+7],p[i7+7],p[i8+7],p[i9+7]]
  c9=[p[i1+8],p[i2+8],p[i3+8],p[i4+8],p[i5+8],p[i6+8],p[i7+8],p[i8+8],p[i9+8]]
  
  g1=[p[i1+0],p[i1+1],p[i1+2],p[i2+0],p[i2+1],p[i2+2],p[i3+0],p[i3+1],p[i3+2]]
  g2=[p[i1+3],p[i1+4],p[i1+5],p[i2+3],p[i2+4],p[i2+5],p[i3+3],p[i3+4],p[i3+5]]
  g3=[p[i1+6],p[i1+7],p[i1+8],p[i2+6],p[i2+7],p[i2+8],p[i3+6],p[i3+7],p[i3+8]]
  g4=[p[i4+0],p[i4+1],p[i4+2],p[i5+0],p[i5+1],p[i5+2],p[i6+0],p[i6+1],p[i6+2]]
  g5=[p[i4+3],p[i4+4],p[i4+5],p[i5+3],p[i5+4],p[i5+5],p[i6+3],p[i6+4],p[i6+5]]
  g6=[p[i4+6],p[i4+7],p[i4+8],p[i5+6],p[i5+7],p[i5+8],p[i6+6],p[i6+7],p[i6+8]]
  g7=[p[i7+0],p[i7+1],p[i7+2],p[i8+0],p[i8+1],p[i8+2],p[i9+0],p[i9+1],p[i9+2]]
  g8=[p[i7+3],p[i7+4],p[i7+5],p[i8+3],p[i8+4],p[i8+5],p[i9+3],p[i9+4],p[i9+5]]
  g9=[p[i7+6],p[i7+7],p[i7+8],p[i8+6],p[i8+7],p[i8+8],p[i9+6],p[i9+7],p[i9+8]]
  

  
  nna09=sorted(r2+c1+g1)
  na09=[]
  for i in nna09:
    if i not in na09:
      na09.append(i)
    if na09[0] == 0:
      na09.remove(0)
  a09=[x for x in base + na09 if x not in base or x not in na09]
  la09=len(a09)

  nna10=sorted(r2+c2+g1)
  na10=[]
  for i in nna10:
    if i not in na10:
      na10.append(i)
    if na10[0] == 0:
      na10.remove(0)
  a10=[x for x in base + na10 if x not in base or x not in na10]
  la10=len(a10)

  nna11=sorted(r2+c3+g1)
  na11=[]
  for i in nna11:
    if i not in na11:
      na11.append(i)
    if na11[0] == 0:
      na11.remove(0)
  a11=[x for x in base + na11 if x not in base or x not in na11]
  la11=len(a11)

  nna12=sorted(r2+c4+g2)
  na12=[]
  for i in nna12:
    if i not in na12:
      na12.append(i)
    if na12[0] == 0:
      na12.remove(0)
  a12=[x for x in base + na12 if x not in base or x not in na12]
  la12=len(a12)

  nna13=sorted(r2+c5+g2)
  na13=[]
  for i in nna13:
    if i not in na13:
      na13.append(i)
    if na13[0] == 0:
      na13.remove(0)
  a13=[x for x in base + na13 if x not in base or x not in na13]
  la13=len(a13)

  nna14=sorted(r2+c6+g2)
  na14=[]
  for i in nna14:
    if i not in na14:
      na14.append(i)
    if na14[0] == 0:
      na14.remove(0)
  a14=[x for x in base + na14 if x not in base or x not in na14]
  la14=len(a14)

  nna15=sorted(r2+c7+g3)
  na15=[]
  for i in nna15:
    if i not in na15:
      na15.append(i)
    if na15[0] == 0:
      na15.remove(0)
  a15=[x for x in base + na15 if x not in base or x not in na15]
  la15=len(a15)

  nna16=sorted(r2+c8+g3)
  na16=[]
  for i in nna16:
    if i not in na16:
      na16.append(i)
    if na16[0] == 0:
      na16.remove(0)
  a16=[x for x in base + na16 if x not in base or x not in na16]
  la16=len(a16)

  nna17=sorted(r2+c9+g3)
  na17=[]
  for i in nna17:
    if i not in na17:
      na17.append(i)
    if na17[0] == 0:
      na17.remove(0)
  a17=[x for x in base + na17 if x not in base or x not in na17]
  la17=len(a17)




  nna18=sorted(r3+c1+g1)
  na18=[]
  for i in nna18:
    if i not in na18:
      na18.append(i)
    if na18[0] == 0:
      na18.remove(0)
  a18=[x for x in base + na18 if x not in base or x not in na18]
  la18=len(a18)

  nna19=sorted(r3+c2+g1)
  na19=[]
  for i in nna19:
    if i not in na19:
      na19.append(i)
    if na19[0] == 0:
      na19.remove(0)
  a19=[x for x in base + na19 if x not in base or x not in na19]
  la19=len(a19)

  nna20=sorted(r3+c3+g1)
  na20=[]
  for i in nna20:
    if i not in na20:
      na20.append(i)
    if na20[0] == 0:
      na20.remove(0)
  a20=[x for x in base + na20 if x not in base or x not in na20]
  la20=len(a20)

  nna21=sorted(r3+c4+g2)
  na21=[]
  for i in nna21:
    if i not in na21:
      na21.append(i)
    if na21[0] == 0:
      na21.remove(0)
  a21=[x for x in base + na21 if x not in base or x not in na21]
  la21=len(a21)

  nna22=sorted(r3+c5+g2)
  na22=[]
  for i in nna22:
    if i not in na22:
      na22.append(i)
    if na22[0] == 0:
      na22.remove(0)
  a22=[x for x in base + na22 if x not in base or x not in na22]
  la22=len(a22)

  nna23=sorted(r3+c6+g2)
  na23=[]
  for i in nna23:
    if i not in na23:
      na23.append(i)
    if na23[0] == 0:
      na23.remove(0)
  a23=[x for x in base + na23 if x not in base or x not in na23]
  la23=len(a23)

  nna24=sorted(r3+c7+g3)
  na24=[]
  for i in nna24:
    if i not in na24:
      na24.append(i)
    if na24[0] == 0:
      na24.remove(0)
  a24=[x for x in base + na24 if x not in base or x not in na24]
  la24=len(a24)

  nna25=sorted(r3+c8+g3)
  na25=[]
  for i in nna25:
    if i not in na25:
      na25.append(i)
    if na25[0] == 0:
      na25.remove(0)
  a25=[x for x in base + na25 if x not in base or x not in na25]
  la25=len(a25)

  nna26=sorted(r3+c9+g3)
  na26=[]
  for i in nna26:
    if i not in na26:
      na26.append(i)
    if na26[0] == 0:
      na26.remove(0)
  a26=[x for x in base + na26 if x not in base or x not in na26]
  la26=len(a26)




  nna27=sorted(r4+c1+g4)
  na27=[]
  for i in nna27:
    if i not in na27:
      na27.append(i)
    if na27[0] == 0:
      na27.remove(0)
  a27=[x for x in base + na27 if x not in base or x not in na27]
  la27=len(a27)

  nna28=sorted(r4+c2+g4)
  na28=[]
  for i in nna28:
    if i not in na28:
      na28.append(i)
    if na28[0] == 0:
      na28.remove(0)
  a28=[x for x in base + na28 if x not in base or x not in na28]
  la28=len(a28)

  nna29=sorted(r4+c3+g4)
  na29=[]
  for i in nna29:
    if i not in na29:
      na29.append(i)
    if na29[0] == 0:
      na29.remove(0)
  a29=[x for x in base + na29 if x not in base or x not in na29]
  la29=len(a29)

  nna30=sorted(r4+c4+g5)
  na30=[]
  for i in nna30:
    if i not in na30:
      na30.append(i)
    if na30[0] == 0:
      na30.remove(0)
  a30=[x for x in base + na30 if x not in base or x not in na30]
  la30=len(a30)

  nna31=sorted(r4+c5+g5)
  na31=[]
  for i in nna31:
    if i not in na31:
      na31.append(i)
    if na31[0] == 0:
      na31.remove(0)
  a31=[x for x in base + na31 if x not in base or x not in na31]
  la31=len(a31)

  nna32=sorted(r4+c6+g5)
  na32=[]
  for i in nna32:
    if i not in na32:
      na32.append(i)
    if na32[0] == 0:
      na32.remove(0)
  a32=[x for x in base + na32 if x not in base or x not in na32]
  la32=len(a32)

  nna33=sorted(r4+c7+g6)
  na33=[]
  for i in nna33:
    if i not in na33:
      na33.append(i)
    if na33[0] == 0:
      na33.remove(0)
  a33=[x for x in base + na33 if x not in base or x not in na33]
  la33=len(a33)

  nna34=sorted(r4+c8+g6)
  na34=[]
  for i in nna34:
    if i not in na34:
      na34.append(i)
    if na34[0] == 0:
      na34.remove(0)
  a34=[x for x in base + na34 if x not in base or x not in na34]
  la34=len(a34)

  nna35=sorted(r4+c9+g6)
  na35=[]
  for i in nna35:
    if i not in na35:
      na35.append(i)
    if na35[0] == 0:
      na35.remove(0)
  a35=[x for x in base + na35 if x not in base or x not in na35]
  la35=len(a35)




  nna36=sorted(r5+c1+g4)
  na36=[]
  for i in nna36:
    if i not in na36:
      na36.append(i)
    if na36[0] == 0:
      na36.remove(0)
  a36=[x for x in base + na36 if x not in base or x not in na36]
  la36=len(a36)

  nna37=sorted(r5+c2+g4)
  na37=[]
  for i in nna37:
    if i not in na37:
      na37.append(i)
    if na37[0] == 0:
      na37.remove(0)
  a37=[x for x in base + na37 if x not in base or x not in na37]
  la37=len(a37)

  nna38=sorted(r5+c3+g4)
  na38=[]
  for i in nna38:
    if i not in na38:
      na38.append(i)
    if na38[0] == 0:
      na38.remove(0)
  a38=[x for x in base + na38 if x not in base or x not in na38]
  la38=len(a38)

  nna39=sorted(r5+c4+g5)
  na39=[]
  for i in nna39:
    if i not in na39:
      na39.append(i)
    if na39[0] == 0:
      na39.remove(0)
  a39=[x for x in base + na39 if x not in base or x not in na39]
  la39=len(a39)

  nna40=sorted(r5+c5+g5)
  na40=[]
  for i in nna40:
    if i not in na40:
      na40.append(i)
    if na40[0] == 0:
      na40.remove(0)
  a40=[x for x in base + na40 if x not in base or x not in na40]
  la40=len(a40)

  nna41=sorted(r5+c6+g5)
  na41=[]
  for i in nna41:
    if i not in na41:
      na41.append(i)
    if na41[0] == 0:
      na41.remove(0)
  a41=[x for x in base + na41 if x not in base or x not in na41]
  la41=len(a41)

  nna42=sorted(r5+c7+g6)
  na42=[]
  for i in nna42:
    if i not in na42:
      na42.append(i)
    if na42[0] == 0:
      na42.remove(0)
  a42=[x for x in base + na42 if x not in base or x not in na42]
  la42=len(a42)

  nna43=sorted(r5+c8+g6)
  na43=[]
  for i in nna43:
    if i not in na43:
      na43.append(i)
    if na43[0] == 0:
      na43.remove(0)
  a43=[x for x in base + na43 if x not in base or x not in na43]
  la43=len(a43)

  nna44=sorted(r5+c9+g6)
  na44=[]
  for i in nna44:
    if i not in na44:
      na44.append(i)
    if na44[0] == 0:
      na44.remove(0)
  a44=[x for x in base + na44 if x not in base or x not in na44]
  la44=len(a44)




  nna45=sorted(r6+c1+g4)
  na45=[]
  for i in nna45:
    if i not in na45:
      na45.append(i)
    if na45[0] == 0:
      na45.remove(0)
  a45=[x for x in base + na45 if x not in base or x not in na45]
  la45=len(a45)

  nna46=sorted(r6+c2+g4)
  na46=[]
  for i in nna46:
    if i not in na46:
      na46.append(i)
    if na46[0] == 0:
      na46.remove(0)
  a46=[x for x in base + na46 if x not in base or x not in na46]
  la46=len(a46)

  nna47=sorted(r6+c3+g4)
  na47=[]
  for i in nna47:
    if i not in na47:
      na47.append(i)
    if na47[0] == 0:
      na47.remove(0)
  a47=[x for x in base + na47 if x not in base or x not in na47]
  la47=len(a47)

  nna48=sorted(r6+c4+g5)
  na48=[]
  for i in nna48:
    if i not in na48:
      na48.append(i)
    if na48[0] == 0:
      na48.remove(0)
  a48=[x for x in base + na48 if x not in base or x not in na48]
  la48=len(a48)

  nna49=sorted(r6+c5+g5)
  na49=[]
  for i in nna49:
    if i not in na49:
      na49.append(i)
    if na49[0] == 0:
      na49.remove(0)
  a49=[x for x in base + na49 if x not in base or x not in na49]
  la49=len(a49)

  nna50=sorted(r6+c6+g5)
  na50=[]
  for i in nna50:
    if i not in na50:
      na50.append(i)
    if na50[0] == 0:
      na50.remove(0)
  a50=[x for x in base + na50 if x not in base or x not in na50]
  la50=len(a50)

  nna51=sorted(r6+c7+g6)
  na51=[]
  for i in nna51:
    if i not in na51:
      na51.append(i)
    if na51[0] == 0:
      na51.remove(0)
  a51=[x for x in base + na51 if x not in base or x not in na51]
  la51=len(a51)

  nna52=sorted(r6+c8+g6)
  na52=[]
  for i in nna52:
    if i not in na52:
      na52.append(i)
    if na52[0] == 0:
      na52.remove(0)
  a52=[x for x in base + na52 if x not in base or x not in na52]
  la52=len(a52)

  nna53=sorted(r6+c9+g6)
  na53=[]
  for i in nna53:
    if i not in na53:
      na53.append(i)
    if na53[0] == 0:
      na53.remove(0)
  a53=[x for x in base + na53 if x not in base or x not in na53]
  la53=len(a53)





  nna54=sorted(r7+c1+g7)
  na54=[]
  for i in nna54:
    if i not in na54:
      na54.append(i)
    if na54[0] == 0:
      na54.remove(0)
  a54=[x for x in base + na54 if x not in base or x not in na54]
  la54=len(a54)

  nna55=sorted(r7+c2+g7)
  na55=[]
  for i in nna55:
    if i not in na55:
      na55.append(i)
    if na55[0] == 0:
      na55.remove(0)
  a55=[x for x in base + na55 if x not in base or x not in na55]
  la55=len(a55)

  nna56=sorted(r7+c3+g7)
  na56=[]
  for i in nna56:
    if i not in na56:
      na56.append(i)
    if na56[0] == 0:
      na56.remove(0)
  a56=[x for x in base + na56 if x not in base or x not in na56]
  la56=len(a56)

  nna57=sorted(r7+c4+g8)
  na57=[]
  for i in nna57:
    if i not in na57:
      na57.append(i)
    if na57[0] == 0:
      na57.remove(0)
  a57=[x for x in base + na57 if x not in base or x not in na57]
  la57=len(a57)

  nna58=sorted(r7+c5+g8)
  na58=[]
  for i in nna58:
    if i not in na58:
      na58.append(i)
    if na58[0] == 0:
      na58.remove(0)
  a58=[x for x in base + na58 if x not in base or x not in na58]
  la58=len(a58)

  nna59=sorted(r7+c6+g8)
  na59=[]
  for i in nna59:
    if i not in na59:
      na59.append(i)
    if na59[0] == 0:
      na59.remove(0)
  a59=[x for x in base + na59 if x not in base or x not in na59]
  la59=len(a59)

  nna60=sorted(r7+c7+g9)
  na60=[]
  for i in nna60:
    if i not in na60:
      na60.append(i)
    if na60[0] == 0:
      na60.remove(0)
  a60=[x for x in base + na60 if x not in base or x not in na60]
  la60=len(a60)

  nna61=sorted(r7+c8+g9)
  na61=[]
  for i in nna61:
    if i not in na61:
      na61.append(i)
    if na61[0] == 0:
      na61.remove(0)
  a61=[x for x in base + na61 if x not in base or x not in na61]
  la61=len(a61)

  nna62=sorted(r7+c9+g9)
  na62=[]
  for i in nna62:
    if i not in na62:
      na62.append(i)
    if na62[0] == 0:
      na62.remove(0)
  a62=[x for x in base + na62 if x not in base or x not in na62]
  la62=len(a62)





  nna63=sorted(r8+c1+g7)
  na63=[]
  for i in nna63:
    if i not in na63:
      na63.append(i)
    if na63[0] == 0:
      na63.remove(0)
  a63=[x for x in base + na63 if x not in base or x not in na63]
  la63=len(a63)

  nna64=sorted(r8+c2+g7)
  na64=[]
  for i in nna64:
    if i not in na64:
      na64.append(i)
    if na64[0] == 0:
      na64.remove(0)
  a64=[x for x in base + na64 if x not in base or x not in na64]
  la64=len(a64)

  nna65=sorted(r8+c3+g7)
  na65=[]
  for i in nna65:
    if i not in na65:
      na65.append(i)
    if na65[0] == 0:
      na65.remove(0)
  a65=[x for x in base + na65 if x not in base or x not in na65]
  la65=len(a65)

  nna66=sorted(r8+c4+g8)
  na66=[]
  for i in nna66:
    if i not in na66:
      na66.append(i)
    if na66[0] == 0:
      na66.remove(0)
  a66=[x for x in base + na66 if x not in base or x not in na66]
  la66=len(a66)

  nna67=sorted(r8+c5+g8)
  na67=[]
  for i in nna67:
    if i not in na67:
      na67.append(i)
    if na67[0] == 0:
      na67.remove(0)
  a67=[x for x in base + na67 if x not in base or x not in na67]
  la67=len(a67)

  nna68=sorted(r8+c6+g8)
  na68=[]
  for i in nna68:
    if i not in na68:
      na68.append(i)
    if na68[0] == 0:
      na68.remove(0)
  a68=[x for x in base + na68 if x not in base or x not in na68]
  la68=len(a68)

  nna69=sorted(r8+c7+g9)
  na69=[]
  for i in nna69:
    if i not in na69:
      na69.append(i)
    if na69[0] == 0:
      na69.remove(0)
  a69=[x for x in base + na69 if x not in base or x not in na69]
  la69=len(a69)

  nna70=sorted(r8+c8+g9)
  na70=[]
  for i in nna70:
    if i not in na70:
      na70.append(i)
    if na70[0] == 0:
      na70.remove(0)
  a70=[x for x in base + na70 if x not in base or x not in na70]
  la70=len(a70)

  nna71=sorted(r8+c9+g9)
  na71=[]
  for i in nna71:
    if i not in na71:
      na71.append(i)
    if na71[0] == 0:
      na71.remove(0)
  a71=[x for x in base + na71 if x not in base or x not in na71]
  la71=len(a71)





  nna72=sorted(r9+c1+g7)
  na72=[]
  for i in nna72:
    if i not in na72:
      na72.append(i)
    if na72[0] == 0:
      na72.remove(0)
  a72=[x for x in base + na72 if x not in base or x not in na72]
  la72=len(a72)

  nna73=sorted(r9+c2+g7)
  na73=[]
  for i in nna73:
    if i not in na73:
      na73.append(i)
    if na73[0] == 0:
      na73.remove(0)
  a73=[x for x in base + na73 if x not in base or x not in na73]
  la73=len(a73)

  nna74=sorted(r9+c3+g7)
  na74=[]
  for i in nna74:
    if i not in na74:
      na74.append(i)
    if na74[0] == 0:
      na74.remove(0)
  a74=[x for x in base + na74 if x not in base or x not in na74]
  la74=len(a74)

  nna75=sorted(r9+c4+g8)
  na75=[]
  for i in nna75:
    if i not in na75:
      na75.append(i)
    if na75[0] == 0:
      na75.remove(0)
  a75=[x for x in base + na75 if x not in base or x not in na75]
  la75=len(a75)

  nna76=sorted(r9+c5+g8)
  na76=[]
  for i in nna76:
    if i not in na76:
      na76.append(i)
    if na76[0] == 0:
      na76.remove(0)
  a76=[x for x in base + na76 if x not in base or x not in na76]
  la76=len(a76)

  nna77=sorted(r9+c6+g8)
  na77=[]
  for i in nna77:
    if i not in na77:
      na77.append(i)
    if na77[0] == 0:
      na77.remove(0)
  a77=[x for x in base + na77 if x not in base or x not in na77]
  la77=len(a77)

  nna78=sorted(r9+c7+g9)
  na78=[]
  for i in nna78:
    if i not in na78:
      na78.append(i)
    if na78[0] == 0:
      na78.remove(0)
  a78=[x for x in base + na78 if x not in base or x not in na78]
  la78=len(a78)

  nna79=sorted(r9+c8+g9)
  na79=[]
  for i in nna79:
    if i not in na79:
      na79.append(i)
    if na79[0] == 0:
      na79.remove(0)
  a79=[x for x in base + na79 if x not in base or x not in na79]
  la79=len(a79)

  nna80=sorted(r9+c9+g9)
  na80=[]
  for i in nna80:
    if i not in na80:
      na80.append(i)
    if na80[0] == 0:
      na80.remove(0)
  a80=[x for x in base + na80 if x not in base or x not in na80]
  la80=len(a80)
  aall=[1,1,1,1,1,1,1,1,1,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72,a73,a74,a75,a76,a77,a78,a79,a80]
  
  # was seperate function "len_chk()
  y=0
  aall2=[]
  while True:
    if p[y] != 0:
      aall2.append([1,1,1,1,1,1,1,1,1,1])
    if p[y] == 0:
      aall2.append(aall[y])
    y=y+1
    if y < 81:
      continue
    break
  
  yy=0
  length_aall2=[]
  while True:
    length_aall2.append(len(aall2[yy]))
    yy=yy+1
    if yy < 81:
      continue
    min_len_aall2=min(length_aall2)
    break

def core():
  global min_index_pos,cnt,cntmax,length_aall2,min_len_aall2,aall,aall2,p
  cnt=0
  while True:
    if cnt > cntmax:
      print("ERROR QUITTING -- Loop Count Reached in Function:  core()")
      quit()
    chk()
    min_index_pos=length_aall2.index(min_len_aall2)
    if min_len_aall2 == 1:
      p[min_index_pos]=choice(aall[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_aall2 == 2:
      p[min_index_pos]=choice(aall[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_aall2 == 3:
      p[min_index_pos]=choice(aall[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_aall2 == 4:
      p[min_index_pos]=choice(aall[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_aall2 == 5:
      p[min_index_pos]=choice(aall[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_aall2 == 6:
      p[min_index_pos]=choice(aall[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_aall2 == 7:
      p[min_index_pos]=choice(aall[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_aall2 == 8:
      p[min_index_pos]=choice(aall[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_aall2 == 9:
      p[min_index_pos]=choice(aall[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_aall2 == 0:
      # print("Empty Array --- Breaking Out of Function:  core()")
      break
    break

def chk2():
  i=12
  v=0
  while True:
    chk()
    rn=[r2,r3,r4,r5,r6,r7,r8,r9]
    loc=[0,1,2,3,4,5,6,7]
    if 0 in rn[loc[v]]:
      p[i]=0
      i=i+1
      p[i]=0
      i=i+1
      p[i]=0
      i=i+1
      p[i]=0
      i=i+1
      p[i]=0
      i=i+1
      p[i]=0
      i=i+4
    if 0 not in rn[loc[v]]:
        i=i+9
    if loc[v] == 7:
      break
    v=v+1
    continue



def final_chk():
  if base == sorted(r1) and base == sorted(r2) and base == sorted(r3) and base == sorted(r4) and base == sorted(r5) and base == sorted(r6) and base == sorted(r7) and base == sorted(r8) and base == sorted(r9) and base == sorted(g1) and base == sorted(g2) and base == sorted(g3) and base == sorted(g4) and base == sorted(g5) and base == sorted(g6) and base == sorted(g7) and base == sorted(g8) and base == sorted(g9) and base == sorted(c1) and base == sorted(c2) and base == sorted(c3) and base == sorted(c4) and base == sorted(c5) and base == sorted(c6) and base == sorted(c7) and base == sorted(c8) and base == sorted(c9):
    print("-----Final Check PASS-----")
  else:
    print("-----Final Check FAIL-----")

def grid_print():# Print Suduko Grid with zero values
  print("█■■■■■■■■■█■■■■■■■■■█■■■■■■■■■█")
  print("█ "+str(p[0])+"  " +str(p[1])+"  " +str(p[2]) +" █ "+str(p[3])+"  " +str(p[4])+"  " +str(p[5]) +" █ "+str(p[6]) +"  "+str(p[7]) +"  "+str(p[8]) +" █ ")
  print("█ "+str(p[9])+"  " +str(p[10])+"  "+str(p[11])+" █ "+str(p[12])+"  "+str(p[13])+"  "+str(p[14])+" █ "+str(p[15])+"  "+str(p[16])+"  "+str(p[17])+" █ ")
  print("█ "+str(p[18])+"  "+str(p[19])+"  "+str(p[20])+" █ "+str(p[21])+"  "+str(p[22])+"  "+str(p[23])+" █ "+str(p[24])+"  "+str(p[25])+"  "+str(p[26])+" █ ")
  print("█■■■■■■■■■█■■■■■■■■■█■■■■■■■■■█")
  print("█ "+str(p[27])+"  "+str(p[28])+"  "+str(p[29])+" █ "+str(p[30])+"  "+str(p[31])+"  "+str(p[32])+" █ "+str(p[33])+"  "+str(p[34])+"  "+str(p[35])+" █ ")
  print("█ "+str(p[36])+"  "+str(p[37])+"  "+str(p[38])+" █ "+str(p[39])+"  "+str(p[40])+"  "+str(p[41])+" █ "+str(p[42])+"  "+str(p[43])+"  "+str(p[44])+" █ ")
  print("█ "+str(p[45])+"  "+str(p[46])+"  "+str(p[47])+" █ "+str(p[48])+"  "+str(p[49])+"  "+str(p[50])+" █ "+str(p[51])+"  "+str(p[52])+"  "+str(p[53])+" █ ")
  print("█■■■■■■■■■█■■■■■■■■■█■■■■■■■■■█")
  print("█ "+str(p[54])+"  "+str(p[55])+"  "+str(p[56])+" █ "+str(p[57])+"  "+str(p[58])+"  "+str(p[59])+" █ "+str(p[60])+"  "+str(p[61])+"  "+str(p[62])+" █ ")
  print("█ "+str(p[63])+"  "+str(p[64])+"  "+str(p[65])+" █ "+str(p[66])+"  "+str(p[67])+"  "+str(p[68])+" █ "+str(p[69])+"  "+str(p[70])+"  "+str(p[71])+" █ ")
  print("█ "+str(p[72])+"  "+str(p[73])+"  "+str(p[74])+" █ "+str(p[75])+"  "+str(p[76])+"  "+str(p[77])+" █ "+str(p[78])+"  "+str(p[79])+"  "+str(p[80])+" █ ")
  print("█■■■■■■■■■█■■■■■■■■■█■■■■■■■■■█")
  print("")

def grid_print_places():# Print Suduko Grid with values marking the array position
  print("█■■■■■■■■■■■■█■■■■■■■■■■■■█■■■■■■■■■■■■█")
  print("█ "+"00"+"  "+"01"+"  "+"02"+" █ "+"03"+"  "+"04"+"  "+"05"+" █ "+"06"+"  "+"07"+"  "+"08"+" █ ")
  print("█ "+"09"+"  "+"10"+"  "+"11"+" █ "+"12"+"  "+"13"+"  "+"14"+" █ "+"15"+"  "+"16"+"  "+"17"+" █ ")
  print("█ "+"18"+"  "+"19"+"  "+"20"+" █ "+"21"+"  "+"22"+"  "+"23"+" █ "+"24"+"  "+"25"+"  "+"26"+" █ ")
  print("█■■■■■■■■■■■■█■■■■■■■■■■■■█■■■■■■■■■■■■█")
  print("█ "+"27"+"  "+"28"+"  "+"29"+" █ "+"30"+"  "+"31"+"  "+"32"+" █ "+"33"+"  "+"34"+"  "+"35"+" █ ")
  print("█ "+"36"+"  "+"37"+"  "+"38"+" █ "+"39"+"  "+"40"+"  "+"41"+" █ "+"42"+"  "+"43"+"  "+"44"+" █ ")
  print("█ "+"45"+"  "+"46"+"  "+"47"+" █ "+"48"+"  "+"49"+"  "+"50"+" █ "+"51"+"  "+"52"+"  "+"53"+" █ ")
  print("█■■■■■■■■■■■■█■■■■■■■■■■■■█■■■■■■■■■■■■█")
  print("█ "+"54"+"  "+"55"+"  "+"56"+" █ "+"57"+"  "+"58"+"  "+"59"+" █ "+"60"+"  "+"61"+"  "+"62"+" █ ")
  print("█ "+"63"+"  "+"64"+"  "+"65"+" █ "+"66"+"  "+"67"+"  "+"68"+" █ "+"69"+"  "+"70"+"  "+"71"+" █ ")
  print("█ "+"72"+"  "+"73"+"  "+"74"+" █ "+"75"+"  "+"76"+"  "+"77"+" █ "+"78"+"  "+"79"+"  "+"80"+" █ ")
  print("█■■■■■■■■■■■■█■■■■■■■■■■■■█■■■■■■■■■■■■█")
  print("")

def grid_print_places_android():# Print Suduko Grid with values marking the array position
  print("============================")
  print("█ "+"00"+"  "+"01"+"  "+"02"+" █ "+"03"+"  "+"04"+"  "+"05"+" █ "+"06"+"  "+"07"+"  "+"08"+" █ ")
  print("█ "+"09"+"  "+"10"+"  "+"11"+" █ "+"12"+"  "+"13"+"  "+"14"+" █ "+"15"+"  "+"16"+"  "+"17"+" █ ")
  print("█ "+"18"+"  "+"19"+"  "+"20"+" █ "+"21"+"  "+"22"+"  "+"23"+" █ "+"24"+"  "+"25"+"  "+"26"+" █ ")
  print("============================")
  print("█ "+"27"+"  "+"28"+"  "+"29"+" █ "+"30"+"  "+"31"+"  "+"32"+" █ "+"33"+"  "+"34"+"  "+"35"+" █ ")
  print("█ "+"36"+"  "+"37"+"  "+"38"+" █ "+"39"+"  "+"40"+"  "+"41"+" █ "+"42"+"  "+"43"+"  "+"44"+" █ ")
  print("█ "+"45"+"  "+"46"+"  "+"47"+" █ "+"48"+"  "+"49"+"  "+"50"+" █ "+"51"+"  "+"52"+"  "+"53"+" █ ")
  print("============================")
  print("█ "+"54"+"  "+"55"+"  "+"56"+" █ "+"57"+"  "+"58"+"  "+"59"+" █ "+"60"+"  "+"61"+"  "+"62"+" █ ")
  print("█ "+"63"+"  "+"64"+"  "+"65"+" █ "+"66"+"  "+"67"+"  "+"68"+" █ "+"69"+"  "+"70"+"  "+"71"+" █ ")
  print("█ "+"72"+"  "+"73"+"  "+"74"+" █ "+"75"+"  "+"76"+"  "+"77"+" █ "+"78"+"  "+"79"+"  "+"80"+" █ ")
  print("============================")
  print("")

def grid_print_android():# Print Suduko Grid with zero values
  print("=========================")
  print("█  "+str(p[0])+"   " +str(p[1])+"   " +str(p[2]) +"  █  "+str(p[3])+"   " +str(p[4])+"   " +str(p[5]) +"  █  "+str(p[6]) +"   "+str(p[7]) +"   "+str(p[8]) +"  █ ")
  print("█  "+str(p[9])+"   " +str(p[10])+"   "+str(p[11])+"  █  "+str(p[12])+"   "+str(p[13])+"   "+str(p[14])+"  █  "+str(p[15])+"   "+str(p[16])+"   "+str(p[17])+"  █ ")
  print("█  "+str(p[18])+"   "+str(p[19])+"   "+str(p[20])+"  █  "+str(p[21])+"   "+str(p[22])+"   "+str(p[23])+"  █  "+str(p[24])+"   "+str(p[25])+"   "+str(p[26])+"  █ ")
  print("=========================")
  print("█  "+str(p[27])+"   "+str(p[28])+"   "+str(p[29])+"  █  "+str(p[30])+"   "+str(p[31])+"   "+str(p[32])+"  █  "+str(p[33])+"   "+str(p[34])+"   "+str(p[35])+"  █ ")
  print("█  "+str(p[36])+"   "+str(p[37])+"   "+str(p[38])+"  █  "+str(p[39])+"   "+str(p[40])+"   "+str(p[41])+"  █  "+str(p[42])+"   "+str(p[43])+"   "+str(p[44])+"  █ ")
  print("█  "+str(p[45])+"   "+str(p[46])+"   "+str(p[47])+"  █  "+str(p[48])+"   "+str(p[49])+"   "+str(p[50])+"  █  "+str(p[51])+"   "+str(p[52])+"   "+str(p[53])+"  █ ")
  print("=========================")
  print("█  "+str(p[54])+"   "+str(p[55])+"   "+str(p[56])+"  █  "+str(p[57])+"   "+str(p[58])+"   "+str(p[59])+"  █  "+str(p[60])+"   "+str(p[61])+"   "+str(p[62])+"  █ ")
  print("█  "+str(p[63])+"   "+str(p[64])+"   "+str(p[65])+"  █  "+str(p[66])+"   "+str(p[67])+"   "+str(p[68])+"  █  "+str(p[69])+"   "+str(p[70])+"   "+str(p[71])+"  █ ")
  print("█  "+str(p[72])+"   "+str(p[73])+"   "+str(p[74])+"  █  "+str(p[75])+"   "+str(p[76])+"   "+str(p[77])+"  █  "+str(p[78])+"   "+str(p[79])+"   "+str(p[80])+"  █ ")
  print("=========================")
  print("")


# grid_print_places()
# grid_print_places_android()


cnt2=0
while True:
  chk()
  core()
  if 0 in p and cnt2 <= 15:
    cnt2=cnt2+1
    chk2()
    continue
  if cnt2 > 15:
    print("cnt2 Count Reached --- Breaking Out of Loop")
    break
  break
chk()
# grid_print()
grid_print_android()
final_chk()





'''
while True:
  nna=sorted(r2+c1+g1)
  na=[]
  for i in nna:
    if i not in na:
      na.append(i)
    if na[0] == 0:
      na.remove(0)
  a=[x for x in base + na if x not in base or x not in na]
  la=len(a)
  break


(r2+c1+g1)
(r2+c2+g1)
(r2+c3+g1)
(r2+c4+g2)
(r2+c5+g2)
(r2+c6+g2)
(r2+c7+g3)
(r2+c8+g3)
(r2+c9+g3)

(r3+c1+g1)


ri=
'''





