# import os
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QMovie

# class GifDisplayUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         """ Initialize the user interface """
#         # Set window title and transparency settings
#         self.setWindowTitle('GIF Display')
#         self.setGeometry(100, 100, 800, 600)

#         # Set window transparency and remove borders
#         self.setAttribute(Qt.WA_TranslucentBackground)
#         self.setWindowFlag(Qt.FramelessWindowHint)

#         # Create a label to display the GIF
#         self.gif_label = QLabel(self)

#         # Specify the path to your GIF
#         gif_path = r"C:\Users\Admin\Desktop\J.A.R.V.I.S\ui2.gif"  # Update this path

#         # Add the GIF to the label
#         self.add_gif_to_label(self.gif_label, gif_path)

#         # Create a vertical layout and add the label (GIF)
#         main_layout = QVBoxLayout(self)
#         main_layout.addWidget(self.gif_label, alignment=Qt.AlignCenter)

#         # Set layout margins and spacing
#         main_layout.setContentsMargins(0, 0, 0, 0)
#         main_layout.setSpacing(0)

#         # Show the window in full-screen mode
#         self.showFullScreen()

#     def add_gif_to_label(self, label, gif_path):
#         """ Load a GIF into the QLabel """
#         print(f"Attempting to load GIF from path: {gif_path}")  # Debugging line
#         if not os.path.exists(gif_path):
#             print(f"Error: GIF not found at path {gif_path}")
#             return

#         movie = QMovie(gif_path)
#         if not movie.isValid():
#             print(f"Error: GIF {gif_path} is not valid.")
#             return

#         label.setMovie(movie)
#         movie.start()
#         label.setAlignment(Qt.AlignCenter)
#         print(f"GIF loaded successfully!")  # Debugging line

# def run_gif_display_ui():
#     """ Run the main application to display the UI """
#     app = QApplication([])

#     # Create and display the GifDisplayUI
#     gif_display_ui = GifDisplayUI()
#     app.exec_()

# if __name__ == '__main__':
#     run_gif_display_ui()











import os
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
 # Import your jarvis.py file

class GifDisplayUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """ Initialize the user interface """
        # Set window title and transparency settings
        self.setWindowTitle('GIF Display')
        self.setGeometry(100, 100, 800, 600)

        # Set window transparency and remove borders
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Create a label to display the GIF
        self.gif_label = QLabel(self)

        # Specify the path to your GIF
        gif_path = r"C:\Users\Admin\Desktop\J.A.R.V.I.S\ui2.gif"  # Update this path

        # Add the GIF to the label
        self.add_gif_to_label(self.gif_label, gif_path)

        # Create a vertical layout and add the label (GIF)
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.gif_label, alignment=Qt.AlignCenter)

        # Set layout margins and spacing
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Show the window in full-screen mode
        self.showFullScreen()

    def add_gif_to_label(self, label, gif_path):
        """ Load a GIF into the QLabel """
        if not os.path.exists(gif_path):
            print(f"Error: GIF not found at path {gif_path}")
            return

        self.movie = QMovie(gif_path)
        if not self.movie.isValid():
            print(f"Error: GIF {gif_path} is not valid.")
            return

        label.setMovie(self.movie)
        self.movie.start()
        label.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        """ Handle mouse click event and run jarvis function in a new thread """

        # Create and start a new thread to run the function from jarvis.py
        threading.Thread(target=self.run_jarvis_function).start()

    def run_jarvis_function(self):
        """ Run the function from jarvis.py in a separate thread """
        print("Starting Bujji your own virtual assistant")
        import jarvis
        jarvis.start_jarvis_logic()  # Call the function from jarvis.py
        print("Jarvis function has finished.")

def run_gif_display_ui():
    """ Run the main application to display the UI """
    app = QApplication([])

    # Create and display the GifDisplayUI
    gif_display_ui = GifDisplayUI()
    app.exec_()

if __name__ == '__main__':
    run_gif_display_ui()







