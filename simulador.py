import tkinter as tk
from tkinter import ttk, messagebox

DISK_SIZE = 100

class DiskSimulator:
    def __init__(self, size):
        self.size = size
        self.blocks = [None] * size
        self.files = {}

    def allocate_contiguous(self, filename, block_count):
        for i in range(self.size - block_count + 1):
            if all(block is None for block in self.blocks[i:i + block_count]):
                self.blocks[i:i + block_count] = [filename] * block_count
                self.files[filename] = list(range(i, i + block_count))
                return True
        return False

    def allocate_linked(self, filename, block_count):
        free_blocks = [i for i, block in enumerate(self.blocks) if block is None]
        if len(free_blocks) >= block_count:
            allocated = free_blocks[:block_count]
            for block in allocated:
                self.blocks[block] = filename
            self.files[filename] = allocated
            return True
        return False

    def allocate_indexed(self, filename, block_count):
        free_blocks = [i for i, block in enumerate(self.blocks) if block is None]
        if len(free_blocks) >= block_count + 1:
            index_block = free_blocks[0]
            data_blocks = free_blocks[1:block_count + 1]
            self.blocks[index_block] = f"{filename}_index"
            for block in data_blocks:
                self.blocks[block] = filename
            self.files[filename] = [index_block] + data_blocks
            return True
        return False

    def delete_file(self, filename):
        if filename in self.files:
            for block in self.files[filename]:
                self.blocks[block] = None
            del self.files[filename]
            return True
        return False

class SimulatorGUI:
    def __init__(self, root, disk_simulator):
        self.root = root
        self.disk_simulator = disk_simulator

        self.root.title("Simulador de Alocação de Blocos")
        self.canvas = tk.Canvas(self.root, width=800, height=100, bg="white")
        self.canvas.pack()

        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack(pady=10)

        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack()

        self.create_controls()
        self.create_table()
        self.draw_disk()

    def create_controls(self):
        tk.Label(self.controls_frame, text="Nome do Arquivo:").grid(row=0, column=0, padx=5)
        self.filename_entry = tk.Entry(self.controls_frame)
        self.filename_entry.grid(row=0, column=1, padx=5)

        tk.Label(self.controls_frame, text="Blocos:").grid(row=0, column=2, padx=5)
        self.blocks_entry = tk.Entry(self.controls_frame, width=5)
        self.blocks_entry.grid(row=0, column=3, padx=5)

        tk.Label(self.controls_frame, text="Modo:").grid(row=0, column=4, padx=5)
        self.mode_var = tk.StringVar(value="Contígua")
        tk.OptionMenu(self.controls_frame, self.mode_var, "Contígua", "Encadeada", "Indexada").grid(row=0, column=5, padx=5)

        tk.Button(self.controls_frame, text="Criar Arquivo", command=self.create_file).grid(row=0, column=6, padx=5)
        tk.Button(self.controls_frame, text="Excluir Arquivo", command=self.delete_file).grid(row=0, column=7, padx=5)

    def create_table(self):
        columns = ("Nome", "Blocos Alocados")
        self.table = ttk.Treeview(self.table_frame, columns=columns, show="headings", height=10)
        self.table.heading("Nome", text="Nome do Arquivo")
        self.table.heading("Blocos Alocados", text="Blocos Alocados")
        self.table.pack(fill=tk.BOTH, expand=True)
        self.table.bind("<ButtonRelease-1>", self.highlight_file)

    def draw_disk(self):
        self.canvas.delete("all")
        block_width = 800 / self.disk_simulator.size
        for i, block in enumerate(self.disk_simulator.blocks):
            color = "white" if block is None else "lightblue"
            self.canvas.create_rectangle(
                i * block_width, 0, (i + 1) * block_width, 40,
                fill=color, outline="black"
            )
            if block:
                self.canvas.create_text(
                    (i + 0.5) * block_width, 20,
                    text=block, font=("Arial", 8)
                )
        self.update_table()

    def update_table(self):
        for item in self.table.get_children():
            self.table.delete(item)
        for filename, blocks in self.disk_simulator.files.items():
            self.table.insert("", tk.END, values=(filename, blocks))

    def highlight_file(self, event):
        selected_item = self.table.selection()
        if selected_item:
            filename = self.table.item(selected_item)["values"][0]
            blocks = self.disk_simulator.files.get(filename, [])
            self.canvas.delete("highlight")
            block_width = 800 / self.disk_simulator.size
            for block in blocks:
                self.canvas.create_rectangle(
                    block * block_width, 0, (block + 1) * block_width, 40,
                    fill="orange", outline="black", tags="highlight"
                )

    def create_file(self):
        filename = self.filename_entry.get().strip()
        try:
            block_count = int(self.blocks_entry.get())
            if not filename or block_count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Nome do arquivo ou número de blocos inválido!")
            return

        mode = self.mode_var.get()
        success = False
        if mode == "Contígua":
            success = self.disk_simulator.allocate_contiguous(filename, block_count)
        elif mode == "Encadeada":
            success = self.disk_simulator.allocate_linked(filename, block_count)
        elif mode == "Indexada":
            success = self.disk_simulator.allocate_indexed(filename, block_count)

        if success:
            self.draw_disk()
        else:
            messagebox.showerror("Erro", "Não foi possível alocar os blocos!")

    def delete_file(self):
        filename = self.filename_entry.get().strip()
        if self.disk_simulator.delete_file(filename):
            self.draw_disk()
        else:
            messagebox.showerror("Erro", "Arquivo não encontrado!")

if __name__ == "__main__":
    root = tk.Tk()
    simulator = DiskSimulator(DISK_SIZE)
    gui = SimulatorGUI(root, simulator)
    root.mainloop()
