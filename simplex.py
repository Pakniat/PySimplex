"""data structure of simplex tree and related operators"""
class Simplex:

    dimension=0
    HEAD=0

    def __init__(self, name):
        self.name = name
        self.parents = {}
        self.childs = {}
        self.starList = []

    def set_childs(self, child):
        self.childs[child.name] = child
        child.parents[self.name] = self

    def has_child(self, child):
        if len(self.childs) > 0:
            return self.childs.has_key(child.name)

    def get_child(self, child):
        if len(self.childs) > 0:
            return self.childs.get(child.name)

    def delete_child(self, child):
        del self.childs[child.name]
        return

    def insert_childs(self, list_childs):
        if len(list_childs) > 0:
            if not (self.has_child(list_childs[self.HEAD])):
                self.set_childs(list_childs[self.HEAD])
                return
            if self.has_child(list_childs[self.HEAD]):
                list_recursion = []
                for i in range(len(list_childs)):
                    if i <> 0:
                        list_recursion.append(list_childs[i])
                self.get_child(list_childs[self.HEAD]).insert_childs(list_recursion)
        return

    def delete_childs(self, list_childs):
        if self.has_child(list_childs[self.HEAD]):
            list_recursion = []
            for i in range(len(list_childs)):
                if i <> 0:
                    list_recursion.append(list_childs[i])
            if len(list_recursion) == 0:
                self.delete_child(list_childs[self.HEAD])
                for key, value in self.childs.items():
                    if value.has_child(list_childs[self.HEAD]):
                        listTemp = []
                        listTemp.append(list_childs[self.HEAD])
                        self.childs[key].delete_childs(listTemp)
            if len(list_recursion) > 0:
                self.get_child(list_childs[self.HEAD]).delete_childs(list_recursion)
                for key, value in self.childs.items():
                    if value.has_child(list_childs[self.HEAD]):
                        value.delete_childs(list_childs)
            return

    def get_power_set(self, s):
        power_set = [[]]
        for elem in s:
            for sub_set in power_set:
                power_set = power_set + [list(sub_set) + [elem]]
        return power_set

    def delete_duplicate(self, list):
        unique = []
        for item in list:
            if sorted(item) not in unique:
                unique.append(sorted(item))
        return unique

    def path_star(self, mySelf,listM):
        if len(self.childs) == 0:
            return
        if len(self.childs) > 0:
            if(self.has_child(mySelf)):
                listRec = []
                listRec.append(self.name)
                listRec.append(mySelf.name)
                for i in range(len(listM)):
                    listRec.append(listM[i])
                mySelf.starList.append(listRec)
                for key,value in self.childs.items():
                    if value.has_child(mySelf):
                        listM.append(self.name)
                        value.path_star(mySelf,listM)
                    for i in range(len(listM)):
                        if listM[i] == self.name:
                            del  listM[i]
        return

    def star_vertex(self):
        for i in range(len(self.starList)):
            container_list =[]
            for j in range(len(self.starList[i])):
                if self.starList[i][j] <> self.name:
                    container_list.append(self.starList[i][j])
            new_container = self.get_power_set(container_list)
            for j in range(len(new_container)):
                self.starList.append(new_container[j])
        final_container=self.delete_duplicate(self.starList)
        self.starList=[]
        self.starList=final_container
        return

    def starChild(self,pChild,mySelf):
        if not self.ifChilds(pChild):
            return
        if self.ifChilds(pChild):
            listRec = []
            if self.name <> mySelf.name:
                listRec.append(mySelf)
            listRec.append(self)
            for i in range(len(self.childs)):
                if self.childs[i].name == pChild.name:
                    listRec.append(self.childs[i])
            mySelf.starList.append(listRec)
            for i in range(len(self.childs)):
                if self.childs[i].ifChilds(pChild):
                    self.childs[i].starChild(pChild,mySelf)


#TODO add dimension and max dimension of simplex