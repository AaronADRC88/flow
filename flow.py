__author__ = 'aferreiradominguez'
from gi.repository import Gtk, Gdk


class flow_box(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="flow")
        self.set_border_width(10)
        self.set_default_size(300, 250)

        cabezera = Gtk.HeaderBar(title="head <:-)")
        cabezera.set_subtitle("flowBox")
        cabezera.props_show_close_button = True
        self.set_titlebar(cabezera)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        caixaflow = Gtk.FlowBox()
        caixaflow.set_valign(Gtk.Align.START)
        caixaflow.set_max_children_per_line(30)
        caixaflow.set_selection_mode(Gtk.SelectionMode.NONE)

        self.crea_flowbox(caixaflow)

        scrolled.add(caixaflow)

        self.add(scrolled)
        self.show_all()

    def crea_flowbox(self, caixabox):
        cores = [
            'AliceBlue',
            'AntiqueWhite',
            'AntiqueWhite1',
            'AntiqueWhite2',
            'AntiqueWhite3',
            'AntiqueWhite4',
            'aqua',
            'aquamarine',
            'aquamarine1',
            'aquamarine2',
            'aquamarine3',
            'aquamarine4',
            'azure',
            'beige',
            'bisque',
            'black'
        ]
        for cor in cores:
            boton = self.asigna_cor(cor)
            caixabox.add(boton)

    def asigna_cor(self, cadea_cor):
        cor = Gdk.color_parse(cadea_cor)

        rgba = Gdk.RGBA.from_color(cor)
        boton = Gtk.Button()

        area = Gtk.DrawingArea()
        area.set_size_request(24, 24)
        area.override_background_color(0, rgba)

        boton.add(area)

        return boton


ventana = flow_box()
ventana.connect("delete-event", Gtk.main_quit)
ventana.show_all()
Gtk.main()
