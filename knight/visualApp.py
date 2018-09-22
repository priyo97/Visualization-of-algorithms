import tkinter as tk
from utility import initiate, runDijkstra,runAstar,runBFS,runDFS


def main():

	window = tk.Tk()

	window.geometry("200x200")

	

	tk.Label(window, text="Enter Grid Size:").grid(row=0)

	v = tk.StringVar()

	e1 = tk.Entry(window,textvariable=v)

	e1.grid(row=0, column=1)


	

	var = tk.StringVar()
	
	R1 = tk.Radiobutton(window, text="BFS", variable=var, value=1)
	
	R1.grid(row=2,column=0)

	R2 = tk.Radiobutton(window, text="DFS", variable=var, value=2)

	R2.grid(row=2,column=1)

	R3 = tk.Radiobutton(window, text="Dijkstra", variable=var, value=3)

	R3.grid(row=3,column=0)

	R4 = tk.Radiobutton(window, text="A*Star", variable=var, value=4)

	R4.grid(row=3,column=1)


	B = tk.Button(window,text ="Generate", command = lambda: generate(v.get(),var.get()))
	B.grid(row=4,column=0)
	
	


	window.mainloop()


def generate(a,b):

	n = int(a)
	option = int(b)

	pos, gameDisplay = initiate(n)


	d = {1:runBFS,2:runDFS,3:runDijkstra,4:runAstar}
	
	d[option](n,pos,gameDisplay)


main()