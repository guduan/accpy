# -*- coding: utf-8 -*-
''' accpy.gui.menu
author:     felix.kramer(at)physik.hu-berlin.de
'''
from __future__ import division
try:
    import Tkinter as Tk
    import ttk
    from tkMessageBox import showinfo
except:
    import tkinter as Tk
    import tkinter.ttk as ttk
    from tkinter.messagebox import showinfo
from .simulate import (gui_twisstrack, gui_parttrack, gui_ramp,
                       gui_quadscansim)
from .measure import tunes, chromaticity, quadscanmeas, achroscan
from .optimize import emittex, twissmatch
from ..visualize.figures import plotstandards


def mainwindow(root, version):
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry('{}x{}'.format(w, h))
    root.wm_title("accpy gui {}".format(version))
    bar, frame = menubar(root, version)
    root.config(menu=bar)
    return


def menubar(root, version):
    def clear(frame):
        # destroy all widgets in fram/tab
        for widget in frame.winfo_children():
            widget.destroy()

    bar = Tk.Menu(root)

    # FILE MENU
    FM = Tk.Menu(bar, tearoff=0)
    FML = ['New lattice',
           'Quit']

    def File_newlat():
        showinfo('Ooops!', 'Sorry, but this feature is not ready yet...')
    FM.add_command(label=FML[0], command=File_newlat)

    def File_quit():
        root.quit()     # stops mainloop
        root.destroy()
    FM.add_command(label=FML[1], command=File_quit)
    bar.add_cascade(label="File", menu=FM)

    # SIMULATION MENU
    SM = Tk.Menu(bar, tearoff=0)
    SML = ['Betamatrix and dispersion tracking',
           'Particle tracking',
           'Ramp',
           'Quadrupole scan']

    def Simu_twisstrack():
        root.wm_title("accpy gui - simulations: {}".format(SML[0]))
        clear(frame)
        gui_twisstrack(frame, w, h)
    SM.add_command(label=SML[0], command=Simu_twisstrack)

    def Simu_parttrack():
        root.wm_title("accpy gui - simulations: {}".format(SML[1]))
        clear(frame)
        gui_parttrack(frame, w, h)
    SM.add_command(label=SML[1], command=Simu_parttrack)

    def Simu_hframp():
        root.wm_title("accpy gui - simulations: {}".format(SML[2]))
        clear(frame)
        gui_ramp(frame, w, h)
    SM.add_command(label=SML[2], command=Simu_hframp)

    def Simu_quadscan():
        root.wm_title("accpy gui - simulations: {}".format(SML[2]))
        clear(frame)
        gui_quadscansim(frame, w, h)
    SM.add_command(label=SML[3], command=Simu_quadscan)
    bar.add_cascade(label="Simulation", menu=SM)

    # MEASUREMENT MENU
    MM = Tk.Menu(bar, tearoff=0)
    MML = ['Tunes',
           'Chromaticity',
           'Quadrupole scan',
           'Achromat scan']

    def Meas_tunes():
        root.wm_title("accpy gui - measurements: {}".format(MML[0]))
        clear(frame)
        tunes(frame, w, h)
    MM.add_command(label=MML[0], command=Meas_tunes)

    def Meas_chrom():
        root.wm_title("accpy gui - measurements: {}".format(MML[1]))
        clear(frame)
        chromaticity(frame, w, h)
    MM.add_command(label=MML[1], command=Meas_chrom)

    def Meas_QuadScan():
        root.wm_title("accpy gui - measurements: {}".format(MML[2]))
        clear(frame)
        quadscanmeas(frame, w, h)
    MM.add_command(label=MML[2], command=Meas_QuadScan)

    def Meas_AchroScan():
        root.wm_title("accpy gui - measurements: {}".format(MML[3]))
        clear(frame)
        achroscan(frame, w, h)
    MM.add_command(label=MML[3], command=Meas_AchroScan)
    bar.add_cascade(label='Measurement', menu=MM)

    # Entries for Optimization menu
    OM = Tk.Menu(bar, tearoff=0)
    OML = ['Find Transverse emittance exchange section',
           'Twiss matching']

    def Opti_emittex():
        root.wm_title("accpy gui - optimizations: {}".format(OML[0]))
        clear(frame)
        emittex(frame, w, h)
    OM.add_command(label=OML[0], command=Opti_emittex)

    def Opti_twissmatch():
        root.wm_title("accpy gui - measurements: {}".format(OML[1]))
        clear(frame)
        twissmatch(frame, w, h)
    OM.add_command(label=OML[1], command=Opti_twissmatch)
    bar.add_cascade(label="Optimization", menu=OM)

    # Entries for Help menu
    HM = Tk.Menu(bar, tearoff=0)
    HML = ['Documentation',
           'About accpy...']

    def Help_docs():
        showinfo('Ooops!', 'Sorry, but this feature is not ready yet...')
    HM.add_command(label=HML[0], command=Help_docs)

    def Help_about():
        r = Tk.Tk()
        r.wm_title('About accpy')
        r.option_add('*font', 'Helvetica -16 bold')
        txt1 = Tk.Label(r, text='accpy version {}'.format(version))
        r.option_add('*font', 'Helvetica -14')
        txt2 = Tk.Label(r, text='Created by\nfelix kramer\n(felix.kramer@physik.hu-berlin.de)')
        txt1.pack()
        txt2.pack()
    HM.add_command(label=HML[1], command=Help_about)
    bar.add_cascade(label="Help", menu=HM)

    frame = ttk.Frame(root)
    frame.pack(expand=True)
    w, h = frame.winfo_screenwidth(), frame.winfo_screenheight()
    plotstandards('pcdisplay', [1, 1], w=w, h=h)
    return bar, frame
