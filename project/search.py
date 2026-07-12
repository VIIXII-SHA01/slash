"""Entry point for the AI Coding Assistant.

Responsibilities:
- Create the QApplication object.
- Create the main application window.
- Start Qt's event loop.
"""

# sys is used to access command-line arguments and to properly exit the application.
import sys

# QApplication is the foundation of every Qt application.
# It manages the application's event loop, styling, clipboard,
# keyboard events, mouse events, and much more.
from PySide6.QtWidgets import QApplication

# Import the main window of our application.
# The MainWindow class will contain the overall UI layout.
from ui.main_window import MainWindow

class Slash:
    """
    Controls the lifecycle of the application.

    Think of this class as the application's manager.
    It is responsible for creating the QApplication,
    creating the main window, and starting the program.
    """

    def __init__(self):
        """
        Initialize the application.

        This method runs only once when the application starts.
        """

        # Create the QApplication object.
        #
        # IMPORTANT:
        # Every PySide6 application must have exactly ONE QApplication.
        # Without it, no windows can be displayed.
        self.app = QApplication(sys.argv)

        # Create the main window.
        #
        # At this point the window exists in memory,
        # but it is NOT visible yet.
        self.window = MainWindow()

    def run(self):
        """
        Start the application.
        """

        # Display the main window.
        self.window.show()

        # Start Qt's event loop.
        #
        # The event loop waits for:
        # - Mouse clicks
        # - Keyboard input
        # - Window resizing
        # - Timer events
        # - Signals and slots
        #
        # Without this line, the application would immediately close.
        sys.exit(self.app.exec())


# This condition ensures that the application starts
# only when this file is executed directly.
#
# If another file imports main.py,
# the code below will NOT execute.
if __name__ == "__main__":
    app = Slash()
    app.run()