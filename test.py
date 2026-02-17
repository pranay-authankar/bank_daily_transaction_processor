class Sample:
    def __str__(self):
        return "a,b,c,d"
    

my_dict = {"1":Sample()}

my_dict["2"] = "Abd"

for x in my_dict:
    print(x)