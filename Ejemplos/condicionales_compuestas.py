calificacion = 100

# if calificacion < 61:
#     print("lo sentimos, ud. perdió")
# elif calificacion > 85:
#     print("usted ganó con honores")
# else:
#     print("usted ganó")

if calificacion < 61:
    print("Usted perdió")
else:
    if calificacion > 85:
        if calificacion > 95:
            if calificacion == 100:
                print("SUPER STAR")
            else:
                print("usted ganó - suma cum laude")
        else:
            print("usted ganó - magna cum laude")
    else:
        print("usted ganó")