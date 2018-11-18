"""this class create for simple process on string"""
from simplex import  Simplex

class Operator:

    def create_complete_connection(self, edgeText, vertices):
        edgeText=self.get_combination(edgeText)
        tempList = []
        tempListGraph = []
        for i in range(len(edgeText)):
            if (edgeText[i] <> ',') and (edgeText[i] <> '.'):
                tempList.append(edgeText[i])
            if (edgeText[i] == ','):
                tempList.sort()
                for j in range(len(tempList)):
                    tempGraph = Simplex(tempList[j])
                    tempGraph.name = tempList[j]
                    tempListGraph.append(tempGraph)
                tempTree = []
                for j in range(len(tempListGraph)):
                    if j <> 0:
                        tempTree.append(tempListGraph[j])
                vertices[int(min(tempList)) - 1].insert_childs(tempTree)
                tempList = []
                tempListGraph = []
            if (edgeText[i] == '.'):
                tempList.sort()
                for j in range(len(tempList)):
                    tempGraph = Simplex(tempList[j])
                    tempGraph.name = tempList[j]
                    tempListGraph.append(tempGraph)
                tempTree = []
                for j in range(len(tempListGraph)):
                    if j <> 0:
                        tempTree.append(tempListGraph[j])
                vertices[int(min(tempList)) - 1].insert_childs(tempTree)
        return

    def create_simple_connection(self, edgeText, vertices):
        tempList = []
        tempListGraph = []
        for i in range(len(edgeText)):
            if (edgeText[i] <> ',') and (edgeText[i] <> '.'):
                tempList.append(edgeText[i])
            if (edgeText[i] == ','):
                tempList.sort()
                for j in range(len(tempList)):
                    tempGraph = Simplex(tempList[j])
                    tempGraph.name = tempList[j]
                    tempListGraph.append(tempGraph)
                tempTree = []
                for j in range(len(tempListGraph)):
                    if j <> 0:
                        tempTree.append(tempListGraph[j])
                vertices[int(min(tempList)) - 1].insert_childs(tempTree)
                tempList = []
                tempListGraph = []
            if (edgeText[i] == '.'):
                tempList.sort()
                for j in range(len(tempList)):
                    tempGraph = Simplex(tempList[j])
                    tempGraph.name = tempList[j]
                    tempListGraph.append(tempGraph)
                tempTree = []
                for j in range(len(tempListGraph)):
                    if j <> 0:
                        tempTree.append(tempListGraph[j])
                vertices[int(min(tempList)) - 1].insert_childs(tempTree)
        return

    def delete_connection(self, edgeText, vertices):
        tempList = []
        tempListGraph = []
        for i in range(len(edgeText)):
            if (edgeText[i] <> ',') and (edgeText[i] <> '.'):
                tempList.append(edgeText[i])
            if (edgeText[i] == ','):
                tempList.sort()
                for j in range(len(tempList)):
                    tempGraph = Simplex(tempList[j])
                    tempGraph.name = tempList[j]
                    tempListGraph.append(tempGraph)
                tempTree = []
                for j in range(len(tempListGraph)):
                    if j <> 0:
                        # first element is node
                        tempTree.append(tempListGraph[j])
                vertices[int(min(tempList)) - 1].delete_childs(tempTree)
                for j in range(len(vertices)):
                    if int(vertices[j].name) < int(vertices[int(min(tempList)) - 1].name):
                        vertices[j].delete_childs(tempListGraph)
                tempList = []
                tempListGraph = []
            if (edgeText[i] == '.'):
                tempList.sort()
                for j in range(len(tempList)):
                    tempGraph = Simplex(tempList[j])
                    tempGraph.name = tempList[j]
                    tempListGraph.append(tempGraph)
                tempTree = []
                for j in range(len(tempListGraph)):
                    if j <> 0:
                        # first element is node
                        tempTree.append(tempListGraph[j])
                vertices[int(min(tempList)) - 1].delete_childs(tempTree)
                for j in range(len(vertices)):
                    if int(vertices[j].name) < int(vertices[int(min(tempList)) - 1].name):
                        vertices[j].delete_childs(tempListGraph)
        return

    def show_structures(self,vertices):
        for i in range(len(vertices)):
            print 'vertices are: ', vertices[i].name

        for i in range(len(vertices)):
            for key1, value1 in vertices[i].childs.items():
                print 'edges connection are: ', value1.parents[vertices[i].name].name, '<--->', value1.name

        for i in range(len(vertices)):
            for key1, value1 in vertices[i].childs.items():
                for key2, value2 in vertices[i].childs[key1].childs.items():
                    print 'triangles connection are: ', value1.parents[
                        vertices[i].name].name, '<--->', value1.name, '<--->', value2.name

        for i in range(len(vertices)):
            for key1, value1 in vertices[i].childs.items():
                for key2, value2 in vertices[i].childs[key1].childs.items():
                    for key3, value3 in vertices[i].childs[key1].childs[key2].childs.items():
                        print 'tetrahedron connection are: ', value1.parents[
                            vertices[i].name].name, '<--->', value1.name, '<--->', value2.name, '<--->', value3.name

    def get_combination(self, edgeText):
        A = []
        S = ''
        for j in range(2, len(edgeText) + 1):
            for x in self.get_combination_list(edgeText, j):
                A.append(x)
        for i in range(len(A)):
            for j in range(len(A[i])):
                S = S + str(A[i][j])
            if i < len(A) - 1:
                S = S + ','
            if i == len(A) - 1:
                S = S + '.'
        return S

    def get_combination_list(self, items, n):
        if n == 0:
            yield []
        else:
            for i in range(len(items)):
                for cc in self.get_combination_list(items[i + 1:], n - 1):
                    yield [items[i]] + cc

    def get_combination_with_list(self,edgeText):
        A = []
        result = []
        for j in range(2, len(edgeText) + 1):
            for x in self.get_combination_list(edgeText, j):
                A.append(x)
        for i in range(len(A)):
            temp_result = []
            for j in range(len(A[i])):
                temp_result.append(int(A[i][j]))
            if i < len(A) - 1:
                result.append(temp_result)
            if i == len(A) - 1:
                result.append(temp_result)
        return result

