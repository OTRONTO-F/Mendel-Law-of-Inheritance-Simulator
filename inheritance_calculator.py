import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class ModernMendelGUI:
    def __init__(self, root):
        # Define color scheme
        self.colors = {
            'bg_dark': '#1a1a1a',        # Background
            'bg_darker': '#0d0d0d',      # Darker background
            'text': '#ffffff',           # Main text
            'text_secondary': '#b3b3b3', # Secondary text
            'accent': '#00ffff',         # Cyan accent
            'border': '#333333',         # Border color
            'dominant': '#4dff88',       # Green for dominant
            'recessive': '#ff6b6b',      # Red for recessive
        }
        
        self.root = root
        self.root.title("Mendel's Law of Inheritance")
        
        # Set fullscreen
        self.root.state('zoomed')
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Set minimum size
        self.root.minsize(1200, 800)
        
        # Configure root window
        self.root.configure(bg=self.colors['bg_dark'])
        
        # Add key binding to exit fullscreen with Escape key
        self.root.bind('<Escape>', lambda e: self.root.state('normal'))
        
        # Initialize variables
        self.parent1_var = tk.StringVar(value="Aa")
        self.parent2_var = tk.StringVar(value="aa")
        
        # Create main layout
        self.create_layout()
        
    def create_layout(self):
        # Header
        header = tk.Frame(self.root, bg=self.colors['bg_dark'])
        header.pack(fill='x', padx=20, pady=20)
        
        title = tk.Label(
            header,
            text="Mendel's Law of Inheritance",
            font=("Segoe UI", 36, "bold"),
            fg=self.colors['accent'],
            bg=self.colors['bg_dark']
        )
        title.pack()
        
        subtitle = tk.Label(
            header,
            text="Interactive Genetic Inheritance Simulator",
            font=("Segoe UI", 14),
            fg=self.colors['text_secondary'],
            bg=self.colors['bg_dark']
        )
        subtitle.pack(pady=(5,20))
        
        # Main content container with 3 columns
        content = tk.Frame(self.root, bg=self.colors['bg_dark'])
        content.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Create panels
        left_panel = tk.Frame(content, bg=self.colors['bg_dark'])
        left_panel.pack(side='left', fill='both', expand=True, padx=(0,10))
        
        center_panel = tk.Frame(content, bg=self.colors['bg_dark'])
        center_panel.pack(side='left', fill='both', expand=True, padx=10)
        
        right_panel = tk.Frame(content, bg=self.colors['bg_dark'])
        right_panel.pack(side='right', fill='both', expand=True, padx=(10,0))
        
        # Create sections (removed header parameters)
        self.create_input_section(left_panel)
        self.create_punnett_square(left_panel)
        self.create_explanation_section(center_panel)
        self.create_visualization_section(right_panel)

    def create_input_section(self, parent):
        frame = tk.LabelFrame(
            parent,
            text="👥 Genotype Selection",
            font=("Segoe UI", 12),
            fg=self.colors['text'],
            bg=self.colors['bg_darker'],
            relief='flat',
            highlightthickness=1,
            highlightbackground=self.colors['border']
        )
        frame.pack(fill='x', pady=(0,20))
        
        # Parent 1
        p1_frame = tk.Frame(frame, bg=self.colors['bg_darker'])
        p1_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(
            p1_frame,
            text="Parent 1:",
            font=("Segoe UI", 11),
            fg=self.colors['text'],
            bg=self.colors['bg_darker']
        ).pack(side='left')
        
        for value in ["AA", "Aa", "aa"]:
            rb = tk.Radiobutton(
                p1_frame,
                text=value,
                variable=self.parent1_var,
                value=value,
                font=("Segoe UI", 11),
                fg=self.colors['text'],
                bg=self.colors['bg_darker'],
                selectcolor=self.colors['bg_dark'],
                activebackground=self.colors['bg_darker'],
                activeforeground=self.colors['accent']
            )
            rb.pack(side='left', padx=10)
            
        # Parent 2 (similar structure)
        p2_frame = tk.Frame(frame, bg=self.colors['bg_darker'])
        p2_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(
            p2_frame,
            text="Parent 2:",
            font=("Segoe UI", 11),
            fg=self.colors['text'],
            bg=self.colors['bg_darker']
        ).pack(side='left')
        
        for value in ["AA", "Aa", "aa"]:
            rb = tk.Radiobutton(
                p2_frame,
                text=value,
                variable=self.parent2_var,
                value=value,
                font=("Segoe UI", 11),
                fg=self.colors['text'],
                bg=self.colors['bg_darker'],
                selectcolor=self.colors['bg_dark'],
                activebackground=self.colors['bg_darker'],
                activeforeground=self.colors['accent']
            )
            rb.pack(side='left', padx=10)
            
        # Calculate button
        button = tk.Button(
            frame,
            text="Calculate Inheritance",
            font=("Segoe UI", 11),
            fg=self.colors['bg_dark'],
            bg=self.colors['accent'],
            relief='flat',
            command=self.calculate_inheritance,
            cursor='hand2'
        )
        button.pack(pady=15)
        
    def create_punnett_square(self, parent):
        self.punnett_frame = tk.LabelFrame(
            parent,
            text="📊 Punnett Square",
            font=("Segoe UI", 12),
            fg=self.colors['text'],
            bg=self.colors['bg_darker'],
            relief='flat',
            highlightthickness=1,
            highlightbackground=self.colors['border']
        )
        self.punnett_frame.pack(fill='x', pady=(0,20))
        
        # Configure grid weights
        for i in range(3):
            self.punnett_frame.grid_columnconfigure(i, weight=1, minsize=100)
            self.punnett_frame.grid_rowconfigure(i, weight=1, minsize=100)

    def update_punnett_square(self, grid_labels):
        for widget in self.punnett_frame.winfo_children():
            widget.destroy()
        
        # Create styled cells
        for i in range(3):
            for j in range(3):
                is_header = i == 0 or j == 0
                is_corner = i == 0 and j == 0
                
                cell_frame = tk.Frame(
                    self.punnett_frame,
                    bg=self.colors['bg_darker'],
                    highlightthickness=1,
                    highlightbackground=self.colors['border']
                )
                cell_frame.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
                
                # Skip corner cell
                if is_corner:
                    continue
                
                # Cell content
                text = grid_labels[i][j]
                label = tk.Label(
                    cell_frame,
                    text=text,
                    font=("Segoe UI", 14, "bold" if not is_header else "normal"),
                    fg=self.colors['accent'] if is_header else self.colors['text'],
                    bg=self.colors['bg_darker'],
                    width=4,
                    height=2
                )
                label.pack(expand=True, fill='both', padx=5, pady=5)

    def create_visualization_section(self, parent):
        viz_frame = tk.LabelFrame(
            parent,
            text="🧬 Inheritance Distribution",
            font=("Segoe UI", 12),
            fg=self.colors['text'],
            bg=self.colors['bg_darker'],
            relief='flat',
            highlightthickness=1,
            highlightbackground=self.colors['border']
        )
        viz_frame.pack(fill='both', expand=True, pady=(0,20))
        
        # Create matplotlib figure with dark theme
        plt.style.use('dark_background')
        self.figure, self.ax = plt.subplots(figsize=(8, 8))
        self.figure.patch.set_facecolor(self.colors['bg_darker'])
        self.ax.set_facecolor(self.colors['bg_darker'])
        
        # Initial empty donut chart
        self.ax.pie([1], colors=[self.colors['bg_darker']], 
                    radius=1.3, 
                    wedgeprops=dict(width=0.5, edgecolor=self.colors['border']))
        self.ax.text(0, 0, "Calculate\nInheritance", 
                    ha='center', va='center',
                    color=self.colors['text'],
                    fontsize=12,
                    fontweight='bold')
        
        self.canvas = FigureCanvasTkAgg(self.figure, viz_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True, padx=20, pady=20)

    def update_visualization(self, dominant, recessive, total):
        self.ax.clear()
        
        # Calculate percentages
        dom_pct = dominant/total * 100
        rec_pct = recessive/total * 100
        
        # Create data for donut chart
        sizes = [dom_pct, rec_pct]
        colors = [self.colors['dominant'], self.colors['recessive']]
        
        # Create donut chart
        wedges, _ = self.ax.pie(sizes, 
                               colors=colors,
                               radius=1.3,
                               wedgeprops=dict(width=0.5, edgecolor='none'))
        
        # Add center text with ratio
        ratio_text = f"Ratio\n{dominant}:{recessive}"
        self.ax.text(0, 0, ratio_text, 
                    ha='center', va='center',
                    color=self.colors['accent'],
                    fontsize=16,
                    fontweight='bold')
        
        # Add labels with dots
        legend_y_positions = [1.2, -1.2]
        legend_x_position = 1.5
        
        for i, (pct, label_text) in enumerate([
            (dom_pct, "Dominant (A_)"),
            (rec_pct, "Recessive (aa)")
        ]):
            # Add dot
            self.ax.plot(legend_x_position - 0.2, legend_y_positions[i], 
                        'o', color=colors[i], markersize=10)
            
            # Add label
            self.ax.text(legend_x_position, legend_y_positions[i],
                        f" {label_text}\n {pct:.1f}%",
                        color=self.colors['text'],
                        va='center',
                        fontsize=10,
                        fontweight='bold')
        
        # Set equal aspect ratio and remove axes
        self.ax.axis('equal')
        self.ax.set_frame_on(False)
        
        # Add title
        self.ax.text(0, 1.5, "Inheritance Distribution",
                    ha='center', va='center',
                    color=self.colors['accent'],
                    fontsize=14,
                    fontweight='bold')
        
        # Update canvas
        self.figure.tight_layout()
        self.canvas.draw()

    def create_stats_section(self, parent):
        stats_frame = tk.LabelFrame(
            parent,
            text="Statistics",
            font=("Segoe UI", 12),
            fg=self.colors['text'],
            bg=self.colors['bg_darker'],
            relief='flat',
            highlightthickness=1,
            highlightbackground=self.colors['border']
        )
        stats_frame.pack(fill='x')
        
        self.stats_label = tk.Label(
            stats_frame,
            text="Select parent genotypes and calculate inheritance",
            font=("Segoe UI", 11),
            fg=self.colors['text'],
            bg=self.colors['bg_darker']
        )
        self.stats_label.pack(pady=15)

    def create_explanation_section(self, parent):
        explanation_frame = tk.LabelFrame(
            parent,
            text="📝 Inheritance Explanation",
            font=("Segoe UI", 12),
            fg=self.colors['text'],
            bg=self.colors['bg_darker'],
            relief='flat',
            highlightthickness=1,
            highlightbackground=self.colors['border']
        )
        explanation_frame.pack(fill='both', expand=True)
        
        # Create canvas for custom drawing and animation
        self.explanation_canvas = tk.Canvas(
            explanation_frame,
            bg=self.colors['bg_darker'],
            highlightthickness=0
        )
        self.explanation_canvas.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Initial explanation text
        self.explanation_text = [
            ("Genotype Basics:", self.colors['accent']),
            "• AA: Homozygous Dominant - Pure dominant trait",
            "• Aa: Heterozygous - Carries both traits",
            "• aa: Homozygous Recessive - Pure recessive trait",
            "",
            ("Inheritance Patterns:", self.colors['accent']),
            "• A is dominant over a (Capital letter dominates)",
            "• Each parent contributes one allele randomly",
            "• Punnett square shows all possible combinations",
            "",
            ("Phenotype Expression:", self.colors['accent']),
            "• A_ (AA or Aa): Shows dominant characteristic",
            "• aa: Shows recessive characteristic only",
            "• Ratios follow Mendel's First Law"
        ]
        
        self.animate_explanation()

    def animate_explanation(self):
        self.explanation_canvas.delete('all')
        y = 20
        
        for i, text in enumerate(self.explanation_text):
            # Delayed text animation
            if isinstance(text, tuple):
                # Headers with accent color
                self.root.after(i * 100, self.add_text, text[0], 20, y, text[1])
            else:
                # Regular text with fade-in effect
                self.root.after(i * 100, self.add_text, text, 20, y, self.colors['text'])
            y += 30

    def add_text(self, text, x, y, color):
        # Create text with fade-in and glow effect
        text_id = self.explanation_canvas.create_text(
            x, y,
            text=text,
            anchor='w',
            font=("Segoe UI", 11),
            fill=color
        )
        
        # Enhanced hover effect
        def on_enter(e):
            # Create glow effect
            self.explanation_canvas.itemconfig(
                text_id,
                font=("Segoe UI", 11, "bold"),
                fill=self.colors['accent']
            )
            # Add subtle animation
            self.explanation_canvas.move(text_id, 5, 0)
        
        def on_leave(e):
            self.explanation_canvas.itemconfig(
                text_id,
                font=("Segoe UI", 11),
                fill=color
            )
            self.explanation_canvas.move(text_id, -5, 0)
        
        self.explanation_canvas.tag_bind(text_id, '<Enter>', on_enter)
        self.explanation_canvas.tag_bind(text_id, '<Leave>', on_leave)
        
        # Smooth fade-in animation
        for alpha in range(0, 21):  # More steps for smoother animation
            self.root.after(alpha * 25, lambda a=alpha: self.explanation_canvas.itemconfig(
                text_id,
                fill=self.interpolate_color(self.colors['bg_darker'], color, a/20)
            ))

    def calculate_inheritance(self):
        # Get parent genotypes
        p1 = self.parent1_var.get()
        p2 = self.parent2_var.get()
        
        # Create Punnett Square
        alleles1 = list(p1)
        alleles2 = list(p2)
        
        # Create grid labels
        grid_labels = [[''] + alleles2]  # First row with p2 alleles
        for a1 in alleles1:
            row = [a1]  # First column with p1 alleles
            for a2 in alleles2:
                genotype = ''.join(sorted([a1, a2]))  # Sort to maintain consistent order
                row.append(genotype)
            grid_labels.append(row)
        
        # Update Punnett Square with new styling
        self.update_punnett_square(grid_labels)
        
        # Calculate and update results
        offspring = []
        for a1 in alleles1:
            for a2 in alleles2:
                offspring.append(''.join(sorted([a1, a2])))
        
        dominant = sum(1 for g in offspring if 'A' in g)
        recessive = len(offspring) - dominant
        
        # Update explanation text
        result_text = [
            "",
            ("Current Cross Results:", self.colors['accent']),
            f"• Parent 1: {p1} ({self.get_genotype_description(p1)})",
            f"• Parent 2: {p2} ({self.get_genotype_description(p2)})",
            f"• Dominant Offspring: {dominant/len(offspring)*100:.1f}%",
            f"• Recessive Offspring: {recessive/len(offspring)*100:.1f}%",
            f"• Phenotype Ratio: {dominant}:{recessive}"
        ]
        
        # Update explanation (prevent duplication)
        if len(self.explanation_text) > 14:
            self.explanation_text = self.explanation_text[:14]
        self.explanation_text.extend(result_text)
        self.animate_explanation()
        
        # Update visualization
        self.update_visualization(dominant, recessive, len(offspring))

    def get_genotype_description(self, genotype):
        descriptions = {
            "AA": "Homozygous Dominant",
            "Aa": "Heterozygous",
            "aa": "Homozygous Recessive"
        }
        return descriptions.get(genotype, "")

    def create_section_header(self, text, icon):
        """Helper function to create consistent section headers"""
        return f"{icon} {text}"

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ModernMendelGUI(root)
    root.mainloop()