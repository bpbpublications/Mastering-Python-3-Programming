# Program E14x4  # No statements excluded
#  Exception handling in queue
class Queue:
    def get_data(self, lis, left, right):
        self.lis=lis
        self.left=left
        self.right=right
    def writeq(self, ele):
        if self.left<0:
            raise IndexError("Queue Full")                               
        else:
            self.lis.append(ele)                             
            self.left-=1
    def readq(self):
        if self.left==self.right:
            raise IndexError("Queue Empty")
        else:
            ele=self.lis[self.right]
            del(self.lis[self.right])
            self.right-=1
            return ele
    def display(self):
            print('que now contains: ', self.lis)
def main():
    try:
        que=Queue()
        que.get_data([], 2,2)
        que.writeq(10)
        que.display()
        que.writeq(20)
        que.display()
        que.writeq(30)
        que.display()
        que.writeq(35)
        que.display()
        print('removed :', que.readq())
        que.display()
        print('removed :', que.readq())
        que.display()
        print('removed :', que.readq())
        que.display()
        print('removed :', que.readq())
        que.display()
    except IndexError as ine:
        print(ine.args)
    que.display()
main()




