import settings;
import fontsize;

settings.outformat="pdf";
settings.render=16;
size(8cm, 0);

import graph;
//Tambor
real r = 1;
pair O = (0,0);    //Origen
draw(circle(O, r));

//Línea subdivisión
pair P1 = (-r,0);
pair P2 = (r,0);
draw(P1 -- P2, rgb(245/255, 92/255, 92/255));

//Relleno
void Relleno(real x, real r){
    real y = (r^2-x^2)^(1/2);
    draw((x,0) -- (x,-y), rgb(245/255, 92/255, 92/255));
}
int num_lineas = 25;
real x = -r;
real subd = 2*r/num_lineas;
for (int i=0; i<num_lineas-1; i=i+1) {
    x = x + subd;
    Relleno(x,r);
}

//Porcentaje de volumen
pair P3 = (0,-r);
pair P4 = (r+r/4,-r);
draw(P3 -- P4, rgb(138/255, 192/255, 239/255));
pair P5 = (r,0);
pair P6 = (r+r/4,0);
draw(P5 -- P6, rgb(138/255, 192/255, 239/255));
pair P7 = (r+r/8,0);
pair P8 = (r+r/8,-r);
pair P9 = (r+r/8, -r/2);
draw(P9 -- P8, arrow = Arrow, rgb(138/255, 192/255, 239/255));
draw(P9 -- P7, arrow = Arrow, rgb(138/255, 192/255, 239/255));

//Texto
label("Arena + Material Vegetal", (0,-r/3));
label("+ Bolas", (0,-r/2));
label("$\%$ del", (r+r/4, -r/4));
label("volumen del", (r+r/2, -2*r/5));
label("tambor", (r+r/2, -3*r/5 + r/20));