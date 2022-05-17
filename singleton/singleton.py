class GovernmentMetaclass(type):
    examples = {}
    def __call__(nowClass, *args, **kwargs):
        if nowClass not in nowClass.examples:
            example = super().__call__( *args, **kwargs)
            nowClass.examples[nowClass] = example
        return nowClass.examples[nowClass]

class Government(metaclass = GovernmentMetaclass):
    def makeNewLaw(self):
        print("new law")
    def getGovernment(self):
        return self



if __name__ == "__main__":
    gov1 = Government()
    gov2 = Government()

    gov2.makeNewLaw()

    if gov2 == gov1:
        print("same")
    else:
        print("dif")
    print(gov1)
    print(gov2)




