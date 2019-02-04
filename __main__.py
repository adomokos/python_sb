print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

from python_sb import main

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    # import ipdb; ipdb.set_trace() - stop here with the debugger
    main()
