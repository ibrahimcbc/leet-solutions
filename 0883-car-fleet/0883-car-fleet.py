class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_hour=[]
        fleets=1
        for i in range(len(position)):
            hours=((target-position[i])/speed[i])
            car_hour.append((position[i],hours))
        car_hour= sorted(car_hour,key=lambda x: x[0],reverse=True)
        dest_time= car_hour[0][1]
        for el in car_hour:
            if el[1]>dest_time:
                dest_time=el[1]
                fleets+=1
        return fleets