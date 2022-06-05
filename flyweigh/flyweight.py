from typing import Dict

class FlyweightTextures:
    def __init__(self, inner_state):
        self._inner_state = inner_state

    def desplyCondition(self, out_unique_state):
        print(f"Flyweight: Displaying texture ({self._inner_state}) and object ({out_unique_state}) \n")


class FlyweightFactory:
    _textures = {}
    def __init__(self, initial_gameObjests):
        for state in initial_gameObjests:
            self._textures[self.get_key(state)] = FlyweightTextures(state)

    def get_key(self, state):
        return "_".join(sorted(state))

    def get_flyweight(self, inner_state):
        key = self.get_key(inner_state)

        if not self._textures.get(key):
            print()
            print("No such flyweight, creating new one")
            self._textures[key] = FlyweightTextures(inner_state)
        else:
            print()
            print("Flyweight is already exist")

        return self._textures[key]

    def list_flyweights(self):
        count = len(self._textures)
        print(f"in base - {count} textures:")
        print("\n".join(map(str, self._textures.keys())), end="")



class GameObject:
    def __init__(self,name,typeObj):
        self.name = name
        self.typeObj = typeObj

    def add_texture_to_database(self, factory, quality, textureName, textureType):
        self.flyweight = factory.get_flyweight([quality, textureName, textureType])
        self.flyweight.desplyCondition([self.name, self.typeObj])


if __name__ == "__main__":
    factory = FlyweightFactory([
        ["high", "personTexture", "type3"],
        ["low", "personTexture", "type3"],
        ["high", "wallTexture", "type1"],
        ["low", "wallTexture", "type1"],
        ["high", "rockTexture", "type2"],
        ["low", "rockTexture", "type2"],
    ])

    factory.list_flyweights()


    person = GameObject("Nick","person")
    wall = GameObject("high wall", "wall")


    person.add_texture_to_database(factory,"high", "personTexture", "type3")
    print("\n")
    factory.list_flyweights()

    wall.add_texture_to_database(factory,"high", "wallTexture", "type3 withGraffiti")
    print("\n")
    factory.list_flyweights()
