# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def topKFrequent(self, nums, k: int):
        counts = {}
        for i in range(0, len(nums)):
            counts[nums[i]] = 1 + counts.get(nums[i], 0)
        frequency = [[] for i in range(0, len(nums) + 1)]
        for value, count in counts.items():
            frequency[count].append(value)
        print(frequency)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
