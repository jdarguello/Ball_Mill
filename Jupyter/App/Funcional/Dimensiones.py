import math
class Volumenes():
    def __init__(self, data):
        #Volúmenes en m3
        V_Gm = data['Req']['Capacity [kg/batch]']/data['Esp']['Density of the material [kg/m3]']
        V_Tb, mult = self.Bolas(V_Gm, data['Esp']['Occupied volume by the material [%]'],
                          data['Esp']['Occupied volume by the balls [%]'])
        V = mult*(V_Gm+V_Tb)
        
        #Mostrar resultados...
        self.resul = {
            'V_Gm': V_Gm,
            'V_Tb': V_Tb,
            'V': V
        }
        self.Vol = {
            'Type': ['$V_{Gm}$', '$V_{Tb}$', '$V_{T}$'],
            'Value $[L]$': [round(V_Gm*1000,2), round(V_Tb*1000,2), round(V*1000,2)]
        }
    
    def __call__(self):
        return self.resul, self.Vol
    
    def Bolas(self, MV, pcarga, pbolas):
        """
            AD - Volumen ocupado por el agente dispersante
            MV - Volumen ocupado por el material vegetal
            pcarga - Porcentaje de carga del molino
            pbolas - Volumen porcentual de las bolas (con respecto al total)
            V = mult*(AD+MV+Tb)
        """
        pcarga = pcarga/100
        pbolas = pbolas/100
        mult = 1/pcarga
        return ((mult*pbolas)/(1-mult*pbolas))*(MV), mult
    
    def AD(self, Rel, Cap, rho):
        m = Cap*Rel    #kg
        return m/rho
    
def dim(V, rel):
    mult = math.pi*rel/4
    D = ((1/mult)*V)**(1/3)
    L = rel*D
    return D,L