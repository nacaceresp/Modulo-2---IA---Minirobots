# Módulo 2. IA & Minirobots
En el presente texto se presenta la solución de diferentes inquietudes teóricas planteadas durante el módulo 2 de la clase Inteligencia Artificial y Minirobots. Adicionalmente, en este repositorio se presentan diversos programas que solucionan multiples ejercicios que ponen a prueba los conocimientos desarrollados durante cada uno de los capitulos planteados por la asignatura.  

## Capitulo 2. 

1.1 Observe sus comportamientos en la casa, en la universidad y en el medio de transporte que utiliza. Encuentre, para cada uno de estos escenarios sus reglas básicas.

En el caso de la casa, mi vecindad son mis padres y mi novia y mi comportamiento en ella depende de diferentes reglas implícitas entre las cuales están mantener la casa limpia y ordenada, no fumar dentro de la casa, no hacer ruido excesivo que pueda molestar a los vecinos, respetar la privacidad y las pertenencias de los demás, apagar las luces y los electrodomésticos cuando no se estén utilizando, cerrar las puertas y ventanas cuando salga de la casa, no llevar personas desconocidas a la casa sin el consentimiento de mis padres, ser amable y respetuoso con los demás, etc..

En lo que respecta a la universidad es necesario cumplir con diferentes horarios, dependiendo de si se es de género masculino o femenino se debe ingresar al baño adecuado, se deben respetar los derechos y la propiedad de los demás, no se debe plagiar, copiar o falsificar trabajos académicos o documentos oficiales, no se debe hacer trampa en los exámenes o en cualquier otra evaluación, se debe abstener de cualquier forma de discriminación o acoso hacia otros estudiantes o miembros del personal, se debe mantener un comportamiento respetuoso y profesional en todo momento, no se deben llevar armas o cualquier objeto peligroso a las instalaciones universitarias y en general se deben respetar las normas y regulaciones de las instalaciones universitarias y seguir las instrucciones del personal.

Finalmente, mi medio de transporte es la motocicleta, cuando me movilizo en ella debo cumplir una serie de normas explícitas que se contienen en un libro llamado código de tránsito, entre estas se encuentran activar las luces direccionales siempre antes de cambiar de carril o de hacer un giro, para indicar a los demás actores viales mi dirección, respetar señales de pare, y en general identificar las diferentes señales bien sea preventivas, restrictivas e Informativas.

2. En la librería de modelos de NetLogo, encuentre una aplicación de AC, describa el modelo, córralo y haga un análisis del resultado.

### CONTEXTO
El modelo escogido fue Brian ́s Brain, el cual es un programa de dos dimensiones con reglas para la supervivencia de las células, maneja dos tipos de células, las blancas y las rojas.

Este programa es un ejemplo de un autómata celular bidimensional que utiliza tres estados celulares: "firing" (disparo), "refractory" (refractario) y "dead" (muerto). El programa se llama "Brian's Brain" porque fue inventado por el científico Brian Silverman en 1991.

En este autómata celular, las celdas que están en estado "firing" se convierten en "refractory" en el siguiente paso de tiempo. Las celdas "refractory" siempre mueren (pasan a estado "dead") en el siguiente paso de tiempo. Una nueva celda "firing" nace en cualquier celda "dead" que tenga exactamente dos vecinos "firing".

El programa tiene controles deslizantes para ajustar la densidad inicial de celdas "firing" y permite al usuario dibujar o borrar celdas "firing" y "refractory" con el mouse.

Este autómata celular produce muchos patrones estables que se mueven constantemente a través de la grilla, conocidos como "gliders". Se puede experimentar para ver si hay patrones estables que no se mueven o "glider guns" (objetos que emiten un flujo constante de gliders). Además, hay muchas otras variaciones interesantes de los autómatas celulares bidimensionales con tres estados, y se puede experimentar con diferentes reglas para crear modelos nuevos y diferentes.

Un vídeo de un ejemplo:
https://drive.google.com/file/d/1y-4FN5-t4rVfLs2UZHjlpwveb26nz-1j/view?usp=sharing

### ANÁLISIS COMPLETO
   
El modelo implementado en el código es un autómata celular bidimensional conocido como "Brian's Brain" que utiliza tres estados celulares: blanco, rojo y negro. El modelo es interesante porque tiene muchas configuraciones que se mueven de manera constante en la grilla, a diferencia del modelo "Life" que tiene relativamente pocas de estas configuraciones.

