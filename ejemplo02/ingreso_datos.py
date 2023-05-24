from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()



# proceso 
#
# acceder al archivo
archivo = open('data/datos_clubs.txt', "r", encoding="utf8")

# obtener las líneas del archivo
lineas = archivo.readlines()

# lineas es ina lista de cadenas

# se imprime las siguientes posiciones



lista = [l.replace("\n", "").split(";") for l in lineas]


# lineas es ina lista de cadenas
# se imprime las siguientes posiciones

for l in lista :
    print(l)

    club = Club(nombre=l[0], deporte=l[1], \
        fundacion=int(l[2]))
    
    session.add(club)
    
    
    

archivo.close()







# proceso 
#
# acceder al archivo
archivo = open('data/datos_jugadores.txt', "r", encoding="utf8")

# obtener las líneas del archivo
lineas = archivo.readlines()

# lineas es ina lista de cadenas

# se imprime las siguientes posiciones



lista = [l.replace("\n", "").split(";") for l in lineas]


# lineas es ina lista de cadenas
# se imprime las siguientes posiciones

for l in lista :
    print(l)
    club =session.query(Club).filter_by(nombre=l[0]).one()
    jugadores = Jugador(nombre=l[3],  dorsal= l[2], posicion=l[1], \
        club=club) 
    

    session.add(jugadores)



session.commit()