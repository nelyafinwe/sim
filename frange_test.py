from math import atan

def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)
        
    return L

def main():
    rho = 1000
    A = 1
    A_ef = 0.95*A
    for x in frange(-4,4,0.2):
        v_o_max=2*0.0115
        q_o=rho*A_ef*atan(x)
        print v_o_max*q_o

    # # parse command line options
    # try:
    #     opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    # except getopt.error, msg:
    #     print msg
    #     print "for help use --help"
    #     sys.exit(2)
    # # process options
    # for o, a in opts:
    #     if o in ("-h", "--help"):
    #         print __doc__
    #         sys.exit(0)
    # # process arguments
    # for arg in args:
    #     process(arg) # process() is defined elsewhere

if __name__ == "__main__":
    main()