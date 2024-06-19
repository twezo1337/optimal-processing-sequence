from tkinter import *
from tkinter import ttk
import random
import copy
import method_functions
from tkinter import filedialog
from PIL import Image, ImageDraw

window = Tk()
window.title('Методы оптимизации')
window.state('zoomed')
window["bg"] = "white"

matrix = []
final_matrix = []
col = 0
row = 0
image1 = Image.new("RGB", (5000, 1200), 'white')

def delete_matrix():
    global matrix, col, row
    matrix = []
    col = 0
    row = 0

    result_seq['text'] = 'Оптимальная последовательность'

    frame = ttk.Frame(borderwidth=1, relief=SOLID, style='My.TFrame')
    for c in range(0): frame.columnconfigure(index=c, weight=1)
    for r in range(0): frame.rowconfigure(index=r, weight=1)

    frame.grid(row=0, column=0, sticky=NSEW, padx=50, pady=50)

    for widget in frame4.winfo_children():
       widget.destroy()

    

def sum_x1(matrix, i):
    sum = 0
    for k in range(i):
        sum += matrix[k][0]
    return sum

def sum_x2(matrix, i, j):
    sum = 0
    for a in range(i, i + 1):
        for b in range(j):
            sum += matrix[a][b]
    return sum

def calculate():
    global matrix, final_matrix, image1

    canvas = Canvas(frame4, bg="white", cursor="pencil", scrollregion=(0,0,5000,1200))
    line_y1 = 100
    line_y2 = 140
    x1 = 100
    x2 = matrix[0][0] * 10 + x1
    x = 0

    colors = ['#EB9D42', '#EBE442', '#8CEB42', '#42EBAE', '#42D7EB', '#428FEB', '#4542EB', '#8C42EB', '#C942EB', '#EB4256']

    x_matrix = copy.deepcopy(matrix)

    
    draw = ImageDraw.Draw(image1)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            color = colors[j]
            if i == 0 and j == 0:
                canvas.create_rectangle(x1, line_y1, x2, line_y2, fill=color, outline=color)
                draw.rectangle([x1, line_y1, x2, line_y2], color)
                x = x2 - x1
                x_matrix[i][j] = x
                canvas.create_text(25, line_y1 + 17, text=f"{i + 1}", fill="#000000", font="Arial 12")
                draw.text([25, line_y1 + 17], text=f"{i + 1}", fill="#000000")
                canvas.create_line(45, line_y1 + 17, 55, line_y1 + 17)
                draw.line([45, line_y1 + 17, 55, line_y1 + 17], fill="#000000")
            elif j == 0 and i != 0:
                x = 0
                line_y1 += 50
                line_y2 += 50
                x1 = (sum_x1(matrix, i)*10) + 100
                x2 = x1 + matrix[i][j]*10
                canvas.create_rectangle(x1, line_y1, x2, line_y2, fill=color,outline=color)
                draw.rectangle([x1, line_y1, x2, line_y2], color)
                x += (x2 - x1) + ((sum_x1(matrix, i)*10))
                x_matrix[i][j] = x
                canvas.create_text(25, line_y1 + 17, text=f"{i + 1}", fill="#000000", font="Arial 12")
                draw.text([25, line_y1 + 17], text=f"{i + 1}", fill="#000000")
                canvas.create_line(45, line_y1 + 17, 55, line_y1 + 17)
                draw.line([45, line_y1 + 17, 55, line_y1 + 17], fill="#000000")
            else:
                if i >= 1 and j != 0:
                    if x_matrix[i - 1][j] > x_matrix[i][j - 1]:
                        x1 = (x2 + ((x_matrix[i - 1][j] - x_matrix[i][j - 1])))
                        x2 = x1 + matrix[i][j]*10
                        canvas.create_rectangle(x1, line_y1, x2, line_y2,fill=color,outline=color)
                        draw.rectangle([x1, line_y1, x2, line_y2], color)
                        x += (x2 - x1) + (x_matrix[i - 1][j] - x_matrix[i][j - 1])
                        x_matrix[i][j] = x
                    else:
                        x1 = x2
                        x2 = x1 + matrix[i][j]*10
                        canvas.create_rectangle(x1, line_y1, x2, line_y2,fill=color,outline=color)
                        draw.rectangle([x1, line_y1, x2, line_y2], color)
                        x += x2 - x1
                        x_matrix[i][j] = x
                else:
                    x1 = x2
                    x2 = x1 + matrix[i][j]*10
                    canvas.create_rectangle(x1, line_y1, x2, line_y2,fill=color,outline=color)
                    draw.rectangle([x1, line_y1, x2, line_y2], color)
                    x += x2 - x1
                    x_matrix[i][j] = x

    canvas.create_line(50, 50, 50, 140 + (50 * len(matrix)))
    draw.line([50, 50, 50, 140 + (50 * len(matrix))], fill="#000000")
    canvas.create_line(50, 140 + (50 * len(matrix)), x_matrix[len(x_matrix) - 1][len(x_matrix[0]) - 1] + 200, 140 + (50 * len(matrix)))
    draw.line([50, 140 + (50 * len(matrix)), x_matrix[len(x_matrix) - 1][len(x_matrix[0]) - 1] + 200, 140 + (50 * len(matrix))], fill="#000000")

    ox_x = 100
    for i in range((x_matrix[len(x_matrix) - 1][len(x_matrix[0]) - 1] + 100)):
        if i == 0 or i % 50 == 0:
            canvas.create_line(ox_x, 140 + (50 * len(matrix)) - 5, ox_x, 140 + (50 * len(matrix)) + 5)
            draw.line([ox_x, 140 + (50 * len(matrix)) - 5, ox_x, 140 + (50 * len(matrix)) + 5], fill="#000000")
            canvas.create_text(ox_x, 140 + (50 * len(matrix)) + 25, text=f"{i / 10}", fill="#000000", font="Arial 12")
            draw.text([ox_x, 140 + (50 * len(matrix)) + 25], text=f"{i / 10}", fill="#000000")
            ox_x += 50

    if method.get() == 'jons':
        result_seq['text'] = method_functions.jons_final_seq(method_functions.rec1_jons(matrix), method_functions.rec2_jons(matrix), method_functions.rec4_jons(matrix))
        final_matrix = method_functions.final_matrix(matrix, method_functions.jons_final_seq(method_functions.rec1_jons(matrix), method_functions.rec2_jons(matrix), method_functions.rec4_jons(matrix)))

        frame = ttk.Frame(borderwidth=1, relief=SOLID, style='My.TFrame')
        for c in range(col + 1): frame.columnconfigure(index=c, weight=1)
        for r in range(row + 1): frame.rowconfigure(index=r, weight=1)

        for r in range(row + 1):
            for c in range(col + 1):
                if r == 0 and c == 0:
                    cell = ttk.Button(frame, text='Деталь\nСтанок', state=DISABLED)
                    cell.grid(row=r, column=c, sticky=NSEW)
                elif c == 0:
                    cell = ttk.Button(frame, text=f'{r}', state=DISABLED)#
                    cell.grid(row=r, column=c, sticky=NSEW)
                elif r == 0:
                    cell = ttk.Button(frame, text=f'{c}', state=DISABLED)
                    cell.grid(row=r, column=c, sticky=NSEW)

        for r in range(row):
            for c in range(col):
                cell = ttk.Button(frame, text=f"{final_matrix[r][c]}", state=DISABLED)
                cell.grid(row=r+1, column=c+1, sticky=NSEW)
        
        frame.grid(row=0, column=0, sticky=NSEW, padx=50, pady=50)
    else:
        result_seq['text'] = method_functions.sokol_final_seq(matrix, method_functions.rec1_sokol(matrix), method_functions.rec2_sokol(matrix), method_functions.rec3_sokol(matrix))
        final_matrix = method_functions.final_matrix(matrix, method_functions.sokol_final_seq(matrix, method_functions.rec1_sokol(matrix), method_functions.rec2_sokol(matrix), method_functions.rec3_sokol(matrix)))\

        frame = ttk.Frame(borderwidth=1, relief=SOLID, style='My.TFrame')
        for c in range(col + 1): frame.columnconfigure(index=c, weight=1)
        for r in range(row + 1): frame.rowconfigure(index=r, weight=1)

        for r in range(row + 1):
            for c in range(col + 1):
                if r == 0 and c == 0:
                    cell = ttk.Button(frame, text='Деталь\nСтанок', state=DISABLED)
                    cell.grid(row=r, column=c, sticky=NSEW)
                elif c == 0:
                    cell = ttk.Button(frame, text=f'{r}', state=DISABLED)#
                    cell.grid(row=r, column=c, sticky=NSEW)
                elif r == 0:
                    cell = ttk.Button(frame, text=f'{c}', state=DISABLED)
                    cell.grid(row=r, column=c, sticky=NSEW)

        for r in range(row):
            for c in range(col):
                cell = ttk.Button(frame, text=f"{final_matrix[r][c]}", state=DISABLED)
                cell.grid(row=r+1, column=c+1, sticky=NSEW)
        
        frame.grid(row=0, column=0, sticky=NSEW, padx=50, pady=50)


    hbar=Scrollbar(canvas,orient=HORIZONTAL)
    hbar.pack(side=BOTTOM,fill=X)
    hbar.config(command=canvas.xview)
    vbar=Scrollbar(canvas,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=canvas.yview)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

    canvas.pack(side=LEFT,expand=True,fill=BOTH)

