import copy

def full_time(matr, r):
    mcopy = copy.deepcopy(matr)
    cop = copy.deepcopy(matr)
    
    for n in range(len(r)):
        for i in range(len(mcopy)):
            for j in range(len(mcopy[0])):
                if r[n] - 1 == j:
                    mcopy[i][n] = cop[i][j]              

    for i in range(1):
        for j in range(1, len(mcopy[i])):
            mcopy[i][j] = mcopy[i][j] + mcopy[i][j - 1]
            
    for i in range(1):
        for j in range(1, len(mcopy)):
            mcopy[j][i] = mcopy[j][i] + mcopy[j - 1][i]

    for i in range(1, len(mcopy[i])):
        for j in range(1, len(mcopy)):
            mcopy[j][i] = mcopy[j][i] + max(mcopy[j - 1][i], mcopy[j][i - 1])
                   
    return mcopy[len(mcopy) - 1][len(mcopy[0]) - 1]

def rec1_sokol(matr):
    r = []
    sum = []
    
    for i in range(len(matr[0])):
        temp_sum = 0
        for j in range(len(matr) - 1):
            temp_sum += matr[j][i]
        sum.append(temp_sum)

    sumcopy = copy.deepcopy(sum)
    sumcopy.sort()

    for i in sumcopy:
        for j in range(len(sum)):
            if i == sum[j]:
                r.append(j)

    r = list(dict.fromkeys(r))

    return r

def rec2_sokol(matr):
    r = []
    sum = []

    for i in range(len(matr[0])):
        temp_sum = 0
        for j in range(len(matr)):
            if j == 0:
                pass
            else:
                temp_sum += matr[j][i]
        sum.append(temp_sum)

    sumcopy = copy.deepcopy(sum)
    sumcopy.sort()
    sumcopy.reverse()

    for i in sumcopy:
        for j in range(len(sum)):
            if i == sum[j]:
                r.append(j)

    r = list(dict.fromkeys(r))

    return r

def rec3_sokol(matr):
    r = []
    diff = []

    for i in range(len(matr[0])):
        diff1 = 0
        diff2 = 0
        for j in range(len(matr)):
            if j == 0:
                diff1 = matr[j][i]
            elif j == len(matr) - 1:
                diff2 = matr[j][i]
        diff3 = diff2 - diff1
        diff.append(diff3)
    
    diffcopy = copy.deepcopy(diff)
    diffcopy.sort()
    diffcopy.reverse()

    for k in diffcopy:
        for i in range(len(matr[0])):
            diff1 = 0
            diff2 = 0
            for j in range(len(matr)):
                if j == 0:
                    diff1 = matr[j][i]
                elif j == len(matr) - 1:
                    diff2 = matr[j][i]
            if diff2 - diff1 == k:
                r.append(i)
    
    r = list(dict.fromkeys(r))
    
    return r

def sokol_final_seq(matrix, r1, r2, r3):
    p1 = full_time(matrix, r1)
    p2 = full_time(matrix, r2)
    p3 = full_time(matrix, r3)

    for i in range(len(r1)):
        r1[i] = r1[i] + 1
        r2[i] = r2[i] + 1
        r3[i] = r3[i] + 1

    if p1 < p2 and p1 < p3:
        return r1
    elif p2 < p1 and p2 < p3:
        return r2
    else:
        return r3


def rec1_jons(matr):
    r = []
    mcopy = copy.deepcopy(matr[0])
    mcopy.sort()

    for i in mcopy:
        for j in range(1):
            for k in range(len(matr[j])):
                if matr[j][k] == i:
                    r.append(k)

    r = list(dict.fromkeys(r))
                    
    return r

def rec2_jons(matr):
    r = []
    mcopy = copy.deepcopy(matr[len(matr) - 1])
    mcopy.sort()
    mcopy.reverse()

    for i in mcopy:
        for j in range(len(matr) - 1, len(matr)):
            for k in range(len(matr[j])):
                if matr[j][k] == i:
                    r.append(k)

    r = list(dict.fromkeys(r))          
    return r

def rec4_jons(matr):
    r = []
    sumMatr = []

    for i in range(len(matr[0])):
        sum = 0
        for j in range(len(matr)):
            sum += matr[j][i]
        sumMatr.append(sum)

    mcopy = copy.deepcopy(sumMatr)
    mcopy.sort()
    mcopy.reverse()

    for i in mcopy:
        for j in range(len(sumMatr)):
            if sumMatr[j] == i:
                r.append(j)
    
    r = list(dict.fromkeys(r)) 
    return r


def jons_final_seq(r1, r2, r3):
    r = []
    sum = []

    for i in range(len(r1)):
        for a in range(len(r1)):
            if i == r1[a]:
                sum.append(a + 1)
        for b in range(len(r2)):
            if i == r2[b]:
                sum[i] += (b + 1)
        for c in range(len(r3)):
            if i == r3[c]:
                sum[i] += (c + 1)
    
    sumcopy = copy.deepcopy(sum)
    sumcopy.sort()

    for i in sumcopy:
        for j in range(len(sum)):
            if i == sum[j]:
                r.append(j + 1)

    r = list(dict.fromkeys(r))
    
    return r

def final_matrix(matr, r):
    mcopy = copy.deepcopy(matr)
    cop = copy.deepcopy(matr)
    
    for n in range(len(r)):
        for i in range(len(mcopy)):
            for j in range(len(mcopy[0])):
                if r[n] - 1 == j:
                    mcopy[i][n] = cop[i][j]              


    return mcopy



#print(jons_final_seq(rec1_jons(matrix), rec2_jons(matrix), rec4_jons(matrix)))

#print(final_matrix(matrix, jons_final_seq(rec1_jons(matrix), rec2_jons(matrix), rec4_jons(matrix))))


#print(sokol_final_seq(matrix, rec1_sokol(matrix), rec2_sokol(matrix), rec3_sokol(matrix)))

#print(full_time(matrix, rec1_jons(matrix)))
#print(full_time(matrix, rec2_jons(matrix)))
#print(full_time(matrix, rec4_jons(matrix)))

#print(full_time(matrix, rec1_sokol(matrix)))
#print(full_time(matrix, rec2_sokol(matrix)))
#print(full_time(matrix, rec3_sokol(matrix)))


#rec3_sokol(matrix)

#print(sum_full_time(matrix, rec1_sokol(matrix)))
#print(sum_full_time(matrix, rec2_sokol(matrix)))
#print(sum_full_time(matrix, rec3_sokol(matrix)))

#r4 = rec4(matrix)
#print(r4)

#r4 = rec4(matrix)
#print(r4)







    