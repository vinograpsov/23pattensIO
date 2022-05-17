import copy

class CloneFactory:
    def __init__(self, clone_name, modelNum):
        self.clone_name = clone_name
        self.modelNum = modelNum
    def __copy__(self):
        model_num = copy.copy(self.modelNum)
        new = self.__class__(self.clone_name,model_num)
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
        clone_name = copy.deepcopy(self.clone_name, memo)
        new = self.__class__(clone_name)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


def makePersonality(clone,name,num):
    clone.clone_name = name
    clone.model_num = num

if __name__ == "__main__":
    personForCloning = CloneFactory("First",0)
    firstClone = copy.copy(personForCloning)

    if personForCloning.clone_name == firstClone.clone_name:
        print("same person")
    else:
        print("differrent")

    makePersonality(firstClone,"clone505",1)

    if personForCloning.clone_name == firstClone.clone_name:
        print("same person")
    else:
        print("differrent")


    secondClone = copy.copy(personForCloning)

    if secondClone.clone_name == firstClone.clone_name:
        print("same person")
    else:
        print("differrent")

    makePersonality(secondClone, "clone253", 2)

    if secondClone.clone_name == firstClone.clone_name:
        print("same person")
    else:
        print("differrent")


