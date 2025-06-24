from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
import EncryptionModule
import os, sys, ctypes

# TODO:
# - ADD a way to manually select key file/path to create key file in.
# - ADD possibility to encrypt movie files. 
# - FIX UI for MacOS X.

# App ID for the taskpar icon (Windows)
app_id = 'File Encrypter'
if sys.platform == 'win32':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

fernet = EncryptionModule.select_key_file('file-encrypter.key')

# Window class
class MainWindow(QMainWindow):

    # Constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Encrypter")
        self.setGeometry(100, 100, 400, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('./assets/icon.png'))
        self.setStyleSheet("background-image: url(./assets/main_bg.jpg);")

        self.initUI()

    # Initialize the UI
    def initUI(self):
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        
        self.filepath_label = QLabel("Enter filepath:", self)
        self.filepath_label.setFont(QFont('Arial', 12))
        self.filepath_label.setStyleSheet("color: white;")
        self.layout.addWidget(self.filepath_label)

        self.filepath = QLineEdit(self)
        self.filepath.setFont(QFont('Arial', 12))
        self.filepath.setGeometry(150, 15, 200, 30)
        self.filepath.setStyleSheet("color: white;")
        self.layout.addWidget(self.filepath)

        self.select_button = QPushButton("Select file", self)
        self.select_button.setFont(QFont('Arial', 12))
        self.select_button.setStyleSheet("color: white;")
        self.select_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.select_button)

        self.select_directory_button = QPushButton("Select directory", self)
        self.select_directory_button.setFont(QFont('Arial', 12))
        self.select_directory_button.setStyleSheet("color: white;")
        self.select_directory_button.clicked.connect(self.select_directory)
        self.layout.addWidget(self.select_directory_button)

        self.encrypt_button = QPushButton("Encrypt", self)
        self.encrypt_button.setFont(QFont('Arial', 12))
        self.encrypt_button.setStyleSheet("color: white;")
        self.encrypt_button.clicked.connect(self.encrypt)
        self.layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton("Decrypt", self)
        self.decrypt_button.setFont(QFont('Arial', 12))
        self.decrypt_button.setStyleSheet("color: white;")
        self.decrypt_button.clicked.connect(self.decrypt)
        self.layout.addWidget(self.decrypt_button)


    # Select file
    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filetypes = "All files (*.*);;Image files (*.png *.jpg *.jpeg *.gif *.bmp *.tiff *.webp);;Text files (*.txt *.docx *.doc *.pdf *.rtf *.odt *.html *.xml *.csv *.json *.log *.md *.tex *.yaml *.yml *.ini *.cfg *.conf *.properties *.env *.sh *.bat *.cmd *.ps1 *.psm1 *.psd1 *.ps1xml *.pssc *.psc1)"
        filepath_select, _ = QFileDialog.getOpenFileName(self, "Select file", "", filetypes, options=options)
        if filepath_select:
            print("Selected file:", filepath_select)
            self.filepath.setText(filepath_select)
        else:
            print("No file selected.")

    # Select directory
    def select_directory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self, "Select directory", "", options=options)
        if directory:
            print("Selected directory:", directory)
            self.filepath.setText(directory)
        else:
            print("No directory selected.")

    # Encrypt
    def encrypt(self):
        filepath = self.filepath.text()
        if filepath:
            if os.path.isdir(filepath):
                EncryptionModule.encrypt_directory(filepath, fernet)
            else:
                EncryptionModule.encrypt_file(filepath, fernet)
        else:
            print("No file selected.")
    
    # Decrypt
    def decrypt(self):
        filepath = self.filepath.text()
        if filepath:
            if os.path.isdir(filepath):
                EncryptionModule.decrypt_directory(filepath, fernet)
            else:
                EncryptionModule.decrypt_file(filepath, fernet)
        else:
            print("No file selected.")

def Main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Main()