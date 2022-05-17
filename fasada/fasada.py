class ResourceLogisticTeam:
    def __init__(self):
        pass
    def buyMaterials(self):
        print("all materials have bought")

class DecorateTeam:
    def __init__(self):
        pass
    def makeScenery(self):
        print("work is done")


class DesignTeam:
    def __init__(self):
        pass
    def makeDesign(self):
        print("design was made")

class ArchitectsTeam:
    def __init__(self):
        pass
    def makeHousePlan(self):
        print("house plan was made")

class BuildTeam:
    def __init__(self):
        pass
    def build(self):
        print("house was built")

class BuilderCompanyFacade:
    def __init__(self,resourceLogisticTeam: ResourceLogisticTeam,decorateTeam: DecorateTeam,
                 designTeam: DesignTeam,architectsTeam: ArchitectsTeam,
                 buildTeam: BuildTeam):
        self.resourceLogisticTeam = resourceLogisticTeam
        self.decorateTeam = designTeam
        self.designTeam = designTeam
        self.architectsTeam = architectsTeam
        self.buildTeam = buildTeam
    def build(self):
        self.resourceLogisticTeam.buyMaterials()
        self.architectsTeam.makeHousePlan()
        self.designTeam.makeDesign()
        self.buildTeam.build()
        self.decorateTeam.makeDesign()
        print("   /\\\n  /  \\\n ----- \n |   | \n |   | \n ----- \n krzywy dach)")


if __name__ == "__main__":
    resourceLogisticTeam = ResourceLogisticTeam()
    buildTeam = BuildTeam()
    architectsTeam = ArchitectsTeam()
    decorateTeam = DecorateTeam()
    designTeam = DesignTeam()
    builderCompanyFacade = BuilderCompanyFacade(resourceLogisticTeam,decorateTeam,designTeam,architectsTeam,buildTeam)
    builderCompanyFacade.build()





