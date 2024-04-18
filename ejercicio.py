list_id = []
list_name = []
list_correo = []
list_contacto = []
list_edad = []
list_años_exp = []
list_profesion = []
list_ciudad = []
list_sexo = []
import os
def fnt_limpiar():
    os.system("")
    print('Autor: Santiago Barrera')
    print('Fecha: 18 de abril del 2024\n\n')

def fnt_registrar(id, name, correo, contacto, edad, años_exp, profesion, ciudad, sexo):
    if id == '' or name == '' or correo == '' or contacto == '' or edad == '' or años_exp == '' or profesion == '' or ciudad == '' or sexo == '':
        enter = input('\nError, debe ingresar todos los datos <ENTER>')
    else:
        list_id.append(id)
        list_name.append(name)
        list_correo.append(correo)
        list_contacto.append(contacto)
        list_edad.append(edad)
        list_años_exp.append(años_exp)
        list_profesion.append(profesion)
        list_ciudad.append(ciudad)
        list_sexo.append(sexo)
        enter = input('\nRegistro exitoso <ENTER>')

def fnt_selector(opcion):
    fnt_limpiar()
    if opcion == 1:
        id = input('ID: ')
        if id in list_id:
            enter = input('\nEste candidato ya esta registrado <ENTER>')
        else:
            if edad <= 25 or edad >= 35:
                enter = input('\nDebe cumplir con la edad promedio')
            else: 
                if años_exp <= 2 or años_exp >= 4:
                    enter = input('\nDebe cumplir con los años de experiencia')
                else:
                    name = input('Nombre: ')
                    
                    correo = input('Correo: ')

                    contacto = input('Contacto: ')

                    edad = input('Edad: ')

                    años_exp = input('Años de experiencia: ')

                    profesion = input('Profesión: ')

                    ciudad = input('Ciudad: ')

                    sexo = input('Sexo: ')

                    fnt_registrar(id, name, correo, contacto, edad, años_exp, profesion, ciudad, sexo)
    elif opcion == 2:
        fnt_limpiar()
        for i in range(len(list_id)):
            print(f'{list_id[i]}, "  ", {list_name[i]}, "  ", {list_correo}, "  ", {list_contacto[1]}, "  " {list_edad[i]}, "  ", {list_años_exp[1]}, "  ", {list_profesion[1]}, "  ", {list_ciudad[1]}, "  ", {list_sexo[1]} ')
        enter = input('\nPresiona <ENTER> para continuar... ')
sw = True 
while sw == True:        
    fnt_limpiar()   
    op = input('\n\n<<<<< MENU PRINCIPAL >>>>>>\n1. REGISTRAR\n2. CONSULTAR\n3. SALIR\n--> ') 
    fnt_selector(op) 