En este modelo, las células blancas siempre se convierten en células rojas en el siguiente paso de tiempo, y las células rojas siempre mueren (se vuelven negras) en el siguiente paso de tiempo. Una nueva célula blanca nace en cualquier célula negra que tenga exactamente dos vecinos blancos de sus ocho células adyacentes. El modelo se ejecuta en una grilla cuadrada o rectangular, y la densidad inicial de células blancas se puede ajustar mediante un control deslizante.

El usuario puede interactuar con el modelo a través de botones para ejecutar el modelo una vez o de forma continua, y también puede dibujar y borrar células blancas y rojas en la grilla con el mouse. El modelo puede ser extendido para experimentar con variaciones en las reglas y en los estados celulares, y se pueden explorar otros autómatas celulares bidimensionales de tres estados en la biblioteca de modelos NetLogo.

En resumen, el modelo implementado en el código es una simulación de un autómata celular bidimensional conocido como "Brian's Brain" que utiliza tres estados celulares y es interesante porque tiene muchas configuraciones que se mueven de manera constante en la grilla. El modelo se puede personalizar y experimentar con diferentes reglas y estados celulares.

### CÓDIGO

El modelo utiliza el entorno de NetLogo y está diseñado para permitir la interacción del usuario a través del ratón, permitiéndole dibujar y borrar células en la vista.

El modelo comienza con dos procedimientos, “setup-blank” y “setup-random”. “setup-blank” simplemente limpia la cuadrícula, lo que significa que todas las células se establecen en el estado muerto y los contadores de tiempo se restablecen a cero. “setup-random” establece una densidad inicial de células que están en estado de fuego. Se utiliza una distribución aleatoria para determinar qué células se encienden inicialmente.

El modelo tiene tres procedimientos de parche, “cell-birth”, “cell-aging” y “cell-death”. “cell-birth” establece una célula en el estado de fuego/disparo (firing), “cell-aging” establece una célula en el estado refractario y “cell-death” establece una célula en el estado muerto.

El procedimiento “go” ejecuta el modelo. Primero, cada parche cuenta cuántos vecinos están en estado de fuego/disparo (firing) y almacena esa cantidad en una variable llamada “firing-neighbors”. Luego, se comprueba el estado actual de la célula y se decide si debe cambiar de estado en función de las reglas del modelo. Si una célula está en estado de fuego/disparo (firing), se llama al procedimiento “cell-aging”, lo que significa que la célula cambia a refractario. Si una célula está en estado refractario, se llama al procedimiento “cell-death”, lo que significa que la célula cambia a muerto. Si una célula está en estado muerto y exactamente dos de sus vecinos están en estado de fuego/disparo (firing), se llama al procedimiento “cell-birth”, lo que significa que la célula cambia a fuego/disparo (firing).

Finalmente, el procedimiento “draw-cells” permite al usuario interactuar con el modelo dibujando o borrando células en la vista. Si el usuario hace clic en un parche y mantiene presionado el botón del ratón, se establece una variable llamada “erasing?” que indica si se está borrando o agregando células. Luego, se pregunta al parche correspondiente si está siendo borrado o agregado. Si se está borrando, la célula cambia al estado muerto. Si se está agregando, la célula cambia al estado de fuego/disparo (firing) o refractario según el color seleccionado. El modelo se actualiza después de cada cambio.

### Citación:

For the model itself:

Wilensky, U. (2002). NetLogo Brian’s Brain model. http://ccl.northwestern.edu/netlogo/models/Brian’sBrain. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.
Please cite the NetLogo software as:
Wilensky, U. (1999). NetLogo. http://ccl.northwestern.edu/netlogo/. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

## Capitulo 4

2.¿Puede utilizarse la PG para hacer Ingeniería Inversa? ¿Justifique, con todo el detalle, su
respuesta?

Inicialmente se tiene que la programación genética es una técnica de optimización que utiliza la evolución artificial para encontrar soluciones a problemas complejos. Se basa en la idea de que, como en la evolución natural, las mejores soluciones a un problema persistirán y mejorarán con el tiempo. 

Por otro lado, la ingeniería inversa es el proceso de desarmar un sistema o producto existente para comprender su funcionamiento interno, a menudo con el objetivo de recrear o mejorar el sistema.  

