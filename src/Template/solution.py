import os

infilename = "test.in"
in_file = open(infilename)





numcases = int(in_file.readline())
totalout = ""

for casenum in range(numcases):
    p = [float(w) for w in in_file.readline().split()]

    #code goes here

    

    outstr = "Case #" + str(casenum + 1) + ": " + ""
    totalout += outstr + "\n"
    print(outstr)


writetofile = False
if "small" in infilename:
    outprefix = "small"
    writetofile = True
elif "large" in infilename:
    outprefix = "large"
    writetofile = True
#writetofile = False

if writetofile:
    filenum = 0
    while True:
        outfilename = outprefix + str(filenum) + ".out"
        filenum += 1
        if not os.path.isfile(outfilename):
            break
    out_file = open(outfilename, 'w+')
    out_file.write(totalout)
    out_file.close()

in_file.close()

