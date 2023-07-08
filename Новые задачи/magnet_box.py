# Тимми скучно на уроках физики, поэтому он смастерил себе магнитную коробку с металлическими кубиками. 
# Магнит установлен справа и слева от коробки. В коробке есть несколько столбиков из кубиков. i-й столбец содержит a_i кубиков. 
# При включении левого магнита, все кубики перемещаются к левой стенке коробки.
# При включении  правого магнита, все кубики перемещаются к правой стенке коробки.

# Вот пример того, как может выглядеть коробка с кубиками до и после переключения магнита.

#   +---+                                       +---+
#   |   |                                       |   |
#   +---+                                       +---+
#   +---++---+     +---+              +---++---++---+
#   |   ||   |     |   |   -->        |   ||   ||   |
#   +---++---+     +---+              +---++---++---+
#   +---++---++---++---+         +---++---++---++---+
#   |   ||   ||   ||   |         |   ||   ||   ||   |
#   +---++---++---++---+         +---++---++---++---+
#   [ 3,   2    2,   1 ]         [ 1,   2    2,   3 ]

# Учитывая начальную конфигурацию кубиков в коробке, выясните, сколько кубиков находится в каждом из n столбцов после того, как Тимми включит левой или правый магнит.
# При необходимости, нарисуйте коробку с кубиками на листочке!

#   'R', [3, 2, 1, 2])     ->  [1, 2, 2, 3]
#   'L', [1, 4, 5, 3, 5])  ->  [5, 5, 4, 3, 1]
