print("Parol daxil edin: ")
say=1
while say<=3:
    a=input()
    if len(a)>=8 and len(a)<=13:
        print("Sisteme daxil oldunuz")
        break
    else:
        print("Sifre yanlisdir")
    