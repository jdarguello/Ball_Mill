import ipywidgets as widgets

def Requerimientos():
    Req = widgets.Accordion(children=[widgets.FloatText(value=200, disabled=False),
                                      widgets.FloatText(value=850),
                                      widgets.FloatText(value=250)])
    Req.set_title(0, 'Capacity [kg/batch]')
    Req.set_title(1, 'Input particle size [um]')
    Req.set_title(2, 'Target particle size [um]')
    return Req

def Esp():
    Req = widgets.Accordion(children=[widgets.FloatSlider(value=1.5, min=1.5, max=3, step=0.1),
                                      widgets.FloatText(value=2700),
                                      widgets.FloatText(value=1200),
                                      widgets.FloatSlider(value=40, min=40, max=60, step=1),
                                      widgets.FloatSlider(value=10, min=10, max=30, step=1),
                                      widgets.FloatSlider(value=80, min=60, max=100, step=1),
                                      widgets.FloatSlider(value=2, min=2, max=4, step=0.1)])
    Req.set_title(0, 'Length - diameter relation')
    Req.set_title(1, 'Density of balls [kg/m3]')
    Req.set_title(2, 'Density of the material [kg/m3]')
    Req.set_title(3, 'Occupied volume by the material [%]')
    Req.set_title(4, 'Occupied volume by the balls [%]')
    Req.set_title(5, 'Rotational speed criteria [%]')
    Req.set_title(6, 'Safety factor')
    return Req

def Datos():
    Req = Requerimientos()
    E = Esp()
    tab = widgets.Tab()
    tab.children = [Req, E]
    tab.set_title(0, 'Requirements')
    tab.set_title(1, 'Specifications')
    return tab
