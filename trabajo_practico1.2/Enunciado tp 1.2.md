# ABSTRACT
El siguiente documento tiene por objetivo detallar el trabajo de clase que debe realizarse para
profundizar el estudio del comportamiento de la ruleta pero desde el punto de vista del apostador y
sus estrategias.
Keywords Simulación · Trabajo práctico · Ruleta · apuestas · estrategias

# 1 Introducción
Apostar en algún juego lleva a controversias de todos los puntos de vista, pero desde el nuestro como ingenieros
debemos tener una visión objetiva de cualquier problema, por muy ajeno que nos resulte. Este trabajo, tiene como fin
el empleo de nuestra primera simulación, con el objetivo desmitificar estadísticamente la verdadera probabilidad de
obtener ganancias con un medio ideal, como es nuestra ruleta simulada.
Las estrategias que se pueden proponer son varias, pero comenzaremos con una de las más sencillas y fáciles de
implementar, dejando al alumno la posibilidad de construir o imitar otras.

# 2 Descripción del trabajo
El trabajo consiste en construir una programa en lenguaje Python 3.x que simule el funcionamiento del plato de una
ruleta y al mismo tiempo lleve adelante diversas apuestas, monitorizando el flujo de caja y el período de ocurrencia de
que la apuesta produzca o no beneficios. Para esto se debe tener en cuenta lo siguientes temas a investigar:
• Beneficios de las apuestas según la selección (color, fila, etc).
• Estrategias de apuestas en la ruleta.
• Gráficas de los resultados mediante el paquete Matplotlib (u otro similar).
Se pide que se detalle la estrategias empleadas y las fuentes donde las obtuvieron (si son de elaboración son propia).
Se propone una primera estrategia llamada "la martingala", pero el grupo de investigación debe de emplear como
mínimo 2 distintas. Para cada estrategia se debe tener en cuenta dos supuestos mutuamente excluyentes: capital
acotado (realidad) y capital infinito (ideal).

## 2.1 Exposición de los resultados y análisis de los mismos
Los resultados se deben graficar y luego concluir su comportamiento simulado y esperado. A modo de ejemplo se dejan
los siguientes bocetos de gráficas, siendo estas las que como mínimo deben de estar en el estudio:
Figura 1: Conjunto de gráficas mínimas solicitadas.
Luego de finalizar lo anterior, se deben de realizar varias corridas del experimento (entre 5 y 10) y generar nuevas
gráficas donde se muestren en forma simultánea sus resultados. En total son como mínimo 4 gráficas en todo el trabajo.

## 2.2 Presentación del trabajo y entrega
Este y los siguientes TPs se presenta obligatoriamente en formato LATEX. Una manera cómoda de trabajar es mediante
un IDE el cual puede ser online o local. La ventaja de trabajar online es la posibilidad de que el resto del grupo aporte y
corrija directamente y simultáneamente.
Una de las plataformas online más conocidas es Overleaf. Por el otro lado, en forma local tenemos, para los que trabajan
con Linux distribución Ubuntu el muy conocido Texmaker. En Windows debe instalarse primero el compilador Miktex,
y posteriormente puede instalarse Texmaker o TexStudio. VSCode también tiene utilidades para escribir en Latex.
### El contenido mínimo a entregar es:
• Código completo en Python 3.x.
• Informe en formato Latex con introducción, gráficas, fórmulas empleadas, conclusiones, referencias (hay un
apartado para esto) y cualquier otra información que quieran agregar.
La fecha de entrega es el día 08/04/2020.

# 3 Recursos online obligatorios
Volveremos a usar el template LATEXde la Cornell University por su sencillez:
https://es.overleaf.com/latex/templates/style-and-template-for-preprints-arxiv-bio-arxiv/
pkzcrhzcdxmc
https://es.wikipedia.org/wiki/Martingala
# 4 Recursos online sugeridos
Algunas páginas que me han ayudado a alumnos de años anteriores en Python:
https://python-para-impacientes.blogspot.com/2014/08/graficos-en-ipython.html
https://relopezbriega.github.io/blog/2015/06/27/probabilidad-y-estadistica-con-python/