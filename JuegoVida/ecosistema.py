
class ecosistema:


    ecosistemaArreglo = []

    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize
        self.__llenarEcosistema()

    def __llenarEcosistema(self):
        for numeroFilas in range(self.ySize):
            fila = []
            for datosFila in range(self.xSize):
                celula = {
                    "estado": "muerta",
                    "numeroVecinos": 0
                }
                fila.append(celula)
            self.ecosistemaArreglo.append(fila)

    def __contarVecinos(self, cordenadaX, cordenadaY):
        vecinos = 0
        for recorridoEnY in range(-1, 2, 1):
            cordenadaYDinamica = cordenadaY + recorridoEnY
            if cordenadaYDinamica >= 0 and cordenadaYDinamica < len(self.ecosistemaArreglo):
                # Busque Vecinos en X
                for recorridoEnX in range(-1, 2, 1):
                    cordenadaXDinamica = cordenadaX + recorridoEnX
                    if cordenadaXDinamica >= 0 and cordenadaXDinamica < len(self.ecosistemaArreglo[cordenadaY]):
                        if self.ecosistemaArreglo[cordenadaYDinamica][cordenadaXDinamica].get("estado") == "viva" \
                                and (cordenadaXDinamica != cordenadaX or cordenadaYDinamica != cordenadaY):
                            vecinos += 1
        #print(vecinos, cordenadaX, cordenadaY)
        self.ecosistemaArreglo[cordenadaY][cordenadaX]["numeroVecinos"] = vecinos

    def __actualizarVecinosCelulas(self):
        for fila in range(len(self.ecosistemaArreglo)):
            for indiceCelula in range(len(self.ecosistemaArreglo[fila])):
                self.__contarVecinos(indiceCelula, fila)

    def realizarIteracion(self):
        self.__actualizarVecinosCelulas()
        for indiceFila in range(len(self.ecosistemaArreglo)):
            for indiceCelula in range(len(self.ecosistemaArreglo[indiceFila])):
                celula = self.ecosistemaArreglo[indiceFila][indiceCelula]
                if celula.get("numeroVecinos") < 2 or celula.get("numeroVecinos") > 3:
                    self.ecosistemaArreglo[indiceFila][indiceCelula]["estado"] = "muerta"
                elif celula.get("estado") == "muerta" and celula.get("numeroVecinos") == 3:
                    self.ecosistemaArreglo[indiceFila][indiceCelula]["estado"] = "viva"

    def obtenerEcosistema(self):
        return self.ecosistemaArreglo

    def setEcosistema(self, ecosistema):
        self.ecosistemaArreglo = ecosistema