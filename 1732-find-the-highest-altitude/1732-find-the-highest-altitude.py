class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #2 variables, one = altitude, two = max_altitude
        #Iterate through the array summing the elements
        #Update the altitude
        #update the max altitude so far

        altitude = 0
        max_altitude = 0

        for change in gain:
            altitude += change

            max_altitude = max(max_altitude, altitude)
            
        return max_altitude

   
       

        