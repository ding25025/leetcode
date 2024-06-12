"""
    - TimeMap() Initializes the object of the data structure.
    - void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    - String get(String key, int timestamp) Returns a value such that set was called previously, 
    with timestamp_prev <= timestamp. 
    If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
    Time O(log N) 
    Space O(1)
"""


class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.dict.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                l = mid + 1
                result = values[mid][0]
            else:
                r = mid - 1
        return result
