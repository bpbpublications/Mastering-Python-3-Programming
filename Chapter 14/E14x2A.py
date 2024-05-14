# Program E14x2 - lines 30 commented
#  simulates stack using list
class Stk:
    def get_data(self, lis, size, top):
        self.lis=lis
        self.size=size
        self.top=top
    def spush(self, ele):
        if self.top>=self.size:
            raise IndexError("Stack Full")
        else:
            self.lis.append(ele)
            self.top+=1
    def spop(self):
        if self.top==0:
            raise IndexError("Stack Empty")
        else:
            ele=self.lis.pop()
            self.top-=1
            return ele
    def display(self):
            print(self.lis)
def main():
    try:
        st=Stk()
        st.get_data([], 3, 0)
        st.spush(10)
        st.spush(20)
        st.spush(30)
       # st.spush(40)
        ele=st.spop()
        print(ele)
        ele=st.spop()
        print(ele)
        ele=st.spop()
        print(ele)
        ele=st.spop()
        print(ele)

    except IndexError as ine:
        print(ine.args)
    st.display()
    
      
main()




