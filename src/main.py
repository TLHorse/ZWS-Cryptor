import sys

if len(sys.argv) > 1:
    if sys.argv[1] == '-c':
        import cli
    else:
        print("ZSE: error: illegal option")
        exit(1)
else: 
    import gui