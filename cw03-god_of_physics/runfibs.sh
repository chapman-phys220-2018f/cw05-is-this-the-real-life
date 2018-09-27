#!/usr/bin/bash

import testmodule

def main(argv):
    print(fib.f(int(argv[1])))
    
if __name__=="__main__":
    import sys
    main(sys.argv)

fi