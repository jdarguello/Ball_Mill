import ipywidgets as widgets

def Requerimientos():
    Req = widgets.Accordion(children=[widgets.FloatText(value=20, disabled=False),
                                      widgets.FloatText(value=8),
                                      widgets.FloatText(value=8),
                                      widgets.FloatText(value=850),
                                      widgets.FloatText(value=250)])
    Req.set_title(0, 'Capacidad [kg/bache]')
    Req.set_title(1, 'Relación másica AD - MV')
    Req.set_title(2, 'Humedad MV [%]')
    Req.set_title(3, 'Granulometría Entrada [um]')
    Req.set_title(4, 'Granulometría Salida [um]')
    return Req

def Esp():
    Req = widgets.Accordion(children=[widgets.FloatSlider(value=1.5, min=1.5, max=3, step=0.1),
                                      widgets.FloatText(value=1500),
                                      widgets.FloatSlider(value=40, min=40, max=60, step=1),
                                      widgets.FloatSlider(value=10, min=10, max=30, step=1),
                                      widgets.FloatSlider(value=80, min=60, max=100, step=1),
                                      widgets.FloatText(value=100),
                                      widgets.FloatText(value=2700),
                                      widgets.FloatSlider(value=2, min=2, max=4, step=0.1)])
    Req.set_title(0, 'Relación Longitud - Diámetro')
    Req.set_title(1, 'Densidad del agente dispersante [kg/m3]')
    Req.set_title(2, 'Relación volumétrica de carga del molino [%]')
    Req.set_title(3, 'Volumen porcentual de las bolas (con respecto al total) [%]')
    Req.set_title(4, 'Relación de velocidad operacional respecto a la crítica [%]')
    Req.set_title(5, 'Densidad del material vegetal [kg/m3]')
    Req.set_title(6, 'Densidad de las bolas [kg/m3]')
    Req.set_title(7, 'Factor de seguridad')
    return Req

def Datos():
    Req = Requerimientos()
    E = Esp()
    tab = widgets.Tab()
    tab.children = [Req, E]
    tab.set_title(0, 'Requerimientos')
    tab.set_title(1, 'Especificaciones')
    return tab
