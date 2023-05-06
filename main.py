import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QBoxLayout, QLabel, QPushButton, QWidget, QFileDialog, QCheckBox, QScrollArea, QDialog, QDialogButtonBox, QMessageBox, QLineEdit, QFormLayout, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QSizePolicy, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame
from PySide6.QtCore import Qt, QDate, QTime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('Sistema de PDV')
        self.resize(500, 500)

    products = [{'name': 'Mouse', 'brand': 'Logitech', 'category': 'Periféricos', 'price': '10.00', 'quantity': '10', 'description': 'Mouse M100'}, 
                {'name': 'Teclado', 'brand': 'Logitech', 'category': 'Periféricos', 'price': '50.00', 'quantity': '10', 'description': 'Teclado K70'}, 
                {'name': 'Monitor LED C23F390F', 'brand': 'Samsung', 'category': 'Monitores', 'price': '800.00', 'quantity': '10', 'description': 'Monitor Samsung LED Curvo 23 Full HD C23F390F'}]

    # Método initUI deve inicializar a interface gráfica
    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.create_product_selection()
        self.create_quantity_selection()
        self.product_price()
        self.create_add_product_button()
        self.create_product_table()
        self.create_total_price_label()
        self.create_remove_product_button()
        self.create_cancel_sale_button()
        self.create_finish_sale_button()


    # Criar um método para selecionar os produtos cadastrados na lista, ver os detalhes e ver o preço final de acordo com a quantidade e produto selecionado
    def create_product_selection(self):
        self.product_selection = QComboBox()
        self.product_selection.addItems([product['name'] for product in self.products])
        self.layout.addWidget(self.product_selection)
    
    # Criar um método para selecionar a quantidade de produtos
    def create_quantity_selection(self):
        self.quantity_selection = QSpinBox()
        self.quantity_selection.setMinimum(1)
        self.quantity_selection.setMaximum(100)
        self.quantity_selection.setValue(1)
        self.layout.addWidget(self.quantity_selection)
        
    # Criar um método para mostrar e atualizar o preço de acordo com a quantidade e produto selecionado em self.product_selection
    def product_price(self):
        self.product_selected = self.product_selection.currentText()
        self.product_price_label = QLabel('Preço Unitário:')
        self.layout.addWidget(self.product_price_label)
        self.product_price = QComboBox()
        self.product_price.setEditable(False)
        self.product_price.setDisabled(True)
        self.product_price.addItems([product['price'] for product in self.products if product['name'] == self.product_selected])
        # Atualizar o preço quando o produto selecionado mudar
        self.product_selection.currentTextChanged.connect(self.update_product_price)
        self.layout.addWidget(self.product_price)
    
    # Criar um método para atualizar o preço de acordo com o produto selecionado
    def update_product_price(self):
        self.product_selected = self.product_selection.currentText()
        self.product_price.clear()
        self.product_price.addItems([product['price'] for product in self.products if product['name'] == self.product_selected])
  
    # Criar um método para adicionar o produto selecionado na lista de produtos
    def create_add_product_button(self):
        self.add_product_button = QPushButton('Adicionar produto')
        self.add_product_button.clicked.connect(self.add_product)
        self.layout.addWidget(self.add_product_button)
        
    # Criar um método para mostrar os produtos selecionados na lista de produtos
    def create_product_table(self):
        self.product_table = QTableWidget()
        self.product_table.setColumnCount(4)
        self.product_table.setHorizontalHeaderLabels(['Produto', 'Quantidade', 'Preço', 'Remover'])
        self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.product_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.product_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.product_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.layout.addWidget(self.product_table)
    
    # Criar um método para mostrar o preço total dos produtos selecionados
    def create_total_price_label(self):
        self.total_price_label = QLabel('R$ 0,00')
        self.layout.addWidget(self.total_price_label)
        
    # Criar um método para remover o produto selecionado na lista de produtos
    def create_remove_product_button(self):
        self.remove_product_button = QPushButton('Remover produto')
        self.remove_product_button.clicked.connect(self.remove_product)
        self.layout.addWidget(self.remove_product_button)
    
    # Criar um método para finalizar a venda
    def create_finish_sale_button(self):
        self.finish_sale_button = QPushButton('Finalizar venda')
        self.finish_sale_button.clicked.connect(self.finish_sale)
        self.layout.addWidget(self.finish_sale_button)
    
    # Criar um método para cancelar a venda
    def create_cancel_sale_button(self):
        self.cancel_sale_button = QPushButton('Cancelar venda')
        self.cancel_sale_button.clicked.connect(self.cancel_sale)
        self.layout.addWidget(self.cancel_sale_button)
    
    # Criar um método para cancelar o produto selecionado na lista de produtos
    def create_cancel_product_button(self):
        self.cancel_product_button = QPushButton('Cancelar produto')
        self.cancel_product_button.clicked.connect(self.cancel_product)
        self.layout.addWidget(self.cancel_product_button)

    # Criar um método para adicionar o produto selecionado na lista de produtos
    def add_product(self):
        product = self.product_selection.currentText()
        quantity = self.quantity_selection.value()
        # Atualizar a quantidade se o produto já estiver na lista de produtos
        for row in range(self.product_table.rowCount()):
            if self.product_table.item(row, 0).text() == product:
                quantity += int(self.product_table.item(row, 1).text())
                self.product_table.removeRow(row)
                break
        # Atualizar o preço se o produto já estiver na lista de produtos
        price = self.product_price.currentText()
        price = float(price.replace('R$ ', '').replace(',', '.'))
        price *= quantity
        price = f'R$ {price:.2f}'.replace('.', ',')
        # Adicionar o produto na lista de produtos
        self.product_table.insertRow(self.product_table.rowCount())
        self.product_table.setItem(self.product_table.rowCount() - 1, 0, QTableWidgetItem(product))
        self.product_table.setItem(self.product_table.rowCount() - 1, 1, QTableWidgetItem(str(quantity)))
        self.product_table.setItem(self.product_table.rowCount() - 1, 2, QTableWidgetItem(price))
        self.product_table.setCellWidget(self.product_table.rowCount() - 1, 3, QPushButton('Remover'))
        self.product_table.cellWidget(self.product_table.rowCount() - 1, 3).clicked.connect(self.remove_product)
        self.update_total_price()
    
    # Criar um método para remover o produto selecionado na lista de produtos
    def remove_product(self):
        selected_row = self.product_table.currentRow()
        self.product_table.removeRow(selected_row)
        self.update_total_price()
    
    # Criar um método para atualizar o preço total dos produtos selecionados
    def update_total_price(self):
        total_price = 0
        for row in range(self.product_table.rowCount()):
            total_price += float(self.product_table.item(row, 2).text().replace('R$ ', '').replace(',', '.'))
        self.total_price_label.setText(f'R$ {total_price:.2f}')
    
    # Criar um método para finalizar a venda
    def finish_sale(self):
        self.product_table.setRowCount(0)
        self.update_total_price()
    
    # Criar um método para cancelar a venda
    def cancel_sale(self):
        self.product_table.setRowCount(0)
        self.update_total_price()
    
    # Criar um método para cancelar o produto selecionado na lista de produtos
    def cancel_product(self):
        self.product_table.setRowCount(0)
        self.update_total_price()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())