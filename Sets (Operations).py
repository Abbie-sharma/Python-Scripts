#  represent the mathematical concept of 'set'.

class set:
    def abc(self, setA, setB):
        self.setA = setA
        self.setB = setB
    def unionFunc(self):
        return self.setA.union(self.setB)
    def intersectionFunc(self):
        return self.setA.intersection(self.setB)
    def cardinalityFunc(self, setName):
        return len(setName)
setObj = set()
setA = {1,2,3,4}
setB = {2,4,6,8}
setObj.abc(setA, setB)
setUnion = setObj.unionFunc()
setIntersection= setObj.intersectionFunc()
setCardinality= setObj.cardinalityFunc(setA)
print(setUnion)
print(setIntersection)
print(setCardinality)
