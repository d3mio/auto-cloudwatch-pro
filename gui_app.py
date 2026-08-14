
import tkinter as tk
from tkinter import ttk
import random
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class CloudTelemetryApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Real-Time Cloud Telemetry & Cost Analytics Dashboard GUI')
        self.root.geometry('1200x800')
        self.root.configure(bg='#2f2f2f')

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.frame1 = tk.Frame(self.notebook, bg='#2f2f2f')
        self.frame2 = tk.Frame(self.notebook, bg='#2f2f2f')

        self.notebook.add(self.frame1, text='Telemetry')
        self.notebook.add(self.frame2, text='Cost Analytics')

        self.create_telemetry_frame()
        self.create_cost_analytics_frame()

    def create_telemetry_frame(self):
        tk.Label(self.frame1, text='Real-Time Cloud Telemetry', font=('Arial', 20), bg='#2f2f2f', fg='white').pack(pady=10)

        self.gauge_frame = tk.Frame(self.frame1, bg='#2f2f2f')
        self.gauge_frame.pack(pady=20)

        self.cpu_gauge = tk.Label(self.gauge_frame, text='CPU: 0%', font=('Arial', 16), bg='#2f2f2f', fg='white')
        self.cpu_gauge.pack(side=tk.LEFT, padx=10)

        self.memory_gauge = tk.Label(self.gauge_frame, text='Memory: 0%', font=('Arial', 16), bg='#2f2f2f', fg='white')
        self.memory_gauge.pack(side=tk.LEFT, padx=10)

        self.disk_gauge = tk.Label(self.gauge_frame, text='Disk: 0%', font=('Arial', 16), bg='#2f2f2f', fg='white')
        self.disk_gauge.pack(side=tk.LEFT, padx=10)

        self.update_telemetry()

        self.chart_frame = tk.Frame(self.frame1, bg='#2f2f2f')
        self.chart_frame.pack(pady=20)

        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Cloud Telemetry Chart')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Value')

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.chart_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.update_chart()

    def create_cost_analytics_frame(self):
        tk.Label(self.frame2, text='Cloud Cost Analytics', font=('Arial', 20), bg='#2f2f2f', fg='white').pack(pady=10)

        self.cost_frame = tk.Frame(self.frame2, bg='#2f2f2f')
        self.cost_frame.pack(pady=20)

        self.cost_label = tk.Label(self.cost_frame, text='Cost: $0.00', font=('Arial', 16), bg='#2f2f2f', fg='white')
        self.cost_label.pack(side=tk.LEFT, padx=10)

        self.update_cost_analytics()

    def update_telemetry(self):
        cpu_value = random.randint(0, 100)
        memory_value = random.randint(0, 100)
        disk_value = random.randint(0, 100)

        self.cpu_gauge['text'] = f'CPU: {cpu_value}%'
        self.memory_gauge['text'] = f'Memory: {memory_value}%'
        self.disk_gauge['text'] = f'Disk: {disk_value}%'

        self.root.after(1000, self.update_telemetry)

    def update_chart(self):
        self.ax.clear()
        self.ax.set_title('Cloud Telemetry Chart')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Value')

        data = pd.DataFrame({
            'Time': [1, 2, 3, 4, 5],
            'CPU': [10, 20, 30, 40, 50],
            'Memory': [50, 40, 30, 20, 10],
            'Disk': [20, 30, 40, 50, 60]
        })

        self.ax.plot(data['Time'], data['CPU'], label='CPU')
        self.ax.plot(data['Time'], data['Memory'], label='Memory')
        self.ax.plot(data['Time'], data['Disk'], label='Disk')

        self.ax.legend()

        self.canvas.draw()

        self.root.after(1000, self.update_chart)

    def update_cost_analytics(self):
        cost_value = round(random.uniform(0.0, 100.0), 2)

        self.cost_label['text'] = f'Cost: ${cost_value}'

        self.root.after(1000, self.update_cost_analytics)

if __name__ == '__main__':
    root = tk.Tk()
    app = CloudTelemetryApp(root)
    root.mainloop()
