#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Jose Diaz"
__credits__ = ["person_1", "person_2", "person_3", "person_n"]
__copyright__ = "Copyright (C) 2015, Jose Diaz"
__license__ = "GPL"
__version__ = "1.1"
__revision__ = "8"
__date__ = "$23/02/2015 08:52:56 AM$"
__status__ = "Desarrollo"
__maintainer__ = "Jose Diaz"
__contact__ = "966403361"
__email__ = "jozz.18x@gmail.com"

from tkinter import *
from tkinter import ttk

class AcercaDe(Toplevel):
    """
    Acerca del software
    """
    def __init__(self, parent, title=None, _htest=False):
        Toplevel.__init__(self, parent)
        self.wm_withdraw()
        self.configure(borderwidth=0)
        self.geometry(
                "350x250+%d+%d" % (parent.winfo_rootx() + 20,
                parent.winfo_rooty() + (30 if not _htest else 150)))
        self.wm_title(title or 'Acerca de')
        
        self.create_widgets()
        
        self.overrideredirect(True)
        self.resizable(height=FALSE, width=FALSE) # don't allow resizing yet
        self.transient(parent)
        self.protocol("WM_DELETE_WINDOW", lambda: self.destroy())
        self.bind("<Escape>", lambda e: self.destroy())
        self.focus_set()
        # wait for window to be generated
        self.update()
        # set current width as the minimum width
        self.wm_minsize(self.winfo_width(), 1)
        # now allow resizing
        self.resizable(height=TRUE, width=TRUE)

        self.wm_deiconify()
        if not _htest:
            self.grab_set()
            self.wait_window()
        
        
    def create_widgets(self):
        """Create the dialog's widgets."""
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)

        borde = Frame(self, bg="WHITE", highlightbackground="GRAY", highlightthickness=1)
        borde.pack(fill=BOTH, expand=True)
        
        fr_inferior = Frame(borde)
        fr_inferior.pack(side=BOTTOM, fill=X)
        fr_both = Frame(borde, bg=borde['bg'])
        fr_both.pack(side=LEFT, fill=BOTH, expand=1)
        
        Label(fr_both, text="Calculadora  version 1.0", font=("Arial", 12), justify="center", 
                        height=2, bg=fr_both['bg']).place(in_=fr_both, x=90, y=50)
        Label(fr_both, text="Copyright (C) 2015 Jose Diaz", font=("Arial", 12), justify="center", 
                        height=2, bg=fr_both['bg']).place(in_=fr_both, x=65, y=90)
        
        btn_ok = ttk.Button(fr_inferior, text="Aceptar", command=lambda: self.destroy())
        btn_ok.pack(side=RIGHT, padx=10, pady=5)