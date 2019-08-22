Короче, вот файл. Он бинарный.
ВСЕ ЧИСЛА НИЖЕ УКАЗАНЫ В ШЕСТНАДЦАТЕРИЧНОЙ СИСТЕМЕ СЧИСЛЕНИЯ.

Каждый редактируемый блок составляет 188 байт, то бишь мне нужно оперировать отдельно в КАЖДОМ блоке. 
Отступ до первого предмета от начала файла - 40 байт, название предмета это первые 10 байт в его блоке. 
21-24 байты это его тег, дальше идет информация, я распишу значение каждой переменной,
 отступ до нее и в каком виде мне нужно ее редактировать в конце этого текста.

А теперь к нужным кнопкам

1) Кнопка выбора предмета. Она будет автоматически читать названия предметов и задавать начальную точку отсчета
 для всех остальных данных. Как это будет работать: базовый отступ - 40 байт, далее идет первый блок, 
 программа читает его название в 10 байт, потом пропускает еще 188 байт, читает название следующего блока и так далее, 
 пока файл не закончится. В результате создается список, из которого можно будет выбрать одно из названий блоков,
  при выборе будет задаваться начальная точка отсчета для всех остальных редактируемых полей программы.

2) Кнопки редактирования данных: нужно какое-то число полей (точное число ниже), 
в которые можно будет писать число в float формате, а после нажатия enter это число будет записано в файл 
или буфер обмена, во втором случае нужна будет кнопка сохранения изменений в файле.
 В идеале еще нужно чтобы программа читала изначальное значение, но это не обязательно.

3) Кнопки выбора варианта: 21 переключатель. Вкл - в нужное место записывается единица, выкл - записывается ноль. 
В идеале тоже нужно чтение изначального положения, но это тоже не обязательно.

Как подписать блоки для редактирования и какой для них нужно будет установить пропуск от начальной точки отсчета,
 задаваемой выбором названия предмета, сейчас напишу.
И да, это техническое описание, если нужно упростить, то я могу примерно показать через демку что мне нужно.
Сейчас распишу как нужно будет подписать блоки и какой до них нужен пропуск.
ВСЕ ЗНАЧЕНИЯ УКАЗАНЫ В ШЕСТНАДЦАТЕРИЧНОЙ СИСТЕМЕ СЧИСЛЕНИЯ

Первое число - кол-во байт до нужного поля редактирования, float значения писать в следующие после пропуска 4 байта,
 остальное - в один.

ПОЛЯ ДЛЯ ЗАПИСИ КОНКРЕТНОГО ЗНАЧЕНИЯ ПЕРЕМЕННОЙ В ФАЙЛ

Это подписать как "Basic Stats"
24 "HP Base" - float (single 32-bit)
28 "HP Scaling" - float (single 32-bit)
30 "Fever Speed" - float (single 32-bit)
34 "Sprint Speed" - float (single 32-bit)
38 "Attack Speed" - float (single 32-bit)
40 "Min DMG" - float (single 32-bit)
44 "Min DMG Scaling" - float (single 32-bit)
4C "Max DMG" - float (single 32-bit)
50 "Max DMG Scaling" - float (single 32-bit)
58 "Power" - float (single 32-bit)
5C "Power Scaling" - float (single 32-bit)
60 "Shield Break" - float (single 32-bit)
64 "Shield Break Scaling" - float (single 32-bit)
F4 "Defense" - float (single 32-bit) 
F8 "Defense Scaling" - float (single 32-bit) 
FC "Evasion" - float (single 32-bit) 
100 "Evasion Scaling" - float (single 32-bit) 
104 "Weight" - float (single 32-bit) 
108 "Weight Scaling" - float (single 32-bit)

