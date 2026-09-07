class TimeMap:

    def __init__(self):

        self.data = {}
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:


        self.data[key] = self.data.get(key, [])
        self.data[key].append((value, timestamp))

        
        

    def get(self, key: str, timestamp: int) -> str:


        if key in self.data:


            arr = self.data[key]


            left = 0 
            right = len(arr)-1

            val = ""


            while left <= right:


                mid = (left+right)//2


                if arr[mid][1] <=  timestamp:


                    val = arr[mid][0]
                    left = mid+1

                else:
                    right = mid-1

            return val
        else:

            return ""


                





        
        
        
