class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x: x[1], reverse=True)

        units = 0

        for boxes, unitPerBox in boxTypes:
            take = min(boxes, truckSize)

            units += take * unitPerBox
            truckSize -= take

            if truckSize == 0:
                break

        return units