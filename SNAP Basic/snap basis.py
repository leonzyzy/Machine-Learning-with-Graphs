import snap

# create a empty vector
v = snap.TIntV()

# add elements
v.Add(1)
v.Add(2)
v.Add(3)
v.Add(4)
v.Add(5)

# print length of vec
print('length: ', v.Len())

# print element in vec
for item in v:
    print(item)

# another print
for i in range(0, v.Len()):
    print(i, v[i])

# create an empty table
h = snap.TIntStrH()
h[5] = 'apple'
h[3] = 'tomato'
h[9] = 'orange'
h[6] = 'banana'
h[1] = 'apricot'
print('length: ', h.Len())

for key in h:
    print(key, h[key])

# create a pair
p = snap.TIntStrPr(1, "one")
print(p.GetVal1())
print(p.GetVal2())

# undirected graph
G1 = snap.TNGraph.New()
G1.AddNode(1)
G1.AddNode(5)
G1.AddNode(12)

# add edge
G1.AddEdge(1, 5)
G1.AddEdge(5, 1)
G1.AddEdge(5, 12)

G2 = snap.TUNGraph.New()  # create undirected graph
N1 = snap.TNEANet.New()  # directed network

# traversal nodes
for node in G1.Nodes():
    print('node id %d, out-degree %d, in-degree %d' % (node.GetId(), node.GetOutDeg(), node.GetInDeg()))

# traversal edges
for edge in G1.Edges():
    print('(%d %d)' % (edge.GetSrcNId(), edge.GetDstNId()))

# traversal edges by nodes
for NI in G1.Nodes():
    for Id in NI.GetOutEdges():
        print("edge (%d %d)" % (NI.GetId(), Id))

# save the graph
snap.SaveEdgeList(G1, "test.txt", "List of edges")

# load graph data
G5 = snap.LoadEdgeList(snap.PNGraph, "test.txt", 0, 1)
for edge in G5.Edges():
    print('(%d %d)' % (edge.GetSrcNId(), edge.GetDstNId()))

# generate a network using Forest Fire model
G3 = snap.GenForestFire(1000, 0.35, 0.35)
# save and load binary
FOut = snap.TFOut("test.graph")
G3.Save(FOut)

# load graph
FIn = snap.TFIn("test.graph")
G4 = snap.TNGraph.Load(FIn)
snap.SaveEdgeList(G4, "test.txt", "Save as tab-separated list of edges")
G5 = snap.LoadEdgeList(snap.TNGraph, "test.txt", 0, 1)

# example of download file:
wiki = snap.LoadEdgeList(snap.PNGraph, "Wiki-Vote.txt", 0, 1)
snap.PrintInfo(wiki, 'QA Stats', "qa-info.txt", False)
