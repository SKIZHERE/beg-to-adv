s = str(input("Roman Number: "))
f = 0

d = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
for i in range(len(s)):
    if i<len(s)-1 and d[s[i]]<d[s[i+1]]:
        f = f - d[s[i]]
    else:
        f = f + d[s[i]]

print(f)















# for i in s:
#     sl.append(i)
# for i in sl:
#     slt.append(d.get(i))

# print(s)
# print(sl)
# print(slt)

# for i in range(0,len(sl)):
#     try:
#         if slt[n] == 1:
#             try:
#                 if slt[n+1] == 5 or slt[n+1]== 10:
#                     slf.append(slt[n+1] - slt[n])
#                     n+=2
#             except IndexError:
#                     slf.append(slt[n])
#                     n+=1
#         elif slt[n] == 10:
#             try:
#                 if slt[n+1] == 50 or slt[n+1]== 100:
#                     slf.append(slt[n+1] - slt[n])
#                     n+=2
#             except IndexError:
#                 slf.append(slt[n])
#                 n+=1
#         elif slt[n] == 100:
#             try:
#                 if slt[n+1] == 500 or slt[n+1]== 1000:
#                     slf.append(slt[n+1] - slt[n])
#                     n+=2
#             except IndexError:
#                 slf.append(slt[n])
#                 n+=1
#         else:
#             slf.append(slt[n])
#             n+=1
#     except:
#         break
# print(slf)
# print(sum(slf))

