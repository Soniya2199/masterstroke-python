
#~ Single level
# class Dad:
#     def phone(self):
#         print('Dads Phone')

# class Son(Dad):
#     def laptop(self):
#         print('Son Laptop')
# arav=Son()
# arav.phone() #! accessing parent cls inside child cls

#^ Multiple level
class Dad:
    def phone(self):
        print('Dads Phone')
class Mom():
    def sweet(self):
        print('Moms sweet')

class Son(Dad,Mom):
    def laptop(self):
        print('Son Laptop')
ar=Son()
ar.phone()
ar.sweet()

#& Multi level
#? Hierarchial
#~ Hybrid

#^ Super() keyword
