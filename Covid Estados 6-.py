from tkinter import *
from tkinter.ttk import *

pantalla=Tk()
pantalla.title('COVID Estados')
pantalla.geometry('400x240')

opcion=StringVar()

etiesta=Label(pantalla,text='Estados')
etiesta.place(x=170,y=10)

coahuila=Radiobutton(pantalla,text='Coahuila',value='Coahuila',variable=opcion)
coahuila.place(x=160,y=40)
nuevoleon=Radiobutton(pantalla,text='Nuevo Leon',value='Nuevo Leon',variable=opcion)
nuevoleon.place(x=160,y=60)
tamaulipas=Radiobutton(pantalla,text='Tamaulipas',value='Tamaulipas',variable=opcion)
tamaulipas.place(x=160,y=80)
chihuahua=Radiobutton(pantalla,text='Chihuahua',value='Chihuahua',variable=opcion)
chihuahua.place(x=160,y=100)
sonora=Radiobutton(pantalla,text='Sonora',value='Sonora',variable=opcion)
sonora.place(x=160,y=120)
sinaloa=Radiobutton(pantalla,text='Sinaloa',value='Sinaloa',variable=opcion)
sinaloa.place(x=160,y=140)

def operacion():
    buscar=opcion.get()

    def busquedalineal(x,y):
        encontrar=False
        posicion=0
        while posicion<len(y) and not encontrar:
            if y[posicion]==x:
                encontrar=True
            posicion= posicion+1
        return encontrar        
    estados=['Coahuila',
             'Nuevo Leon',
             'Tamaulipas',
             'Chihuahua',
             'Sonora',
             'Sinaloa']
    
    busqueda=busquedalineal(buscar,estados)
    if busqueda:
        data={}
        
        data['Coahuila']=[]
        data['Coahuila'].append({'Muertes':1868,
                                 'Recuperados':21278,
                                'Hospitalizados':3831})
        data['Nuevo Leon']=[]
        data['Nuevo Leon'].append({'Muertes':3027,
                                 'Recuperados':28585,
                                'Hospitalizados':7904})
        data['Tamaulipas']=[]
        data['Tamaulipas'].append({'Muertes':2195,
                                 'Recuperados':23256,
                                'Hospitalizados':4472})
        data['Chihuahua']=[]
        data['Chihuahua'].append({'Muertes':1377,
                                 'Recuperados':7324,
                                'Hospitalizados':3296})
        data['Sonora']=[]
        data['Sonora'].append({'Muertes':2864,
                                 'Recuperados':18082,
                                'Hospitalizados':5756})
        data['Sinaloa']=[]
        data['Sinaloa'].append({'Muertes':3194,
                                 'Recuperados':11739,
                                'Hospitalizados':6403})

        
        pantalla2=Tk()
        pantalla2.title('COVID Estadisticas')
        pantalla2.geometry('400x200')
        
        archivo=open('covidprogramacion'+buscar+'.txt','w')
        
        for c in data[buscar]:
            eti=Label(pantalla2,text=(buscar))
            eti1=Label(pantalla2,text=('Muertes:',c['Muertes']))
            eti2=Label(pantalla2,text=('Recuperados:',c['Recuperados']))
            eti3=Label(pantalla2,text=('Hospitalizados:',c['Hospitalizados']))
            
            c['Muertes']=str(c['Muertes'])
            c['Recuperados']=str(c['Recuperados'])
            c['Hospitalizados']=str(c['Hospitalizados'])
            
            archivo.write(buscar)
            archivo.write('\n'+'Muertes: '+c['Muertes'])
            archivo.write('\n'+'Recuperados: '+c['Recuperados'])
            archivo.write('\n'+'Hospitalizados: '+c['Hospitalizados']+'\n\n')
            
        archivo.close()
        
        etia=Label(pantalla2,text='Se guardaron correctamente los datos en')
        etib=Label(pantalla2,text='el archivo de texto "covidprogramacion'+buscar+'.txt"')
        etia.place(x=85,y=150)
        etib.place(x=60,y=170)
        
        eti.place(x=150,y=20)
        eti1.place(x=150,y=60)
        eti2.place(x=150,y=80)
        eti3.place(x=150,y=100)
        
        pantalla2.mainloop()
    else:
        pantalla2=Tk()
        pantalla2.title('COVID Estadisticas')
        pantalla2.geometry('400x200')

        no=Label(pantalla2,text='Selecciona una opcion del menu por favor')
        no.place(x=88,y=80)

        pantalla2.mainloop()

enter=Button(pantalla,text='Enter',command=operacion)
enter.place(x=160,y=190)

pantalla.mainloop()
