from abc import ABC, abstractmethod


class BuilderAbstract(ABC):
    def base_builder_method(self):
        self.buildFoundation()
        self.buildWalls()
        self.buildDoor()
        self.buildWindows()
        self.buildRoof()
        self.buildInside()
        self.makeBalconyHook()
        self.windowOnRoofHook()

    def buildFoundation(self):
        print('foundation was built')

    def buildWalls(self):
        print('walls were built')

    def buildWindows(self):
        print('windows were built')

    def buildRoof(self):
        print('roof was built')


    @abstractmethod
    def buildDoor(self):
        pass

    @abstractmethod
    def buildInside(self):
        pass

    def windowOnRoofHook(self):
        pass

    def makeBalconyHook(self):
        pass



class Garage(BuilderAbstract):
    def buildDoor(self):
        print('garage door was built')
    def buildInside(self):
        print('the garage pit has been built, the tools have been placed')


class House(BuilderAbstract):
    def buildDoor(self):
        print('beautiful door was built')

    def buildInside(self):
        print('beautiful interior was done')

    def windowOnRoofHook(self):
        print("a window with a beautiful view on the stars was built")


def build(builder_abstruct):
    builder_abstruct.base_builder_method()

if __name__ == "__main__":
    print('lets make garage')
    build(Garage())

    print('---------------')

    print('lets make garage')
    build(House())