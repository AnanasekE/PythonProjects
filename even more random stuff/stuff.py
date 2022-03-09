class BinaryNumber:
    def __init__(self,number):
        binary = ""
        while number > 0:
            if number % 2 == 0:
                binary += "0"
            else:
                binary += "1"
            number //= 2
        self.binary = self.binary[::1]

def show(self):
    print(self.binary)



                
# Do not remove the following lines
# if __name__ == '__main__':
#   value = int(input())
#   binary = BinaryNumber(value)
#   binary.show()