Эти подписать как "Status Effects"
70 "Crit Base" - float (single 32-bit)
8C "Crit Scaling" - float (single 32-bit)
74 "KB Base" - float (single 32-bit)
90 "KB Scaling" - float (single 32-bit)
78 "Stagger Rate" - float (single 32-bit)
94 "Stagger Rate Scaling" - float (single 32-bit)
7C "Fire Rate" - float (single 32-bit)
98 "Fire Rate Scaling" - float (single 32-bit)
80 "Sleep Rate" - float (single 32-bit)
9C "Sleep Rate Scaling" - float (single 32-bit)
84 "Freeze Rate" - float (single 32-bit)
A0 "Freeze Rate Scaling" - float (single 32-bit)
88 "Poison Rate" - float (single 32-bit)
A4 "Poison Rate Scaling" - float (single 32-bit)
144 "Crit Res" - float (single 32-bit) 
160 "Crit Res Scaling" - float (single 32-bit) 
148 "KB Res" - float (single 32-bit) 
164 "KB Res Scaling" - float (single 32-bit) 
14C "Stagger Res" - float (single 32-bit) 
168 "Stagger Res Scaling" - float (single 32-bit) 
150 "Fire Res" - float (single 32-bit) 
16C "Fire Res Scaling" - float (single 32-bit) 
154 "Sleep Res" - float (single 32-bit) 
170 "Sleep Res Scaling" - float (single 32-bit) 
158 "Freeze Res" - float (single 32-bit) 
174 "Freeze Res Scaling" - float (single 32-bit) 
15C "Poison Res" - float (single 32-bit) 
178 "Poison Res Scaling" - float (single 32-bit)

Эти подписать как "Damage Multiplie"rs
B4 "Demons X" - float (single 32-bit)
D4 "Demons X Scaling" - float (single 32-bit)
B8 "Undead X" - float (single 32-bit)
D8 "Undead X Scaling"" - float (single 32-bit)
BC "Shells X" - float (single 32-bit)
DC "Shells X Scaling" - float (single 32-bit)
C0 "Dragons X" - float (single 32-bit)
E0 "Dragons X Scaling" - float (single 32-bit)
C4 "Giants X" - float (single 32-bit)
E4 "Giants X Scaling" - float (single 32-bit)
C8 "Wood X" - float (single 32-bit)
E8 "Wood X Scaling" - float (single 32-bit)
CC "Stone X" - float (single 32-bit)
EC "Stone X Scaling" - float (single 32-bit)
D0 "Metals X" - float (single 32-bit)
F0 "Metals X Scaling" - float (single 32-bit)

Эти подписать как "Resistance Multipliers"
118 "Slash X" - float (single 32-bit)
11C "Strike X" - float (single 32-bit)
120 "Stab X" - float (single 32-bit)
124 "Crush X" - float (single 32-bit)
128 "Flame X" - float (single 32-bit)
12C "Ice X" - float (single 32-bit)
130 "Shock X" - float (single 32-bit)
134 "Poison X" - float (single 32-bit)
138 "Sound X" - float (single 32-bit)
13C "Light X" - float (single 32-bit)
140 "Dark X" - float (single 32-bit)

ПЕРЕКЛЮЧАТЕЛИ

Эти подписать как "Attack Elements"
A5 "Slash" - 8-bit
A6 "Strike" - 8-bit
A7 "Stab" - 8-bit
A8 "Crush" - 8-bit
A9 "Fire" - 8-bit
AA "Ice" - 8-bit
AB "Lightning" - 8-bit
AC "Poison" - 8-bit
AD "Sound" - 8-bit
AE "Light" - 8-bit
AF "Darkness" - 8-bit
B0 "Burn" - 8-bit
B1 "Venom" - 8-bit

Эти подписать как "Status Immunes"
17B "Crit Imm" - 8-bit
17C "Stagger Imm" - 8-bit
17D "KB Imm" - 8-bit
17E "Fire Imm" - 8-bit
17F "Sleep Imm" - 8-bit
180 "Ice Imm" - 8-bit
181 "Poison Imm" - 8-bit
182 "Tumble Imm" - 8-bit