def save_files():
    matrixpath = filedialog.asksaveasfilename(initialfile='matrix.txt', filetypes=(("TXT files", "*.txt"),))
    with open(matrixpath, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')
    
    diagramname = filedialog.asksaveasfilename(initialfile='gant.jpg', filetypes=(("JPG files", "*.jpg"),))
    diagramname += '.jpg'
    image1.save(diagramname)

def get_file_matrix():
    global matrix, row, col
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            matrix = [list(map(int, row.split())) for row in file.readlines()]

    col = len(matrix[0])
    row = len(matrix)

    frame = ttk.Frame(borderwidth=1, relief=SOLID, style='My.TFrame')
    for c in range(col + 1): frame.columnconfigure(index=c, weight=1)
    for r in range(row + 1): frame.rowconfigure(index=r, weight=1)

    for r in range(row + 1):
        for c in range(col + 1):
            if r == 0 and c == 0:
                cell = ttk.Button(frame, text='Деталь\nСтанок', state=DISABLED)
                cell.grid(row=r, column=c, sticky=NSEW)
            elif c == 0:
                cell = ttk.Button(frame, text=f'{r}', state=DISABLED)#
                cell.grid(row=r, column=c, sticky=NSEW)
            elif r == 0:
                cell = ttk.Button(frame, text=f'{c}', state=DISABLED)
                cell.grid(row=r, column=c, sticky=NSEW)

    for r in range(row):
        for c in range(col):
            cell = ttk.Button(frame, text=f"{matrix[r][c]}", state=DISABLED)
            cell.grid(row=r+1, column=c+1, sticky=NSEW)

    frame.grid(row=0, column=0, sticky=NSEW, padx=50, pady=50)

def get_random_matrix():
    global matrix, row, col
    col = 0
    row = 1
    while row > col:
        col = random.randint(3, 10)
        row = random.randint(3, 10)
    
    matrix = [ [0]*col for i in range(row) ]

    for i in range(row):
        for j in range(col):
            matrix[i][j] = random.randint(1, 30)

    frame = ttk.Frame(borderwidth=1, relief=SOLID, style='My.TFrame')
    for c in range(col + 1): frame.columnconfigure(index=c, weight=1)
    for r in range(row + 1): frame.rowconfigure(index=r, weight=1)

    for r in range(row + 1):
        for c in range(col + 1):
            if r == 0 and c == 0:
                cell = ttk.Button(frame, text='Деталь\nСтанок', state=DISABLED)
                cell.grid(row=r, column=c, sticky=NSEW)
            elif c == 0:
                cell = ttk.Button(frame, text=f'{r}', state=DISABLED)#
                cell.grid(row=r, column=c, sticky=NSEW)
            elif r == 0:
                cell = ttk.Button(frame, text=f'{c}', state=DISABLED)
                cell.grid(row=r, column=c, sticky=NSEW)

    for r in range(row):
        for c in range(col):
            cell = ttk.Button(frame, text=f"{matrix[r][c]}", state=DISABLED)
            cell.grid(row=r+1, column=c+1, sticky=NSEW)

    frame.grid(row=0, column=0, sticky=NSEW, padx=50, pady=50)




for c in range(3): window.columnconfigure(index=c, weight=1)
for r in range(3): window.rowconfigure(index=r, weight=1)

s = ttk.Style()
s.configure('My.TFrame', background='white')

#frame1

frame = ttk.Frame(borderwidth=1, relief=SOLID, style='My.TFrame')


#frame2
frame2 = ttk.Frame(style='My.TFrame')
for c in range(1): frame2.columnconfigure(index=c, weight=1)
for r in range(5): frame2.rowconfigure(index=r, weight=1)

l1 = ttk.Label(frame2, text="Действия", font='Jomolhari 20', foreground='#4F0F01', background='white')
l1.grid(row=0, column=0, sticky=NW)

s = ttk.Style()
s.configure('btn.TButton', font=('Jomolhari', 14))
btn_matrix_from_file = ttk.Button(frame2, text="Загрузить матрицу из файла", style='btn.TButton', command=get_file_matrix)
btn_matrix_from_file.grid(row=1, column=0, sticky=NSEW)
btn_matrix_gen = ttk.Button(frame2, text="Сгенерировать матрицу", style='btn.TButton', command=get_random_matrix)
btn_matrix_gen.grid(row=2, column=0, sticky=NSEW)
btn_matrix_del = ttk.Button(frame2, text="Удалить матрицу", style='btn.TButton', command=delete_matrix)
btn_matrix_del.grid(row=3, column=0, sticky=NSEW)
btn_matrix_save = ttk.Button(frame2, text="Сохранить матрицу", style='btn.TButton', command=save_files)
btn_matrix_save.grid(row=4, column=0, sticky=NSEW)

frame2.grid(row=0, column=1, sticky=NSEW, pady=50)



#frame3
frame3 = ttk.Frame( style='My.TFrame')

for c in range(1): frame3.columnconfigure(index=c, weight=1)
for r in range(4): frame3.rowconfigure(index=r, weight=1)

l1 = ttk.Label(frame3, text="Выбор метода для вычисления", font='Jomolhari 20', foreground='#4F0F01', background='white')
l1.grid(row=0, column=0, sticky=NW)

result_seq = ttk.Label(frame3, text="Оптимальная последовательность", font='Jomolhari 16', foreground='#4F0F01', background='white')
result_seq.grid(row=1, column=0, sticky=S)

s = ttk.Style()
s.configure('btn.TRadiobutton', font=('Jomolhari', 14),  background='white')
method = StringVar(value='') 
method_jons_btn = ttk.Radiobutton(frame3, text='Метод джонсона', value='jons', variable=method, style='btn.TRadiobutton')
method_jons_btn.grid(row=2, column=0, sticky=NW, pady=50)
method_sokol_btn = ttk.Radiobutton(frame3, text='Метод Соколовского', value='sokol', variable=method, style='btn.TRadiobutton')
method_sokol_btn.grid(row=2, column=0, sticky=SW, pady=50)

btn_matrix_result = ttk.Button(frame3, text="Вычислить", style='btn.TButton', command=calculate)
btn_matrix_result.grid(row=3, column=0, sticky=NSEW)

frame3.grid(row=0, column=2, sticky=NSEW, pady=50, padx=50)

frame4 = ttk.Frame( style='My.TFrame')

frame4.grid(row=1, column=0, rowspan=2, columnspan=3, sticky=NSEW)


window.mainloop()