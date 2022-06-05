from __future__ import annotations
from abc import ABC, abstractmethod


class Enemy:
    _state = None
    def __init__(self, state: Behavior):
        self.change_state(state)

    def change_state(self, state: Behavior):
        print(f"State was changed to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def tracking(self,distanse):
        self._state.track_distance_to_player(distanse)


    def walk(self):
        print("walking")

    def track_players_attack(self):
        print("I track player attacks")


class Behavior(ABC):
    @property
    def context(self) -> Enemy:
        return self._context

    @context.setter
    def context(self, context: Enemy):
        self._context = context

    @abstractmethod
    def track_distance_to_player(self,distanse):
        pass



class Passive(Behavior):
    def track_distance_to_player(self,distanse):
        print("tracking")
        if distanse < 5:
            print("player so close I need to attack")
            self.context.change_state(Aggressive())
        else:
            print("player so far")




class Aggressive(Behavior):
    def track_distance_to_player(self,distanse):
        print("tracking")
        if distanse > 5:
            print("player so far")
            self.context.change_state(Passive())
        else:
            print("player so close I need to attack")



if __name__ == "__main__":

    context = Enemy(Passive())
    context.walk()
    context.tracking(6)
    context.tracking(3)
    context.track_players_attack()
    context.tracking(9)
