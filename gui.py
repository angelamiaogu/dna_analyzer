from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel,QLineEdit, QPushButton, QMessageBox
from dna_utils import translate_dna_to_rna, translate_rna_to_dna, translate_rna_to_protein, get_reverse_complement,calculate_gc_content
class DNAAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DNA Analyzer")
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.dna_label = QLabel("Enter DNA:")
        self.layout.addWidget(self.dna_label)

        self.dna_input = QLineEdit()
        self.layout.addWidget(self.dna_input)

        self.translate_dna_to_rna_button = QPushButton("Translate DNA to RNA")
        self.translate_dna_to_rna_button.clicked.connect(self.translate_dna_to_rna)
        self.layout.addWidget(self.translate_dna_to_rna_button)

        self.translate_rna_to_dna_button = QPushButton("Translate RNA to DNA")
        self.translate_rna_to_dna_button.clicked.connect(self.translate_rna_to_dna)
        self.layout.addWidget(self.translate_rna_to_dna_button)

        self.translate_rna_to_protein_button = QPushButton("Translate RNA to Protein")
        self.translate_rna_to_protein_button.clicked.connect(self.translate_rna_to_protein)
        self.layout.addWidget(self.translate_rna_to_protein_button)

        self.reverse_complement_button = QPushButton("Get Reverse Complement")
        self.reverse_complement_button.clicked.connect(self.reverse_complement)
        self.layout.addWidget(self.reverse_complement_button)

        self.gc_content_button = QPushButton("Calculate GC Content")
        self.gc_content_button.clicked.connect(self.gc_content)
        self.layout.addWidget(self.gc_content_button)

    def translate_dna_to_rna(self):
        rna = translate_dna_to_rna(self.dna_input.text())
        QMessageBox.information(self, "RNA", rna)

    def translate_rna_to_dna(self):
        dna = translate_rna_to_dna(self.dna_input.text())
        QMessageBox.information(self, "DNA", dna)

    def translate_rna_to_protein(self):
        protein = translate_rna_to_protein(self.dna_input.text())
        QMessageBox.information(self, "Protein", protein)

    def reverse_complement(self):
        rev_comp = get_reverse_complement(self.dna_input.text())
        QMessageBox.information(self, "Reverse Complement", rev_comp)

    def gc_content(self):
        gc_content = calculate_gc_content(self.dna_input.text())
        QMessageBox.information(self, "GC Content", str(gc_content) + "%")
