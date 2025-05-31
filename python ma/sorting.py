p=[{"name":"arav","age":20,"place":"chn"},
   {"name":"abi","age":24,"place":"blr"},
   {"name":"ragu","age":18,"place":"chn"},
   {"name":"swe","age":21,"place":"vlr"},]
x=sorted(p,key=lambda y:y['age'])
print(x)