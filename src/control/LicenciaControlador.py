from src.modelo import Licencia
from src.modelo.DiasTomados import DiasTomados
from src.modelo.Persona import Persona


class LicenciaControlador():
    __empleados = list()


    def getListaEmpleados(self):
        return self.__empleados
        
    #Persona
    def buscarPersona(self, nroLegajoBuscado):
        empleadoBuscado = None
        for e in self.__empleados:
            if(e.getNroLegajo() == nroLegajoBuscado):
                empleadoBuscado=e
                break
        return empleadoBuscado 

    def addPersona(self, newEmpleado):
        print("\t└-->INICIO CREAR EMPLEADO (Módulo)")
        empleadoRepetido=None
        empleadoRepetido=self.buscarPersona(newEmpleado.getNroLegajo())
        # si no está repetido el nro de legajo
        if(empleadoRepetido==None):
            self.__empleados.append(newEmpleado)
            print(f"\t\t└->inserté el empleado {newEmpleado.getNombreApe()} con nro de legajo {newEmpleado.getNroLegajo()}\n")
        else:
            print(f"Ocurrio un error al intentar crear el empleado (Ya existe un empleado con el mísmo nro de legajo '{newEmpleado.getNroLegajo()}')")


    def delPersona(self, nroLegajoBuscado):
        personaBorrar=self.buscarPersona(self,nroLegajoBuscado)
        if(personaBorrar!=None):
            personaBorrar.setEstado(False)
        else:
            print(f"Ocurrio un error al intentar dar de baja el empleado (No se encontró el empleado con el nro de legajo '{nroLegajoBuscado}')")


    #dias correspondientes
    def generarDias_correspondiente(self, nroLegajoBuscado, diasCorrespNew):
        print("\t└-->INICIO GENERAR DÍAS CORRESP (Módulo)")
        empleado=self.buscarPersona(nroLegajoBuscado)
        if(empleado!=None):
            diasDuplicado = empleado.buscarDias_correspondiente(diasCorrespNew.getFecha())
            if(diasDuplicado==None):#si no esta repetido
                empleado.addDias_correspondiente(diasCorrespNew)
                print(f"\t\t└->inserté el día correspondiente del año '{diasCorrespNew.getFecha().strftime('%Y')}' con '{diasCorrespNew.getDias()}'"
                      f" días disponibles al legajo nro '{nroLegajoBuscado}'\n")
            else:
                print(f"Ocurrio un error al intentar dar días al empleado (Ya existen días asociados al año '{diasCorrespNew.getFecha().strftime('%Y')}' al nro de legajo)")
        else:
            print(f"Ocurrio un error al intentar dar días al empleado (No se encontró el empleado con el nro de legajo '{nroLegajoBuscado}')")


    def bajaDias_correspondiente(self, nroLegajoBuscado, diasCorrespBaja):
        empleado=self.buscarPersona(self, nroLegajoBuscado)
        if(empleado!=None):
            if(empleado.buscarDias_correspondiente(diasCorrespBaja) != None):
                empleado.buscarDias_correspondiente(diasCorrespBaja).setEstado(False)
            else:
                print(f"Ocurrio un error al intentar dar de baja los días al empleado (No se encontraron los días del año '{diasCorrespBaja.getFecha().strftime('%Y')}'")
        else:
            print(f"Ocurrio un error al intentar dar de baja los días al empleado (No se encontró el empleado con el nro de legajo '{nroLegajoBuscado}')")

    #Licencias

        # función que verifica si es posible los días que se quiere tomar el empleado
    def verificarCantidadDiasLic(self, diasCorrespTotalesEmple, NewLicencia):
        print("\t\t└-->INICIO VERIFICAR CANT DIAS LIC (Módulo)")
        verifica = False
        totalDiasDisponibles = 0
        diasPedidos = NewLicencia.getCantDias()
        for d in diasCorrespTotalesEmple:
            if (d.getEstado() == True):  # si son ocupables
                totalDiasDisponibles += d.getDias()
                if (totalDiasDisponibles >= diasPedidos):  # si dispongo de la cantidad usable de días
                    verifica = True
                    print(f"\t\t\t└->Existen suficientes días disponibles para generar la licencia solicitada "
                          f"existen mayor o igual a '{diasPedidos}' días pedidos en la licencia ('{totalDiasDisponibles}' existentes)\n")
                    break
        if(verifica==False):
            print(
                f"\t\t\t└->No existen suficientes días disponibles para generar la licencia solicitada"
                f" (La licencia '{NewLicencia.getFecha_ini()}' requiere '{NewLicencia.getCantDias()}' días)\n")
        return verifica

    # función que controla y llama a insertar la licencia
    def generarLicencia(self, nroLegajoBuscado, newLicencia):
        print("\t└-->INICIO GENERAR LICENCIA (Módulo)\n")
        empleado = self.buscarPersona(nroLegajoBuscado)
        if (empleado != None):
            licdupli = empleado.buscarLicencia(newLicencia.getFecha_ini(), newLicencia.getFecha_fin())
            if (licdupli is None):  # si la Lic no existe
                if (self.verificarCantidadDiasLic(empleado.getDias_correspondiente(), newLicencia) == True):#si hay suficientes dias para la lic

                    empleado.getLicencias().append(self.insertarLicencia(nroLegajoBuscado, newLicencia))
                    print(f"\t\t└->inserté la licencia del '{newLicencia.getFecha_ini().strftime('%d/%m/%Y')}' al empleado '{empleado.getNombreApe()}'\n")
            else:
                print(
                    f"Ocurrio un error al intentar generar licencia al empleado (Ya existe una licencia con la fecha '{newLicencia.getFecha_ini().strftime('%d/%m/%Y')}')")


    def insertarLicencia(self, nroLegajoBuscado, newLicencia):
        print("\t└-->INICIO INSERTAR LICENCIA (Módulo)")
        empleado = self.buscarPersona(nroLegajoBuscado)
        diasPedidos = newLicencia.getCantDias()
        diasPedidosCorresp = 0
        # recorremos los días correspondientes del empleado
        for dias in empleado.getDias_correspondiente():
            while ((diasPedidos > 0) and (dias.getEstado() == True)):  # si no se tomaron la cantidad de días para la lic, y ese dia corresp
                diasPedidos = diasPedidos - 1  # tiene aun dias tomables(se setea sola el estado en false si llega a cero)
                dias.setDias(dias.getDias() - 1)
                diasPedidosCorresp = diasPedidosCorresp + 1
            # cuando se terminan los de esos días se registra en la lista de lincencia de q años se tomaron los dias
            if(diasPedidosCorresp>0):
                diasTomados = DiasTomados(diasPedidosCorresp,dias.getFecha())#generamos los dias tomados
                newLicencia.addDiasTomados(diasTomados)
                print(f"\t\t└->se tomaron '{diasTomados.getCantidadDiasTomados()}' dias del año '{diasTomados.getAnioDiasCorresp().strftime('%Y')}'")
            for dTomadosEnLic in newLicencia.getDiasTomados():
                anio = dTomadosEnLic.getAnioDiasCorresp()
                print(f"\t\t\t└->la licencia '{newLicencia.getFecha_ini().strftime('%d/%m/%Y')}' tiene '{dTomadosEnLic.getCantidadDiasTomados()}' días "
                      f"del año '{anio.strftime('%Y')}'")
            diasPedidosCorresp = 0
            if (diasPedidos == 0):
                print(
                    f"\t\t└->La licencia del día '{newLicencia.getFecha_ini().strftime('%d/%m/%Y')}' ya tomo todos los días necesarios ('{newLicencia.getCantDias()}' días)")
                break  # si ya se llego a los dias pedidos, salimos del bucle (más óptimo)
        return newLicencia