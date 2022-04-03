import random
cntmax=250
p=[0]*81
base=[1,2,3,4,5,6,7,8,9]
def core_1():
  global p, r1, r2, r3, r4, r5, r6, r7, r8, r9, c1, c2, c3, c4, c5, c6, c7, c8, c9, g1, g2, g3, g4, g5, g6, g7, g8, g9, a, al, length_al, min_len_al, nna, na
  # Combines the cells of variable (p) into lists broken down into their rows
  r1=(p)[0:9]
  r2=(p)[9:18]
  r3=(p)[18:27]
  r4=(p)[27:36]
  r5=(p)[36:45]
  r6=(p)[45:54]
  r7=(p)[54:63]
  r8=(p)[63:72]
  r9=(p)[72:81]
  # Combines the cells of variable (p) into lists broken down into their columns
  c1=[p[0+0],p[9+0],p[18+0],p[27+0],p[36+0],p[45+0],p[54+0],p[63+0],p[72+0]]
  c2=[p[0+1],p[9+1],p[18+1],p[27+1],p[36+1],p[45+1],p[54+1],p[63+1],p[72+1]]
  c3=[p[0+2],p[9+2],p[18+2],p[27+2],p[36+2],p[45+2],p[54+2],p[63+2],p[72+2]]
  c4=[p[0+3],p[9+3],p[18+3],p[27+3],p[36+3],p[45+3],p[54+3],p[63+3],p[72+3]]
  c5=[p[0+4],p[9+4],p[18+4],p[27+4],p[36+4],p[45+4],p[54+4],p[63+4],p[72+4]]
  c6=[p[0+5],p[9+5],p[18+5],p[27+5],p[36+5],p[45+5],p[54+5],p[63+5],p[72+5]]
  c7=[p[0+6],p[9+6],p[18+6],p[27+6],p[36+6],p[45+6],p[54+6],p[63+6],p[72+6]]
  c8=[p[0+7],p[9+7],p[18+7],p[27+7],p[36+7],p[45+7],p[54+7],p[63+7],p[72+7]]
  c9=[p[0+8],p[9+8],p[18+8],p[27+8],p[36+8],p[45+8],p[54+8],p[63+8],p[72+8]]
  # Combines the cells of variable (p) into lists broken down into their 3x3 sub-grids
  g1=[p[0+0],p[0+1],p[0+2],p[9+0],p[9+1],p[9+2],p[18+0],p[18+1],p[18+2]]
  g2=[p[0+3],p[0+4],p[0+5],p[9+3],p[9+4],p[9+5],p[18+3],p[18+4],p[18+5]]
  g3=[p[0+6],p[0+7],p[0+8],p[9+6],p[9+7],p[9+8],p[18+6],p[18+7],p[18+8]]
  g4=[p[27+0],p[27+1],p[27+2],p[36+0],p[36+1],p[36+2],p[45+0],p[45+1],p[45+2]]
  g5=[p[27+3],p[27+4],p[27+5],p[36+3],p[36+4],p[36+5],p[45+3],p[45+4],p[45+5]]
  g6=[p[27+6],p[27+7],p[27+8],p[36+6],p[36+7],p[36+8],p[45+6],p[45+7],p[45+8]]
  g7=[p[54+0],p[54+1],p[54+2],p[63+0],p[63+1],p[63+2],p[72+0],p[72+1],p[72+2]]
  g8=[p[54+3],p[54+4],p[54+5],p[63+3],p[63+4],p[63+5],p[72+3],p[72+4],p[72+5]]
  g9=[p[54+6],p[54+7],p[54+8],p[63+6],p[63+7],p[63+8],p[72+6],p[72+7],p[72+8]]
  # The above code is used in future functions to check the final variable (p) for various things (rules of the Suduko game, future allowable numbers that can go in each cell, ETC.

  # Combined List of Not Allowed Numbers in Each Cell  (contains duplicate numbers)
  nna=[sorted(r2+c1+g1),sorted(r2+c2+g1),sorted(r2+c3+g1),sorted(r2+c4+g2),sorted(r2+c5+g2),sorted(r2+c6+g2),sorted(r2+c7+g3),sorted(r2+c8+g3),sorted(r2+c9+g3),sorted(r3+c1+g1),sorted(r3+c2+g1),sorted(r3+c3+g1),sorted(r3+c4+g2),sorted(r3+c5+g2),sorted(r3+c6+g2),sorted(r3+c7+g3),sorted(r3+c8+g3),sorted(r3+c9+g3),sorted(r4+c1+g4),sorted(r4+c2+g4),sorted(r4+c3+g4),sorted(r4+c4+g5),sorted(r4+c5+g5),sorted(r4+c6+g5),sorted(r4+c7+g6),sorted(r4+c8+g6),sorted(r4+c9+g6),sorted(r5+c1+g4),sorted(r5+c2+g4),sorted(r5+c3+g4),sorted(r5+c4+g5),sorted(r5+c5+g5),sorted(r5+c6+g5),sorted(r5+c7+g6),sorted(r5+c8+g6),sorted(r5+c9+g6),sorted(r6+c1+g4),sorted(r6+c2+g4),sorted(r6+c3+g4),sorted(r6+c4+g5),sorted(r6+c5+g5),sorted(r6+c6+g5),sorted(r6+c7+g6),sorted(r6+c8+g6),sorted(r6+c9+g6),sorted(r7+c1+g7),sorted(r7+c2+g7),sorted(r7+c3+g7),sorted(r7+c4+g8),sorted(r7+c5+g8),sorted(r7+c6+g8),sorted(r7+c7+g9),sorted(r7+c8+g9),sorted(r7+c9+g9),sorted(r8+c1+g7),sorted(r8+c2+g7),sorted(r8+c3+g7),sorted(r8+c4+g8),sorted(r8+c5+g8),sorted(r8+c6+g8),sorted(r8+c7+g9),sorted(r8+c8+g9),sorted(r8+c9+g9),sorted(r9+c1+g7),sorted(r9+c2+g7),sorted(r9+c3+g7),sorted(r9+c4+g8),sorted(r9+c5+g8),sorted(r9+c6+g8),sorted(r9+c7+g9),sorted(r9+c8+g9),sorted(r9+c9+g9)]
  
  cnt=0
  a=[1,1,1,1,1,1,1,1,1]     # Combined List of allowed numbers in all cells
  while True:
    na=[]                   # Empty List to later remove duplicate values in above list
    for i in nna[cnt]:
      if i not in na:
        na.append(i)        # Adds the numbers from list (nna) to list (na), only if that number (from list nna) is not already in list (na).  This effectivly "removes" the duplicate numbers from the origional list of not allowed numbers (nna).
      if na[0] == 0:
        na.remove(0)        # Since the origional list (p) was an array of 81 zeros, the filtered not allowed number list (na) may contain a zero value from the cells that have not yet had numbers placed in them.  This removes the zero value from this list.
    a.append([x for x in base + na if x not in base or x not in na])    # Combined List of allowed numbers in all cells, broken into sub-lists within this list.  Code compares the 2 lists [Filtered Not Allowed Numbers (na) to the list of all numbers 1-9 (base)] and creates a new list of the numbers that are NOT in both lists.
    cnt=cnt+1
    if cnt == len(nna):
      break
    continue
  cnt=0                                  # Position varaible to be used with variable list (p)
  al=[]                                  # Empty list which will contain the final list of allowed numbers for all remaining cells
  while True:
    if p[cnt] != 0:                      # if the cell already contains an actual non-zero number, then append a sub list of 10 numbers.  10 numbers are required to make the future length check (within the function:  core()) bypass the analysis.
      al.append([1,1,1,1,1,1,1,1,1,1])   # We want to bypass the core() analysis when a non-zero number is already present at that cell location.  There is no case of allowable numbers that has a list length of 10 possible numbers.
    if p[cnt] == 0:                      # if the cell == 0 then append the previous list of allowed numbers (variable aall), to be randomly chosen from and assigned to that cell location later on.
      al.append(a[cnt])
    cnt=cnt+1
    if cnt < 81:
      continue
    break
  cnt=0                                  # Position variable to be used below with the list al
  length_al=[]                           # Empty list to be filled in with the lengths values of each "allowed numbers" list at the cell location
  while True:
    length_al.append(len(al[cnt]))       # fills the above empty list with the length values at position (yy)
    cnt=cnt+1
    if cnt < 81:
      continue
    min_len_al=min(length_al)            # finds the minimum list length of the "allowed numbers" for the entire 9x9 grid.  This is critical, because if the value is zero, then it means somewhere in the 9x9 grid, there is no solution of "allowed numbers" within that cell.  This means that we created a non-solvable Suduko grid in a previously randomly generated number placed in a previous cell location.
    break
