import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie

class JarvisUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """ Initialize the user interface """
        # Set window title and initial size to 1000x1000 pixels
        self.setWindowTitle('Jarvis UI')
        self.setGeometry(100, 100, 2450, 1400)  # Set window size to 1000x1000 pixels

        # Set window transparency and remove borders
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Create a label for displaying the GIF
        self.mic_label = QLabel(self)
        gif_path = r"C:\Users\Admin\Desktop\J.A.R.V.I.S\ui2.gif"  # Ensure this path is correct
        self.add_gif_to_label(self.mic_label, gif_path)

        # Create a vertical layout and add the label (GIF)
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.mic_label, alignment=Qt.AlignCenter)

        # Set layout margins and spacing to ensure center alignment
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Set the layout to the window
        self.setLayout(main_layout)

        # Show the window
        self.show()

        # Set up mouse click event on the GIF label (optional)
        self.mic_label.mousePressEvent = self.start_listening

    def add_gif_to_label(self, label, gif_path):
        """ Load a GIF into the QLabel """
        print(f"Attempting to load GIF from path: {gif_path}")  # Debugging line
        if not os.path.exists(gif_path):
            print(f"Error: GIF not found at path {gif_path}")
            return

        movie = QMovie(gif_path)
        if not movie.isValid():
            print(f"Error: GIF {gif_path} is not valid.")
            return

        # Make sure the GIF fits within the window size without distortion
        label.setMovie(movie)
        movie.start()
        label.setAlignment(Qt.AlignCenter)

        # Set the label size based on the movie size (dynamic sizing)
        label.resize(movie.currentImage().width(), movie.currentImage().height())
        print(f"GIF loaded successfully!")  # Debugging line

    def start_listening(self, event):
        """ Placeholder for future action on click (e.g., Jarvis activation) """
        print("You clicked the GIF!")  # Debugging line for click event

def run_jarvis_ui():
    """ Run the main application to display the UI """
    app = QApplication([])

    # Create and display the Jarvis UI
    jarvis_ui = JarvisUI()
    app.exec_()

if __name__ == '__main__':
    run_jarvis_ui()
