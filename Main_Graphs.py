from Random_Graphs import *

def run():
    
    # Main menu
    # Directs the user to the method they want to use
    # by selecting a number

    

    print("Hello, welcome to Graphic Generator")
    print("Choose an generation method, please:")
    print("1.- Erdos-Rényi")
    print("2.- Gilbert")
    print("3.- Geographic")
    print("4.- Grid")
    print("5.- Barabasi-Albert")
    print("6.- Dorogovtev-Mendes")
    o = int(input())

    if o == 1:
        print("====== ERDOS-RENYI ======")
        name = input("Whats is your graph name?") # Obtaining data to create the graph
        n = int(input("How many nodes do you want?"))
        e = int(input("How many edges do you need?"))
        g=randomErdos(n,e,False,False,name) # Call the method to create the graph
        g.printNodes() # Show graph data to verify results on console
        g.printEdges()
        g.toGVFormat() # Creating gv file
    elif o == 2:
        print("====== GILBERT ======")
        name = input("Whats is your graph name?")
        n = int(input("How many nodes do you want?"))
        p = float(input("What probability do you expect to create an edge?")) # Obtaining data to create the graph
        if p <= 1 and p >= 0: # Valid probability check
            g=randomGilbert(n,p,False,False,name) # Call the method to create the graph
            g.printNodes() # Show graph data to verify results on console
            g.printEdges()
            g.toGVFormat() # Creating gv file
        else:
            print("Select a valid probability value")       
    elif o == 3:
        print("====== GEOGRAPHIC ======")
        name = input("Whats is your graph name?")
        n = int (input("How many nodes do you want?"))
        r = float (input("Choose a maximum distance less than 1"))
        if r <= 1 and r > 0: # Valid distance check
            g=randomGeo(n,r,False,False,name)
            g.printNodes()
            g.printEdges()
            g.toGVFormat()
        else:
            print("Select a valid distance")
    elif o == 4:
        print("====== GRID ======")
        name = input("Whats is your graph name?")
        m = int (input("How many columns do you want?"))
        n = int (input("How many files do you want?"))
        if m >= 1 and n >= 0: # Valid colomns and files check
            g=randomGrid(m,n,False,False,False,name)
            g.printNodes()
            g.printEdges()
            g.toGVFormat()
        else:
            print("Select a valid number of columns or files")
    elif o == 5:
        print("====== BARABASI-ALBERT ======")
        name = input("Whats is your graph name?")
        n = int (input("How many nodes do you want?"))
        d = int (input("Whats the maximum degree possible per node?"))
        g=randomBarabasi(n,d,False,False,name)
        g.printNodes()
        g.printEdges()
        g.toGVFormat()
    elif o == 6:
        print("====== DOROGOVTEV-MENDES ======")
        name = input("Whats is your graph name?")
        n = int (input("How many nodes do you want?"))
        g=randomDoroMendes(n,False,False,name)
        g.printNodes()
        g.printEdges()
        g.toGVFormat()
    else:
        print("Pick a valid option please")
    

if __name__ == '__main__':
    run()