"""
Summary:
    secondary storage
    Opening a file - file handle
        file handle as a sequence
        a sequence is an ordered set
    File Structure - newline character /n
    Reading a file line by line with a for loop "for eachline in fhand: pass"
    Searching for lines " if eline.startswith("***"):"
    Searching for certain characters "if 'word' in line:/if not 'word' in line:"
    Reading file names "fname= input('enter the file name: ')"
    Dealing with bad files - try except


"""
def say_hello():
    # fhand= open('story.txt')

    # counter=0
    # for eline in fhand:
    #     print(eline)
    #     counter +=1
    #
    # print("This text has ",counter,' lines in total')
    # # read txt in one line
    # linetext = fhand.read()
    # print(len(linetext))
    # search through a file
    # for line in fhand:
    #     if line.startswith('This'):
    #         print(line)
    # counter=0
    #     # for eline in fhand:
    #     #     eline= eline.rstrip()
    #     #     print(eline)
    #     #     counter +=1
    #     #
    #     # print("This text has ",counter,' lines in total')
    # counter=0
    # for eline in fhand:
    #     if not eline.startswith("This"):
    #         continue
    #     print(eline)
    #     counter +=1
    # Try Except
    fname= input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        quit()
    counter=0
    for eline in fhand:
        eline=eline.rstrip()
        print(eline)
        counter +=1

    print("This text has ",counter,' lines in total')

say_hello()