input latexmp;
setupLaTeXMP(packages="amssymb");
outputformat := "png";
outputtemplate := "%j-%c.%o";
%-----ESQUEMA MOLINO DE BOLAS PLANETARIO------
beginfig(1);
%Datos
DM = 10cm;		%Diámetro mayor
Dm = 5cm;		%Diámetro menor
Db = 0.5cm;		%Diámetro de las bolas
Da = 0.15cm;		%Diámetro del material a moler
path mm;
mm = fullcircle scaled Db;


%Círculo mayor
pair M[];
M0 = (0, -DM/2); M1 = (0, DM/2); M2 = (-DM/2,0); M3 = (DM/2, 0);
draw M0..M1 ..cycle withcolor (253,157,32)/255;

%Sistema coordenado en círculo mayor
pair E[];
E0 = (xpart M0, ypart M0 - 1cm); E1 = (xpart M1, ypart M1 + 1cm); 
E2 = (xpart M2 - 1cm, ypart M2); E3 = (xpart M3 + 1cm, ypart M3); 
draw E0 -- E1 dashed evenly withcolor (80,80,80)/255;
draw E2 -- E3 dashed evenly withcolor (80,80,80)/255;

%Movimiento rotacional - Mayor
drawarrow (DM/2 + 0.5cm, 0) .. (DM/2 - 1cm, -(DM/2 - 1cm)) .. (xpart M1, -(ypart M1 + 0.5cm)) dashed evenly withcolor (253,113,32)/255;

%Bola (DM = 10cm)
pair b[];
b0 = (0, -Db/2); b1 = (0, Db/2);
y = DM/4 - 0.25cm;
path a;
a = mm shifted (xpart b0 - (DM/2 - 3*Db/2), ypart b0 + y + Db/2);
fill a withcolor .4white;
draw (xpart b0 - (DM/2 - 3*Db/2), ypart b0 + y)..(xpart b1 - (DM/2 - 3*Db/2), ypart b1 + y) ..cycle;

%--Info--
draw (xpart b0 - (DM/2 - 3*Db/2), ypart b0 + y + Db/2) -- (0,0);
draw((0,0) -- (0,DM/2));
drawarrow((xpart b0 - (DM/2 - 3*Db/2), ypart b0 + y + Db/2) -- (xpart b0 - (DM/2 - 3*Db/2), ypart b0 + y + Db/2 - DM/8));
draw ((0, DM/20) .. (-DM/15, DM/20 + 0.05cm) .. (-DM/12,DM/20 - 0.1cm));
drawarrow((- (DM/2 - 3*Db/2), ypart b0 + y + Db/2) -- (-DM/2, ypart b0 + y + Db/2 + 0.5cm));

%Textos
%t = (-DM/15, DM/20 + 0.05cm);
label(textext("$x_2$"), (-DM/15, DM/20 + 0.05cm));
%label(btex $\mathcal{X}_{\eta}$ etex,(-15,55)); 

endfig;
end;
