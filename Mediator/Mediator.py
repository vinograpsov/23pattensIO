from abc import ABC


class AircraftCommunicationsTowerInterface(ABC):
    def notify(self, sender: object, event: str):
        pass


class AircraftCommunicationsTower(AircraftCommunicationsTowerInterface):
    _aircrafts = []
    def __init__(self,*aircrafts):
        for i in aircrafts:
            self._aircrafts.append(i)
        for i in range(0,len(self._aircrafts)):
            self._aircrafts[i].aircraftTowerA = self

    def __returnIndex(self,typeA):
        for i in range(0,len(self._aircrafts)):
            if self._aircrafts[i].typeA == typeA: return i

    def notify(self, sender: object, event: str) -> None:
        if event == "P":
            print("Request from plane receiwed")
            self._aircrafts[self.__returnIndex('P')].land()
            self._aircrafts[self.__returnIndex('P')].releasePassengers()
            del self._aircrafts[self.__returnIndex('P')]
        elif event == "H":
            print("Request  from helicopter receiwed")
            self._aircrafts[self.__returnIndex('H')].land()
            self._aircrafts[self.__returnIndex('H')].releasePassengers()
            self._aircrafts[self.__returnIndex('H')].realeaseInjured()
            del self._aircrafts[self.__returnIndex('H')]
        elif event == "PP":
            print("Request  from private plane receiwed")
            self._aircrafts[self.__returnIndex('PP')].land()
            self._aircrafts[self.__returnIndex('PP')].releasePassengers()
            del self._aircrafts[self.__returnIndex('PP')]

class Aircraft:
    def __init__(self, aircraftTower: AircraftCommunicationsTowerInterface = None):
        self._aircraftTower = aircraftTower

    @property
    def aircraftTowerA(self):
        return self._aircraftTower

    @aircraftTowerA.setter
    def aircraftTowerA(self, aircraftTower):
        self._aircraftTower = aircraftTower


class Boieng777(Aircraft):

    typeA = "P"
    def request_to_land(self):
        self.aircraftTowerA.notify(self, self.typeA)
    def land(self):
        print("boing 777 was landed")

    def releasePassengers(self):
        print("release passengers")

class AirbusHelicoptersEC135(Aircraft):
    typeA = "H"

    def request_to_land(self):
        self.aircraftTowerA.notify(self, self.typeA)

    def land(self):
        print("Airbus Helicopters EC135 was landed")

    def releasePassengers(self):
        print("release passengers")

    def realeaseInjured(self):
        print("the wounded were taken to hospitals")


class GulfstreamG650(Aircraft):
    typeA = "PP"
    def request_to_land(self):
        self.aircraftTowerA.notify(self, self.typeA)

    def land(self):
        print("Gulfstream G650 was landed")

    def releasePassengers(self):
        print("release super rich passengers")



if __name__ == "__main__":

    just_boieng = Boieng777()
    super_rich_jet = GulfstreamG650()
    airAmbulanceHelicompte = AirbusHelicoptersEC135()
    aicraftTower = AircraftCommunicationsTower(just_boieng,super_rich_jet,airAmbulanceHelicompte)


    just_boieng.request_to_land()
    print()
    super_rich_jet.request_to_land()
    print()
    airAmbulanceHelicompte.request_to_land()