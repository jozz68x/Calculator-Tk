# -*- coding: utf-8 -*-

__author__ = "Jose Diaz"
__copyright__ = "Copyright (C) 2015, Jose Diaz"
__license__ = "GPL v3.0"
__version__ = "1.0"
__revision__ = "12"
__date__ = "$06/03/2015 03:49:20 AM$"
__status__ = "Desarrollo"
__contact__ = "966403361"
__email__ = "jozz.18x@gmail.com"

from tkinter import *
from PIL import Image, ImageTk
from tkinter import colorchooser
from modulos.beep import Beep
from modulos.acerca_de import AcercaDe
import math

class Calculadora(Frame):
    """
    Interfaz de la Calculadora Basica y Cientifica
    incluye las funcionalidades de los metodos matematicos.
    """
    
    BG_BUTTON = "#424242"
    BG_BUTTON_2 = "#212121"
    BG_BLACK = "#000000"
    FG = "#FFFFFF"
    FONT = font=("Microsoft Yi Baiti", 19)
    
    BG_BUTTON_TEMACLARO = "#ECEFF1"
    BG_BUTTON_2_TEMACLARO = "#CFD8DC"
    BG_BLACK_TEMACLARO = "#FFFFFF"
    FG_TEMACLARO = "#455A64"
    
    BG_BUTTON_TEMAIOS7 = "#d9dadc"
    BG_BUTTON_2_TEMAIOS7 = "#f78f12"
    BG_BLACK_TEMAIOS7 = "#000000"
    FG_TEMAIOS7 = "BLACK"
    
    LABEL = dict(font=("Arial Unicode MS",9), relief=FLAT, bd=0, height=1,
                        fg="#00BFA5", activebackground="BLACK", activeforeground="#1DE9B6")
    ENTRY = dict(font=("Arial Unicode MS", 20), relief=FLAT, bd=0,
                        insertwidth="1p", justify=RIGHT)
    BUTTON = dict(font=(FONT[0], 27), relief=FLAT, bd=0, width=4,
                        activebackground="#00BFA5", activeforeground="WHITE",
                        bg=BG_BUTTON, fg="WHITE")
    BUTTON_CIENTIFICA = dict(relief=FLAT, bd=0, width=6, height=2,
                        font=FONT, bg=BG_BUTTON_2, fg="WHITE",
                        activebackground="#00BFA5", activeforeground="WHITE")
    PADDING = dict(padx=1, pady=1)
    
    
    BUTTON_TEMACLARO = dict(bg=BG_BUTTON_TEMACLARO, fg=FG_TEMACLARO, 
                      activebackground="#00E5FF", activeforeground="BLACK")
    BUTTON_CIENTIFICA_TEMACLARO = dict(bg=BG_BUTTON_2_TEMACLARO, fg=FG_TEMACLARO, 
                                 activebackground="#1DE9B6", activeforeground=FG_TEMACLARO)
    
    BUTTON_TEMAOSCURO = dict(bg=BG_BUTTON, fg=FG,
                      activebackground="#00BFA5", activeforeground="BLACK")
    BUTTON_CIENTIFICA_TEMAOSCURO = dict(bg=BG_BUTTON_2, fg=FG,
                                 activebackground="#00BFA5", activeforeground=FG)
    
    BUTTON_TEMAIOS7 = dict(bg=BG_BUTTON_TEMAIOS7, fg=FG_TEMAIOS7, 
                      activebackground="#F5F5F5", activeforeground=FG_TEMAIOS7)
    BUTTON_CIENTIFICA_TEMAIOS7 = dict(bg=BG_BUTTON_2_TEMAIOS7, fg="WHITE", 
                                 activebackground="#fba743", activeforeground="WHITE")
    
    
    @classmethod
    def main(cls):
        """Metodo principal"""
        root = Tk()
        root.title("Calculator-Tk")
        #root.overrideredirect(True)
        root.resizable(width=False, height=False) 
        root.geometry("288x437+500+150")
        
        root.wm_iconbitmap(r"images\Icon.ico")
        
        cls(root)
        root.mainloop()
        
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.master['bg'] = self.BG_BLACK
        
        self.cargar_imagenes()
        
        self.etiqueta = self.etiqueta_entry()
        self.etiqueta.pack(fill=X, padx=5)
        
        self.cabecera = self.frame_entry()
        self.cabecera.pack(fill=X, padx=5, pady=5)
        
        self.barra_borrar = self.barra_borrar()
        self.barra_borrar.pack(fill=X)
        
        self.calculadora_basico()
        
        self.eventos_keypress()
    
    def cargar_imagenes(self):
        #Image
        self.imagenLight = ImageTk.PhotoImage(Image.open(r"images\light.png"))
        self.imagenDark = ImageTk.PhotoImage(Image.open(r"images\dark.png"))
        self.imagenIOS = ImageTk.PhotoImage(Image.open(r"images\ios.png"))
        self.imagenPersonalice = ImageTk.PhotoImage(Image.open(r"images\personalize.png"))
        #SelectImage
        self.imagenLightSelect = ImageTk.PhotoImage(Image.open(r"images\light_select.png"))
        self.imagenDarkSelect = ImageTk.PhotoImage(Image.open(r"images\dark_select.png"))
        self.imagenIOSSelect = ImageTk.PhotoImage(Image.open(r"images\ios_select.png"))
     
    def calculadora_basico(self):
        self.master.geometry("288x437+500+150")
        self.basico = self.widgets_basico()
        self.basico.pack(side=RIGHT)
        
    def calculadora_cientifica(self):        
        self.master.geometry("658x437+500+150")
        self.cientifica = self.widgets_cientifica()
        self.cientifica.pack(side=RIGHT)
        
    def etiqueta_entry(self):
        etiqueta = Frame(self.master, bg=self.BG_BLACK)
        
        self.btn_sistema = Button(etiqueta, text="DEC", bg=etiqueta['bg'], **self.LABEL)
        self.btn_sistema.pack(side=LEFT, anchor=W)
        self.lb_separador = Label(etiqueta, text="|", bg=etiqueta['bg'], **self.LABEL)
        self.lb_separador.pack(side=LEFT)
        self.btn_conversion = Button(etiqueta, text="RAD", command=self.degrees, bg=etiqueta['bg'], **self.LABEL)
        self.btn_conversion.pack(side=LEFT, anchor=E)
        
        return etiqueta
    
    def frame_entry(self):
        frame = Frame(self.master, bg=self.BG_BLACK)
        
        img = Image.open(r"images\menu.png")
        self.IconMenu = ImageTk.PhotoImage(img)
        
        self.btn_menu = Menubutton(frame, image=self.IconMenu, relief=FLAT, bd=0, bg=frame['bg'], activebackground="#424242", direction='left')
        self.btn_menu.pack(side=RIGHT, anchor=W)
        menu = Menu(self.btn_menu, tearoff=0, font=("Arial", 10), activebackground="#00BFA5", activeforeground = "BLACK")
        menu.add_radiobutton(label="Standar", accelerator='Alt+1', command=lambda: self.calculadora_basico())
        menu.add_radiobutton(label="Scientific", accelerator='Alt+2', command=lambda: self.calculadora_cientifica())
        menu.add_separator()
        sub_menu_archivo = Menu(menu, tearoff=0, font=("Arial", 10), activebackground="#00BFA5", activeforeground = "BLACK")
        menu.add_cascade(label='Theme', menu=sub_menu_archivo)
        sub_menu_archivo.add_radiobutton(label = " Dark", command=self.tema_oscuro, image=self.imagenDark, compound=TOP, columnbreak=True, selectimage=self.imagenDarkSelect, selectcolor="TEAL")
        sub_menu_archivo.add_radiobutton(label = " Light", command=self.tema_claro, image=self.imagenLight, compound=TOP, columnbreak=False, selectimage=self.imagenLightSelect, selectcolor="TEAL")
        sub_menu_archivo.add_radiobutton(label = " iOS", command=self.tema_ios7, image=self.imagenIOS, compound=TOP, columnbreak=True, selectimage=self.imagenIOSSelect, selectcolor="TEAL")
        sub_menu_archivo.add_command(label = " Personalize", command=self.cambiar_tema, image=self.imagenPersonalice, compound=TOP, columnbreak=False)
        menu.add_separator()
        sub_menu_ayuda = Menu(menu, tearoff=0, font=("Arial", 10), activebackground="#00BFA5", activeforeground = "BLACK")
        menu.add_cascade(label='Help', menu=sub_menu_ayuda)
        sub_menu_ayuda.add_command(label='Help', accelerator='F1', command=lambda: self.ayuda())
        sub_menu_ayuda.add_separator()
        sub_menu_ayuda.add_command(label='About Calculator', command=lambda: self.acerca_de_calculadora())
        self.btn_menu["menu"] = menu
                
        self.entry = Entry(frame, bg=self.BG_BLACK, insertbackground="WHITE", fg="WHITE", **self.ENTRY)
        self.entry.pack(side=RIGHT, anchor=E, fill=X, expand=1, padx=5)
        self.entry.focus_set()
        self.entry.icursor(END)
        
        return frame
        
    def barra_borrar(self):
        frame = Frame(self.master, bg=self.BG_BLACK)
        
        self.btn_limpiar_entry = Button(frame, text="BORRAR", command=self.btn_borrar, 
                        relief=FLAT, bd=0, font=("Arial Unicode MS", 10), 
                        bg=self.BG_BUTTON_2, fg="WHITE", width=7,
                        activebackground="TEAL", activeforeground="WHITE")
        self.btn_limpiar_entry.pack(side=RIGHT, ipadx=4, ipady=5, **self.PADDING)

        self.btn_historial = Button(frame, relief=FLAT, bd=0, text=" ", 
                        font=("Arial Unicode MS", 10), bg=self.BG_BUTTON_2, 
                        fg="WHITE", activebackground="#263238", 
                        activeforeground="WHITE")
        self.btn_historial.pack(fill=X, ipady=5, **self.PADDING)
        
        return frame
    
    def widgets_basico(self, event=None):
        basico = Frame(self.master, bg=self.BG_BLACK)
        
        self.btns = ["7","8","9","/","4","5","6","*","1","2","3","-",".","0","=","+"]
        
        '''
        fila = 1
        columna = 0
        for bt in self.btns:
            self.comando = lambda x=bt : self.calcular_basico(x)
            self.boton = Button(basico, text=self.btns[5], command=lambda x=self.btns[5]: self.calcular_basico(x), **self.BUTTON)
            self.boton.grid(row=fila, column=columna, sticky=S+E+W+N, ipady=10, **self.PADDING)
            columna += 1
            if columna > 3:
                self.boton.config(bg=self.BG_BUTTON_2)
                columna = 0
                fila += 1
            if columna==3 and fila==4:
                self.boton.config(bg=self.BG_BUTTON_2)
        '''
            
        self.btn_7 = Button(basico, text=self.btns[0], command=lambda x=self.btns[0]: self.calcular_basico(x), **self.BUTTON)
        self.btn_7.grid(row=0, column=0, sticky=S+E+W+N, ipady=10, **self.PADDING)        
        self.btn_8 = Button(basico, text=self.btns[1], command=lambda x=self.btns[1]: self.calcular_basico(x), **self.BUTTON)
        self.btn_8.grid(row=0, column=1, sticky=S+E+W+N, ipady=10, **self.PADDING)        
        self.btn_9 = Button(basico, text=self.btns[2], command=lambda x=self.btns[2]: self.calcular_basico(x), **self.BUTTON)
        self.btn_9.grid(row=0, column=2, sticky=S+E+W+N, ipady=10, **self.PADDING)        
        self.btn_division = Button(basico, text="/", command=lambda x=self.btns[3]: self.calcular_basico(x), **self.BUTTON)
        self.btn_division.grid(row=0, column=3, sticky=S+E+W+N, ipady=10, **self.PADDING)
        self.btn_division.config(bg=self.BG_BUTTON_2, fg="WHITE")
        self.btn_4 = Button(basico, text=self.btns[4], command=lambda x=self.btns[4]: self.calcular_basico(x), **self.BUTTON)
        self.btn_4.grid(row=1, column=0, sticky=S+E+W+N, ipady=10, **self.PADDING)        
        self.btn_5 = Button(basico, text=self.btns[5], command=lambda x=self.btns[5]: self.calcular_basico(x), **self.BUTTON)
        self.btn_5.grid(row=1, column=1, sticky=S+E+W+N, ipady=10, **self.PADDING)        
        self.btn_6 = Button(basico, text=self.btns[6], command=lambda x=self.btns[6]: self.calcular_basico(x), **self.BUTTON)
        self.btn_6.grid(row=1, column=2, sticky=S+E+W+N, ipady=10, **self.PADDING)        
        self.btn_multiplicacion = Button(basico, text="x", command=lambda x=self.btns[7]: self.calcular_basico(x), **self.BUTTON)
        self.btn_multiplicacion.grid(row=1, column=3, sticky=S+E+W+N, ipady=10, **self.PADDING)
        self.btn_multiplicacion.config(bg=self.BG_BUTTON_2, fg="WHITE")
        self.btn_1 = Button(basico, text=self.btns[8], command=lambda x=self.btns[8]: self.calcular_basico(x), **self.BUTTON)
        self.btn_1.grid(row=2, column=0, sticky=S+E+W+N, ipady=10, **self.PADDING)        
        self.btn_2 = Button(basico, text=self.btns[9], command=lambda x=self.btns[9]: self.calcular_basico(x), **self.BUTTON)
        self.btn_2.grid(row=2, column=1, sticky=S+E+W+N, ipady=10, **self.PADDING)        
        self.btn_3 = Button(basico, text=self.btns[10], command=lambda x=self.btns[10]: self.calcular_basico(x), **self.BUTTON)
        self.btn_3.grid(row=2, column=2, sticky=S+E+W+N, ipady=10, **self.PADDING)        
        self.btn_resta = Button(basico, text=self.btns[11], command=lambda x=self.btns[11]: self.calcular_basico(x), **self.BUTTON)
        self.btn_resta.grid(row=2, column=3, sticky=S+E+W+N, ipady=10, **self.PADDING) 
        self.btn_resta.config(bg=self.BG_BUTTON_2, fg="WHITE")
        self.btn_punto = Button(basico, text=self.btns[12], command=lambda x=self.btns[12]: self.calcular_basico(x), **self.BUTTON)
        self.btn_punto.grid(row=3, column=0, sticky=S+E+W+N, ipady=10, **self.PADDING)        
        self.btn_0 = Button(basico, text=self.btns[13], command=lambda x=self.btns[13]: self.calcular_basico(x), **self.BUTTON)
        self.btn_0.grid(row=3, column=1, sticky=S+E+W+N, ipady=10, **self.PADDING)        
        self.btn_igual = Button(basico, text=self.btns[14], command=lambda x=self.btns[14]: self.calcular_basico(x), **self.BUTTON)
        self.btn_igual.grid(row=3, column=2, sticky=S+E+W+N, ipady=10, **self.PADDING) 
        self.btn_igual.config(bg=self.BG_BUTTON_2, fg="WHITE")
        self.btn_suma = Button(basico, text=self.btns[15], command=lambda x=self.btns[15]: self.calcular_basico(x), **self.BUTTON)
        self.btn_suma.grid(row=3, column=3, sticky=S+E+W+N, ipady=10, **self.PADDING)
        self.btn_suma.config(bg=self.BG_BUTTON_2, fg="WHITE")
        
        return basico
    
    def widgets_cientifica(self):
        cientifica = Frame(self.master, bg=self.BG_BLACK)
        
        self.btn_sen = Button(cientifica, text="sen", command=self.seno, **self.BUTTON_CIENTIFICA)
        self.btn_sen.grid(row=0, column=0, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_cos = Button(cientifica, text="cos", command=self.coseno, **self.BUTTON_CIENTIFICA)
        self.btn_cos.grid(row=0, column=1, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_tan = Button(cientifica, text="tan", command=self.tangente, **self.BUTTON_CIENTIFICA)
        self.btn_tan.grid(row=0, column=2, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_fact = Button(cientifica, text="!", command=self.factorial, **self.BUTTON_CIENTIFICA)
        self.btn_fact.grid(row=0, column=3, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_abs = Button(cientifica, text="abs", command=self.absoluto, **self.BUTTON_CIENTIFICA)
        self.btn_abs.grid(row=0, column=4, sticky=S+E+W+N, ipady=7, **self.PADDING)
        
        self.btn_asen = Button(cientifica, text="asen", command=self.cosecante, **self.BUTTON_CIENTIFICA)
        self.btn_asen.grid(row=1, column=0, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_acos = Button(cientifica, text="acos", command=self.secante, **self.BUTTON_CIENTIFICA)
        self.btn_acos.grid(row=1, column=1, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_atan = Button(cientifica, text="atan", command=self.cotangente, **self.BUTTON_CIENTIFICA)
        self.btn_atan.grid(row=1, column=2, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_In = Button(cientifica, text="In", command=self.ln, **self.BUTTON_CIENTIFICA)
        self.btn_In.grid(row=1, column=3, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_log = Button(cientifica, text="log", command=self.logaritmo, **self.BUTTON_CIENTIFICA)
        self.btn_log.grid(row=1, column=4, sticky=S+E+W+N, ipady=7, **self.PADDING)
        
        self.btn_raiz_2 = Button(cientifica, text="raiz 2", command=self.raiz_cuadrada, **self.BUTTON_CIENTIFICA)
        self.btn_raiz_2.grid(row=2, column=0, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_pot_2 = Button(cientifica, text="pot 2", command=self.potencia_cuadrado, **self.BUTTON_CIENTIFICA)
        self.btn_pot_2.grid(row=2, column=1, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_pot_3 = Button(cientifica, text="pot 3", command=self.potencia_cubo, **self.BUTTON_CIENTIFICA)
        self.btn_pot_3.grid(row=2, column=2, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_pi = Button(cientifica, text="pi", command=self.pi, **self.BUTTON_CIENTIFICA)
        self.btn_pi.grid(row=2, column=3, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_e = Button(cientifica, text="e", command=self.e, **self.BUTTON_CIENTIFICA)
        self.btn_e.grid(row=2, column=4, sticky=S+E+W+N, ipady=7, **self.PADDING)
        
        self.btn_X = Button(cientifica, text="X", command=self.X, **self.BUTTON_CIENTIFICA)
        self.btn_X.grid(row=3, column=0, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_X.config(bg="#424242")
        self.btn_Y = Button(cientifica, text="Y", command=self.Y, **self.BUTTON_CIENTIFICA)
        self.btn_Y.grid(row=3, column=1, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_Y.config(bg="#424242")
        self.btn_mod = Button(cientifica, text="mod", command=self.modulo, **self.BUTTON_CIENTIFICA)
        self.btn_mod.grid(row=3, column=2, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_parentesis_open = Button(cientifica, text="(", command=self.parentesis_abrir, **self.BUTTON_CIENTIFICA)
        self.btn_parentesis_open.grid(row=3, column=3, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_parentesis_open.config(bg="#424242")
        self.btn_parentesis_close = Button(cientifica, text=")", command=self.parentesis_cerrar, **self.BUTTON_CIENTIFICA)
        self.btn_parentesis_close.grid(row=3, column=4, sticky=S+E+W+N, ipady=7, **self.PADDING)
        self.btn_parentesis_close.config(bg="#424242")
        
        return cientifica
    
    def limpiar_entry(self):
        """ Metodo privado para limpiar el entry."""
        self.entry.delete(0, END)
        
    def btn_borrar(self):
        Beep.sonido(20)
        self.entry.delete(0, END)
    
    # Funciones y metodos matematicos
    
    def calcular_basico(self, valor):
        Beep.sonido(30)
        if valor == "=":
            tudo = "*/-+.123456789()"
            if self.entry.get() == "":
                pass
            elif self.entry.get()[0] not in tudo:
                self.limpiar_entry()
                self.entry.insert(END,"Operacion invalida")
            try:
                resultado = eval(self.entry.get())
                self.limpiar_entry()
                self.entry.insert(END, str(resultado))
            except:
                self.limpiar_entry()
                self.entry.insert(END,"Error")
        else:
            if "=" in self.entry.get():
                self.limpiar_entry()
            self.entry.insert(END, valor)
    
    
    def degrees(self):
        Beep.sonido(50)
        self.btn_conversion.config(text="DEG", command=self.radians)
        """ Converts angle x from radians to degrees."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                x = float(self.entry.get())
                degrees = math.degrees(x)
                self.limpiar_entry()
                self.entry.insert(END, str(degrees))
            else:
                x = int(self.entry.get())
                degrees = math.degrees(x)
                self.limpiar_entry()
                self.entry.insert(END, str(degrees))
        
    def radians(self):
        Beep.sonido(50)
        self.btn_conversion.config(text="RAD", command=self.degrees)
        """ Converts angle x from degrees to radians."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                x = float(self.entry.get())
                radians = math.radians(x)
                self.limpiar_entry()
                self.entry.insert(END, str(radians))
            else:
                x = int(self.entry.get())
                radians = math.radians(x)
                self.limpiar_entry()
                self.entry.insert(END, str(radians))
        
        
    def seno(self):
        Beep.sonido(30)
        """ Return the sine of x radians."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                sin = math.sin(float(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(sin))
            else:
                sin = math.sin(int(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(sin))
                
    def coseno(self):
        Beep.sonido(30)
        """ Return the cosine of x radians."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                cos = math.cos(float(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(cos))
            else:
                cos = math.cos(int(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(cos))
                
    def tangente(self):
        Beep.sonido(30)
        """ Return the tangent of x radians."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                tan = math.tan(float(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(tan))
            else:
                tan = math.tan(int(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(tan))
    
    def cotangente(self):
        Beep.sonido(30)
        """ Return the arc tangent of x, in radians."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                atan = math.acos(float(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(atan))
            else:
                atan = math.atan(int(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(atan))
        
    def secante(self):
        Beep.sonido(30)
        """ Return the arc cosine of x, in radians."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                acos = math.acos(float(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(acos))
            else:
                acos = math.acos(int(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(acos))
        
    def cosecante(self):
        Beep.sonido(30)
        """ Return the arc sine of x, in radians."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                asen = math.asin(float(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(asen))
            else:
                asen = math.asin(int(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(asen))
    
    def pi(self):
        Beep.sonido(30)
        """ The mathematical constant ? = 3.141592..., to available precision."""
        valor_pi = math.pi
        self.limpiar_entry()
        self.entry.insert(END, str(valor_pi))
        
    def e(self):
        Beep.sonido(30)
        """ The mathematical constant e = 2.718281..., to available precision."""
        valor_e = math.e
        self.limpiar_entry()
        self.entry.insert(END, str(valor_e))
        
    def factorial(self):
        Beep.sonido(30)
        """ Return x factorial. Raises ValueError if x is not integral or is negative."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y negativos"""
            if "." in self.entry.get():
                self.entry.config(fg="RED")
                self.limpiar_entry()
                self.entry.insert(END,"Is not integral")
            elif "-" in self.entry.get():
                self.entry.config(fg="RED")
                self.limpiar_entry()
                self.entry.insert(END,"Is negative")
            else:
                factorial = math.factorial(eval(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(factorial))
    
    def modulo(self):
        Beep.sonido(30)
        """Inserta el simbolo del modulo en el Entry."""
        self.entry.insert(END, "%")
        
    def ln(self):
        Beep.sonido(30)
        
    def logaritmo(self):
        Beep.sonido(30)
        """Return the base-10 logarithm of x. This is usually more accurate than log(x, 10)."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                log = math.log10(float(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(log))
            else:
                log = math.log10(int(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(log))
        
    
    def raiz_cuadrada(self):
        Beep.sonido(30)
        """ Return the square root of x."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                num = float(self.entry.get())
                raiz = math.sqrt(num)
                self.limpiar_entry()
                self.entry.insert(END, str(raiz))
            else:
                num = int(self.entry.get())
                raiz = math.sqrt(num)
                self.limpiar_entry()
                self.entry.insert(END, str(raiz))
    
    def potencia_cuadrado(self):
        Beep.sonido(30)
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                cuadrado = float(self.entry.get())**2
                self.limpiar_entry()
                self.entry.insert(END, str(cuadrado))
            else:
                cuadrado = int(self.entry.get())**2
                self.limpiar_entry()
                self.entry.insert(END, str(cuadrado))

    def potencia_cubo(self):
        Beep.sonido(30)
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                cubo = float(self.entry.get())**3
                self.limpiar_entry()
                self.entry.insert(END, str(cubo))
            else:
                cubo = int(self.entry.get())**3
                self.limpiar_entry()
                self.entry.insert(END, str(cubo))
                
    def redondeo_dos_decimales(self):
        Beep.sonido(30)
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                num = round(float(self.entry.get()), 2)
                self.limpiar_entry()
                self.entry.insert(END, str(num))
            else:
                num = round(int(self.entry.get()), 2)
                self.limpiar_entry()
                self.entry.insert(END, str(num))
                
    def absoluto(self):
        Beep.sonido(30)
        """ Return the absolute value of x."""
        if self.entry.get() == "":
                pass
        else:
            """Control de numeros enteros y reales"""
            if "." in self.entry.get():
                absoluto = math.fabs(float(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(absoluto))
            else:
                absoluto = math.fabs(int(self.entry.get()))
                self.limpiar_entry()
                self.entry.insert(END, str(absoluto))
        
                        
    def parentesis_abrir(self):
        Beep.sonido(30)
        self.entry.insert(END, "(")
        
    def parentesis_cerrar(self):
        Beep.sonido(30)
        self.entry.insert(END, ")")
        
    def X(self):
        Beep.sonido(30)
        self.entry.insert(END, "X")
        
    def Y(self):
        Beep.sonido(30)
        self.entry.insert(END, "Y")
                
                
    """-----------------------------------------------------------"""
    def acerca_de_calculadora(self):
        AcercaDe(self.master)
    
    def ayuda(self):
        pass
    
    def eventos_keypress(self):
        self.master.focus_force()
        self.master.bind("<Alt-KeyPress-1>", lambda e: self.calculadora_basico())
        self.master.bind("<Alt-KeyPress-2>", lambda e: self.calculadora_cientifica())
        self.master.bind("<KeyPress-F1>", lambda e: self.ayuda())
        self.master.bind("<Key>", self.keypressed)

    #evento para el teclado 
    def keypressed(self, event):
        list = ["7","8","9","/","4","5","6","*","1","2","3","-",".","0","=","+"]
        for i in list:
            if event.char == i:
                self.boton.config(state=ACTIVE)
            else:
                pass
            
    def cambiar_tema(self):
        select_color = colorchooser.askcolor(parent=self.master)
        
        if select_color != None:
            color = select_color[0]
            color_generado = "#%02x%02x%02x" % (color[0]/1.2, color[1]/1.2, color[2]/1.2)
            color_generado_2 = "#%02x%02x%02x" % (color[0]/1.5, color[1]/1.5, color[2]/1.5)
            
            self.master['bg'] =  select_color[1]
            self.etiqueta.config(bg=select_color[1])
            self.cabecera.config(bg=select_color[1])
            self.barra_borrar.config(bg=select_color[1])
            self.cientifica.config(bg=select_color[1])
            self.basico.config(bg=select_color[1])
            self.btn_sistema.config(bg=select_color[1])
            self.lb_separador.config(bg=select_color[1])
            self.btn_conversion.config(bg=select_color[1])
            self.btn_menu.config(bg=select_color[1])
            self.entry.config(bg=select_color[1])
            
            self.btn_limpiar_entry.config(bg=color_generado)
            self.btn_historial.config(bg=color_generado)
            
            self.btn_sen.config(bg=color_generado_2)
            self.btn_cos.config(bg=color_generado_2)
            self.btn_tan.config(bg=color_generado_2)
            self.btn_fact.config(bg=color_generado_2)
            self.btn_abs.config(bg=color_generado_2)
            self.btn_asen.config(bg=color_generado_2)
            self.btn_acos.config(bg=color_generado_2)
            self.btn_atan.config(bg=color_generado_2)
            self.btn_In.config(bg=color_generado_2)
            self.btn_log.config(bg=color_generado_2)
            self.btn_raiz_2.config(bg=color_generado_2)
            self.btn_pot_2.config(bg=color_generado_2)
            self.btn_pot_3.config(bg=color_generado_2)
            self.btn_pi.config(bg=color_generado_2)
            self.btn_e.config(bg=color_generado_2)
            self.btn_X.config(bg=color_generado)
            self.btn_Y.config(bg=color_generado)
            self.btn_mod.config(bg=color_generado_2)
            self.btn_parentesis_open.config(bg=color_generado)
            self.btn_parentesis_close.config(bg=color_generado)
            #Botones calculadora Basica
            self.btn_7.config(bg=color_generado)
            self.btn_8.config(bg=color_generado)
            self.btn_9.config(bg=color_generado)
            self.btn_division.config(bg=color_generado_2)
            self.btn_4.config(bg=color_generado)      
            self.btn_5.config(bg=color_generado)       
            self.btn_6.config(bg=color_generado)        
            self.btn_multiplicacion.config(bg=color_generado_2)
            self.btn_1.config(bg=color_generado)      
            self.btn_2.config(bg=color_generado)      
            self.btn_3.config(bg=color_generado)      
            self.btn_resta.config(bg=color_generado_2)
            self.btn_punto.config(bg=color_generado)      
            self.btn_0.config(bg=color_generado)       
            self.btn_igual.config(bg=color_generado_2)
            self.btn_suma.config(bg=color_generado_2)
        else:
            pass
        
        self.master.after(500, self.master.update())
        
    def tema_claro(self):
        self.master['bg'] = self.BG_BLACK_TEMACLARO
        self.etiqueta.config(bg=self.BG_BLACK_TEMACLARO)
        self.cabecera.config(bg=self.BG_BLACK_TEMACLARO)
        self.entry.config(insertbackground="GRAY",fg="BLACK")
        self.barra_borrar.config(bg=self.BG_BLACK_TEMACLARO)
        self.cientifica.config(bg=self.BG_BLACK_TEMACLARO)
        self.basico.config(bg=self.BG_BLACK_TEMACLARO)
        self.btn_sistema.config(bg=self.BG_BLACK_TEMACLARO)
        self.lb_separador.config(bg=self.BG_BLACK_TEMACLARO)
        self.btn_conversion.config(bg=self.BG_BLACK_TEMACLARO)
        self.btn_menu.config(bg=self.BG_BLACK_TEMACLARO)
        self.entry.config(bg=self.BG_BLACK_TEMACLARO)
        #Botones historial y clear
        self.btn_limpiar_entry.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_historial.config(**self.BUTTON_TEMACLARO)
        #Botones calculadora Cientifica
        self.btn_sen.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_cos.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_tan.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_fact.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_abs.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_asen.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_acos.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_atan.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_In.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_log.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_raiz_2.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_pot_2.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_pot_3.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_pi.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_e.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_X.config(**self.BUTTON_TEMACLARO)
        self.btn_Y.config(**self.BUTTON_TEMACLARO)
        self.btn_mod.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_parentesis_open.config(**self.BUTTON_TEMACLARO)
        self.btn_parentesis_close.config(**self.BUTTON_TEMACLARO)
        #Botones calculadora Basica
        self.btn_7.config(**self.BUTTON_TEMACLARO)
        self.btn_8.config(**self.BUTTON_TEMACLARO)
        self.btn_9.config(**self.BUTTON_TEMACLARO)
        self.btn_division.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_4.config(**self.BUTTON_TEMACLARO)      
        self.btn_5.config(**self.BUTTON_TEMACLARO)       
        self.btn_6.config(**self.BUTTON_TEMACLARO)        
        self.btn_multiplicacion.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_1.config(**self.BUTTON_TEMACLARO)      
        self.btn_2.config(**self.BUTTON_TEMACLARO)      
        self.btn_3.config(**self.BUTTON_TEMACLARO)      
        self.btn_resta.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        self.btn_punto.config(**self.BUTTON_TEMACLARO)      
        self.btn_0.config(**self.BUTTON_TEMACLARO)       
        self.btn_igual.config(bg="#039BE5", fg="WHITE",
                        activebackground="#1DE9B6", activeforeground="WHITE")
        self.btn_suma.config(**self.BUTTON_CIENTIFICA_TEMACLARO)
        
        
    def tema_oscuro(self):
        self.master['bg'] = self.BG_BLACK
        self.etiqueta.config(bg=self.BG_BLACK)
        self.cabecera.config(bg=self.BG_BLACK)
        self.entry.config(insertbackground=self.FG,fg=self.FG)
        self.barra_borrar.config(bg=self.BG_BLACK)
        self.cientifica.config(bg=self.BG_BLACK)
        self.basico.config(bg=self.BG_BLACK)
        self.btn_sistema.config(bg=self.BG_BLACK)
        self.lb_separador.config(bg=self.BG_BLACK)
        self.btn_conversion.config(bg=self.BG_BLACK)
        self.btn_menu.config(bg=self.BG_BLACK)
        self.entry.config(bg=self.BG_BLACK)
        self.btn_limpiar_entry.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_historial.config(bg=self.BG_BUTTON_2, fg=self.FG, activebackground="#006064")
        #Botones calculadora Cientifica
        self.btn_sen.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_cos.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_tan.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_fact.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_abs.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_asen.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_acos.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_atan.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_In.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_log.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_raiz_2.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_pot_2.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_pot_3.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_pi.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_e.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_X.config(**self.BUTTON_TEMAOSCURO)
        self.btn_Y.config(**self.BUTTON_TEMAOSCURO)
        self.btn_mod.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_parentesis_open.config(**self.BUTTON_TEMAOSCURO)
        self.btn_parentesis_close.config(**self.BUTTON_TEMAOSCURO)
        #Botones calculadora Basica
        self.btn_7.config(**self.BUTTON_TEMAOSCURO)
        self.btn_8.config(**self.BUTTON_TEMAOSCURO)
        self.btn_9.config(**self.BUTTON_TEMAOSCURO)
        self.btn_division.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_4.config(**self.BUTTON_TEMAOSCURO)      
        self.btn_5.config(**self.BUTTON_TEMAOSCURO)       
        self.btn_6.config(**self.BUTTON_TEMAOSCURO)        
        self.btn_multiplicacion.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_1.config(**self.BUTTON_TEMAOSCURO)      
        self.btn_2.config(**self.BUTTON_TEMAOSCURO)      
        self.btn_3.config(**self.BUTTON_TEMAOSCURO)      
        self.btn_resta.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_punto.config(**self.BUTTON_TEMAOSCURO)      
        self.btn_0.config(**self.BUTTON_TEMAOSCURO)       
        self.btn_igual.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        self.btn_suma.config(**self.BUTTON_CIENTIFICA_TEMAOSCURO)
        
    def tema_ios7(self):
        self.master['bg'] = self.BG_BLACK_TEMAIOS7
        self.etiqueta.config(bg=self.BG_BLACK_TEMAIOS7)
        self.cabecera.config(bg=self.BG_BLACK_TEMAIOS7)
        self.entry.config(insertbackground="WHITE",fg="WHITE")
        self.barra_borrar.config(bg=self.BG_BLACK_TEMAIOS7)
        self.cientifica.config(bg=self.BG_BLACK_TEMAIOS7)
        self.basico.config(bg=self.BG_BLACK_TEMAIOS7)
        self.btn_sistema.config(bg=self.BG_BLACK_TEMAIOS7)
        self.lb_separador.config(bg=self.BG_BLACK_TEMAIOS7)
        self.btn_conversion.config(bg=self.BG_BLACK_TEMAIOS7)
        self.btn_menu.config(bg=self.BG_BLACK_TEMAIOS7)
        self.entry.config(bg=self.BG_BLACK_TEMAIOS7)
        self.btn_limpiar_entry.config(**self.BUTTON_CIENTIFICA_TEMAIOS7)
        self.btn_historial.config(**self.BUTTON_TEMAIOS7)
        #Botones calculadora Cientifica
        self.btn_sen.config(**self.BUTTON_TEMAIOS7)
        self.btn_cos.config(**self.BUTTON_TEMAIOS7)
        self.btn_tan.config(**self.BUTTON_TEMAIOS7)
        self.btn_fact.config(**self.BUTTON_TEMAIOS7)
        self.btn_abs.config(**self.BUTTON_TEMAIOS7)
        self.btn_asen.config(**self.BUTTON_TEMAIOS7)
        self.btn_acos.config(**self.BUTTON_TEMAIOS7)
        self.btn_atan.config(**self.BUTTON_TEMAIOS7)
        self.btn_In.config(**self.BUTTON_TEMAIOS7)
        self.btn_log.config(**self.BUTTON_TEMAIOS7)
        self.btn_raiz_2.config(**self.BUTTON_TEMAIOS7)
        self.btn_pot_2.config(**self.BUTTON_TEMAIOS7)
        self.btn_pot_3.config(**self.BUTTON_TEMAIOS7)
        self.btn_pi.config(**self.BUTTON_TEMAIOS7)
        self.btn_e.config(**self.BUTTON_TEMAIOS7)
        self.btn_X.config(**self.BUTTON_CIENTIFICA_TEMAIOS7)
        self.btn_Y.config(**self.BUTTON_CIENTIFICA_TEMAIOS7)
        self.btn_mod.config(**self.BUTTON_TEMAIOS7)
        self.btn_parentesis_open.config(**self.BUTTON_CIENTIFICA_TEMAIOS7)
        self.btn_parentesis_close.config(**self.BUTTON_CIENTIFICA_TEMAIOS7)
        #Botones calculadora Basica
        self.btn_7.config(**self.BUTTON_TEMAIOS7)
        self.btn_8.config(**self.BUTTON_TEMAIOS7)
        self.btn_9.config(**self.BUTTON_TEMAIOS7)
        self.btn_division.config(**self.BUTTON_CIENTIFICA_TEMAIOS7)
        self.btn_4.config(**self.BUTTON_TEMAIOS7)      
        self.btn_5.config(**self.BUTTON_TEMAIOS7)       
        self.btn_6.config(**self.BUTTON_TEMAIOS7)        
        self.btn_multiplicacion.config(**self.BUTTON_CIENTIFICA_TEMAIOS7)
        self.btn_1.config(**self.BUTTON_TEMAIOS7)      
        self.btn_2.config(**self.BUTTON_TEMAIOS7)      
        self.btn_3.config(**self.BUTTON_TEMAIOS7)      
        self.btn_resta.config(**self.BUTTON_CIENTIFICA_TEMAIOS7)
        self.btn_punto.config(**self.BUTTON_TEMAIOS7)      
        self.btn_0.config(**self.BUTTON_TEMAIOS7)       
        self.btn_igual.config(**self.BUTTON_CIENTIFICA_TEMAIOS7)
        self.btn_suma.config(**self.BUTTON_CIENTIFICA_TEMAIOS7)
        

if __name__ == "__main__":
    Calculadora.main()