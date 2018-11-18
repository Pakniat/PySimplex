#
from simplex import  Simplex
from textOperator import Operator

class ObjLoader(object):
    def __init__(self, fileName):
        self.vertices = []
        self.faces = []
        try:
            f = open(fileName)
            for line in f:
                if line[:2] == "v ":
                    index1 = line.find(" ") + 1
                    index2 = line.find(" ", index1 + 1)
                    index3 = line.find(" ", index2 + 1)
                    vertex=[]
                    vertex.append(float(line[index1:index2]))
                    vertex.append(float(line[index2:index3]))
                    vertex.append(float(line[index3:-1]))
                    self.vertices.append(vertex)
                elif line[0] == "f":
                    string = line.replace("//", "/")
                    i = string.find(" ") + 1
                    face = []
                    for item in range(string.count(" ")):
                        if string.find(" ", i) == -1:
                            face.append(string[i:-1])
                            break
                        face.append(string[i:string.find(" ", i)])
                        i = string.find(" ", i) + 1
                    self.faces.append(face)
            f.close()
        except IOError:
            print(".obj file not found.")
    #convert to vertices and faces
    def convert_obj(self,path):
        with open(path + '.obj', 'w') as file:
            for i in new1.vertices:
                file.write("v ")
                for j in i:
                    file.write(str(j) + " ")
                file.write("\n")
            for i in new1.faces:
                file.write("f ")
                for j in i:
                    file.write(str(j) + " ")
                file.write("\n")

new1=ObjLoader('path obj file')
new1.convert_obj('name')
operator=Operator()
#set vertext from file
counter_temp_name_vertex=0
vertices_simpelx=[]
for item in new1.vertices:
    counter_temp_name_vertex+=1
    vertex_simplex = Simplex(str(counter_temp_name_vertex))
    vertex_simplex.set_coordinate(item)
    vertices_simpelx.append(vertex_simplex)
#set face from file
counter_temp_name_vertex=0
faces=[]
for item in new1.faces:
    temp=[]
    for inner_item in item:
        index_vertex=inner_item.find("/")
        if inner_item[0:index_vertex]!='':
            temp.append(int(inner_item[0:index_vertex]))
    faces.append(temp)
# create simplicial complex
for i in faces:
    i.sort()
    temp_string_list = []
    for q in i:
        temp_string_list.append(str(q))
    combination = operator.get_combination_with_list(temp_string_list)
    for j in combination:
        tempList=[]
        tempListGraph=[]
        for q in j:
            tempGraph = Simplex(str(q))
            tempList.append(q)
            tempListGraph.append(tempGraph)
        tempTree = []
        for k in range(len(tempListGraph)):
            if k <> 0:
                tempTree.append(tempListGraph[k])
        vertices_simpelx[int(min(tempList)) - 1].insert_childs(tempTree)

# show structure of obj file
operator.show_structures(vertices_simpelx)