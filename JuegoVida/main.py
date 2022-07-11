from ecosistema import ecosistema
import time

ecosistema = ecosistema(15, 15)
ArregloEcosistema = ecosistema.obtenerEcosistema()

#Entra jugador
ArregloEcosistema[0][1]["estado"] = "viva"
ArregloEcosistema[1][2]["estado"] = "viva"
ArregloEcosistema[2][0]["estado"] = "viva"
ArregloEcosistema[2][1]["estado"] = "viva"
ArregloEcosistema[2][2]["estado"] = "viva"
ecosistema.setEcosistema(ArregloEcosistema)
#termina Jugador

#mostrarEcosistema

while(True):
    for fila in ArregloEcosistema:
        for dato in fila:
            if dato.get("estado") == "muerta":
                print(" . ", end="")
            else:
                print(" V ", end="")
        print("")
    print("-----------")
    ecosistema.realizarIteracion()
    time.sleep(0.5)


