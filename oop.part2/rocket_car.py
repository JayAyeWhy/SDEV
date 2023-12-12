from car import Car

class RocketCar(Car):
    def __init__(self, heading = 'N', x=0, y=0, fuel: float = 2.0):
        super().__init__(heading = 'N', x=0, y=0)
        
        self.__BASE_VELOCITY = 2.0
        self.__ROCKET_VELOCITY = 10.0
        self._use_rocket_fuel = False
        self._minutes_of_fuel = fuel
        
        self._velocity = 2.0
    def toggle_rocket_fuel(self):
        self.use_rocket_fuel = not self._use_rocket_fuel
        if self.use_rocket_fuel:
            print("Rocket fuel is now on.")
            self._velocity = self.__ROCKET_VELOCITY
        else:
            print("Rocket fuel is now off.")
            self._velocity
    
    def move(self,time: float = 1.0):

        if self._use_rocket_fuel:
            fueled_move = min(self._minutes_of_fuel, time)
            unfueled_move = time - fueled_move

            self._minutes_of_fuel -= fueled_move

            super().move(fueled_move)

            if fueled_move < time:
                print('Out of Fuel!')
                self.toggle_rocket_fuel()
                super().move(unfueled_move)
        else:
            super().move(time)
        #if self._use_rocket_fuel:
#            self._minutes_of_fuel -= time
#            print(f"{self._minutes_of_fuel} minutes of fuel remaining.")
