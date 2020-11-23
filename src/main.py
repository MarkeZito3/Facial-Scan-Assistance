import webcam
from datetime import date
import os

mes = {
        1:"Enero",
        2:"Febrero",
        3:"Marzo",
        4:"Abril",
        5:"Mayo",
        6:"Junio",
        7:"Julio",
        8:"Agosto",
        9:"Septiembre",
        10:"Octubre",
        11:"Noviembre",
        12:"Diciembre"
    }
dia_semana = {
        0:"Lunes",
        1:"Martes",
        2:"Miércoles",
        3:"Jueves",
        4:"Viernes",
        5:"Sábado",
        6:"Domingo"
    }
fecha = dia_semana[date.today().weekday()] + " " + str(date.today().day) + " de " + mes[date.today().month] + " del " + str(date.today().year)


menu = """
\t\t\t\t\t"""+fecha+"""
==========================================================================
||\t\tBIENVENIDO/A A "FACIAL SCAN ASSISTANCE"\t\t\t||
==========================================================================\n
==========================================================================
||\tPrecione el Número de la opción que desee:\t\t\t||
||\t\t1) Agregar nuevos alumnos\t\t\t\t||
||\t\t2) Tomar asistencia de los alumnos presentes\t\t||
||\t\t3) Ver lista de los alumnos totales\t\t\t||
||\t\t4) Salir\t\t\t\t\t\t||
=========================================================================="""

while_menu = True

while while_menu == True:
    print(menu)
    op = int(input('\t\tNumero Ingresado: '))

    if op == 1:
        menu_op_1 = True
        while menu_op_1 == True:

            person_name = input("Ingrese el nombre del nuevo alumno: ")
            print("==========================================================================")
            webcam.camara(person_name)
            os.system("cls")
            skip = int(input("==========================================================================\n"
                             "1:[volver al Menu Pricipal]\n"
                             "2:[Ingresar un nuevo Alumnos o uno ya existente]\n"
                             "3:[Salir]\n"
                             "Opción: "))
            if skip == 1:
                os.system("cls")
                webcam.training()
                break
            elif skip == 2:
                menu_op_1 = True
                os.system("cls")
            elif skip == 3:
                while_menu = False
                webcam.training()
                os.system("cls")
                break
        os.system("cls")

    elif op == 2:
        menu_op_2 = True
        while menu_op_2 == True:
            print("==========================================================================")
            webcam.assistance()
            print("==========================================================================\n")
            os.system("cls")
            skip = int(input("==========================================================================\n"
                             "1:[volver al Menu Pricipal]\n"
                             "2:[Volver a ver tomar asistencia]\n"
                             "3:[Salir]\n"
                             "Opción: "))
            if skip == 1:
                os.system("cls")
                break
            elif skip == 2:
                menu_op_2 = True
                os.system("cls")
            elif skip == 3:
                while_menu = False
                os.system("cls")
                break

    elif op == 3:
        menu_op_3 = True
        while menu_op_3 == True:
            lista_alum = webcam.lista()
            cont = 1
            os.system("cls")
            print("==========================================================================")
            for x in lista_alum:
                print(cont,")" ,x)
                cont+= 1
            skip = int(input("==========================================================================\n"
                         "1:[volver al Menu Pricipal]\n"
                         "2:[Volver a ver la Lista de Alumnos]\n"
                         "3:[Salir]\n"
                         "Opción: "))
            if skip == 1:
                os.system("cls")
                break
            elif skip == 2:
                menu_op_3 = True
                os.system("cls")
            elif skip == 3:
                while_menu = False
                os.system("cls")
                break

    elif op == 4:
        while_menu = False
        os.system("cls")

print("""==========================================================================
||\t\t\tEl programa ha Finalizado\t\t\t||
||\t\t\tRevisar la Carpeta "Presentes"\t\t\t||
==========================================================================""")