Entonces, la relación entre la programación genética y la ingeniería inversa, es que, la programación genética se puede utilizar para realizar ingeniería inversa mediante la creación de modelos informáticos que coincidan con el comportamiento observado. Por ejemplo, si tiene un producto o sistema con un comportamiento desconocido, puede recopilar datos de entrada y salida y utilizar la programación genética para crear modelos que coincidan con esos datos.  

Una vez que tenga un modelo computacional que se ajuste a los datos de entrada y salida observados, puede utilizar el modelo para obtener información sobre cómo funciona el sistema subyacente. Este enfoque puede ser especialmente útil para sistemas muy complejos o donde el acceso a su funcionamiento interno es limitado. 
 
Sin embargo, es importante tener en cuenta que la programación genética no es tan eficiente para la ingeniería inversa. A menudo se requiere  un conocimiento previo del sistema y  experiencia en la interpretación de patrones generados por  programación genética para  obtener resultados útiles. Además, la calidad de los modelos generados por  programación genética puede depender de la calidad y cantidad de  datos disponibles.

Un uso más eficiente de la programación genética sería,  para la optimización de diseños en ingeniería. En este caso, se utilizará la programación genética para generar y evolucionar soluciones de diseño que cumplan con ciertos criterios de optimización, como la maximización de la resistencia estructural o la minimización del peso del objeto. De esta manera, la programación genética puede ser una herramienta útil para los ingenieros que buscan optimizar el rendimiento de sus diseños, ya que permite explorar una amplia gama de soluciones posibles de manera eficiente y automatizada. 

Existen otro tipo de algoritmos más eficientes para el desarrollo de la ingeniería inversa, que implica la obtención de información sobre un objeto o sistema existente, a partir de datos incompletos o limitados. Se pueden utilizar diversos algoritmos de IA, como redes neuronales, algoritmos genéticos, lógica difusa, entre otros. Cada uno de estos algoritmos tiene fortalezas y debilidades en términos de su capacidad para abordar diferentes tipos de problemas.  

### Redes neuronales:

Estos algoritmos están inspirados en el funcionamiento del cerebro humano y se utilizan comúnmente para problemas de clasificación, reconocimiento de patrones y predicción. Las redes neuronales son capaces de aprender patrones y relaciones a partir de grandes conjuntos de datos, lo que las hace adecuadas para problemas de ingeniería inversa que implican la identificación de patrones y relaciones en datos incompletos o ruidosos.

### Algoritmos genéticos:

Estos algoritmos están inspirados en la evolución biológica y se utilizan para problemas de optimización y búsqueda. Los algoritmos genéticos funcionan a través de la selección natural, reproducción y mutación de soluciones candidatas, generando nuevas soluciones que se ajusten a las restricciones y objetivos definidos. Los algoritmos genéticos pueden ser útiles en la ingeniería inversa para optimizar el diseño de sistemas y estructuras complejas.

### Lógica difusa:

Esta técnica se utiliza para el modelado de sistemas complejos y la toma de decisiones en situaciones inciertas o ambiguas. La lógica difusa se basa en el concepto de conjuntos difusos, que permiten la representación de la incertidumbre y la ambigüedad en los datos. La lógica difusa puede ser útil en la ingeniería inversa para la identificación de relaciones y patrones en datos con incertidumbre y para la toma de decisiones en situaciones complejas.

Los algoritmos de IA son eficientes para la ingeniería inversa porque permiten la identificación de patrones y relaciones en datos complejos e incompletos, la optimización de soluciones y la toma de decisiones en situaciones inciertas o ambiguas. La elección del algoritmo más adecuado dependerá de las características específicas del problema a resolver y de los datos disponibles.

En resumen, la programación genética se puede utilizar para realizar ingeniería inversa mediante la generación de modelos informáticos que coincidan con el comportamiento observado. Este enfoque puede ser especialmente útil para sistemas muy complejos o donde el acceso a su funcionamiento interno es limitado. Sin embargo, se requiere  un conocimiento previo del sistema y  experiencia en la interpretación de patrones generados por  programación genética para obtener resultados útiles.

Tomado de: 

"Artificial Intelligence Techniques for Reverse Engineering" de Ming-Ying Leung y Tao Li, publicado en Journal of Computing and Information Science in Engineering en 2009.

"Reverse Engineering Techniques in Machine Learning" de Shaohua Kevin Zhou, publicado en International Journal of Advanced Computer Science and Applications en 2015.

"Genetic Programming: An Introduction" de Wolfgang Banzhaf et al.