def core_2():
  global min_index_pos, length_al, min_len_al, a, al, p
  cnt=0
  while True:
    if cnt > cntmax:
      print("ERROR QUITTING -- Loop Count Reached in Function:  core_2()")
      quit()
    core_1()
    min_index_pos=length_al.index(min_len_al) # This returns the 1st cell position of the cell with the least amount of possible numbers
    
    # Below places randomly selected numbers (from that cells allowed number list) into the cell defined by the above line.
    # This goes in order by placing numbers in cells that have the least amount of possible numbers first.
    # in the case of a zero length list of allowed numbers in a cell, we exit this function and proceed to the function:  chk2().
    if min_len_al == 1:
      p[min_index_pos]=random.choice(a[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_al == 2:
      p[min_index_pos]=random.choice(a[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_al == 3:
      p[min_index_pos]=random.choice(a[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_al == 4:
      p[min_index_pos]=random.choice(a[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_al == 5:
      p[min_index_pos]=random.choice(a[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_al == 6:
      p[min_index_pos]=random.choice(a[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_al == 7:
      p[min_index_pos]=random.choice(a[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_al == 8:
      p[min_index_pos]=random.choice(a[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_al == 9:
      p[min_index_pos]=random.choice(a[min_index_pos])
      cnt=cnt+1
      continue
    if min_len_al == 0:
      break
    break

def chk():
  i=12                              # initial cell position
  cnt=0                             # initial list location for selecting the row
  while True:
    core_1()
    rn=[r2,r3,r4,r5,r6,r7,r8,r9]    # Row List to be pulled from during the below for loop
    loc=[0,1,2,3,4,5,6,7]           # List Location to determine what row will be selected during the below for loop
    if 0 in rn[loc[cnt]]:           # checks for 0 within the selected row (loop iterates and checks all rows)
      p[i+0]=0                      # this resets the last 6 numbers in the currect iterated row to zero.  only the last 6 places are reset (and not the entire row) because these 6 cells cause the "Empty List of allowed numbers in future cell location".
      p[i+1]=0
      p[i+2]=0
      p[i+3]=0
      p[i+4]=0
      p[i+5]=0
      i=i+4
    if 0 not in rn[loc[cnt]]:       # This skips resetting the 6 cells to zero if all numbers within the row were generated correctly according to the rules of Suduko
      i=i+9
    if loc[cnt] == 7:               # This exits the function chk2() since the last row has been checked when v == 7
      break
    cnt=cnt+1
    continue
def final_chk():
  if base == sorted(r1) and base == sorted(r2) and base == sorted(r3) and base == sorted(r4) and base == sorted(r5) and base == sorted(r6) and base == sorted(r7) and base == sorted(r8) and base == sorted(r9) and base == sorted(g1) and base == sorted(g2) and base == sorted(g3) and base == sorted(g4) and base == sorted(g5) and base == sorted(g6) and base == sorted(g7) and base == sorted(g8) and base == sorted(g9) and base == sorted(c1) and base == sorted(c2) and base == sorted(c3) and base == sorted(c4) and base == sorted(c5) and base == sorted(c6) and base == sorted(c7) and base == sorted(c8) and base == sorted(c9):
    print("-----Final Check PASS-----")
  else:
    print("-----Final Check FAIL-----XXXXXXXXXXXXXXXXXXXXXX")
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


# Main Loop to Generate Suduko Grid
while True:
  temp=[1,2,3,4,5,6,7,8,9]
  random.shuffle(temp)              # Create Numbers in Row 1 by Shuffling the List
  p[0]=temp[0]                      # Assigns each number from the shuffled list to a cell in row 1
  p[1]=temp[1]
  p[2]=temp[2]
  p[3]=temp[3]
  p[4]=temp[4]
  p[5]=temp[5]
  p[6]=temp[6]
  p[7]=temp[7]
  p[8]=temp[8]
  cnt2=0
  while True:
    core_1()
    core_2()
    if 0 in p and cnt2 <= cntmax:
      cnt2=cnt2+1
      chk()
      continue
    if cnt2 > cntmax:
      print("Error --- Loop Count Reached --- Please Try Running This Again")
      break
    break
  core_1()
  grid_print()
  final_chk()
  break