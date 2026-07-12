"""
This module contains the DefaultWindow class.

The DefaultWindow acts as the main container of the application.
Its primary responsibility is to organize the major UI components,
such as the Activity Bar, Sidebar, Editor, AI Chat, and Terminal.

Think of it as the "frame" of the entire IDE.

NOTE:
This class should NOT contain AI logic, file management,
or editor logic. Its job is simply to assemble the interface.
"""

# QWidget is used as the base widget that will occupy the center
# of the QMainWindow.
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QSplitter,
)

from ui.sidebar import Sidebar
from ui.editor import CodeEditor
from ui.chat_panel import AIChatPanel
from ui.terminal import TerminalPanel


class MainWindow(QMainWindow):
    """
    The main application window.

    QMainWindow is specifically designed for applications like:
    - IDEs
    - Text editors
    - Browsers
    - File managers

    It provides built-in support for:
        • Menu Bars
        • Tool Bars
        • Status Bars
        • Dock Widgets
        • A Central Widget

    Because we're building an AI Coding Assistant,
    QMainWindow is the perfect foundation.
    """

    def __init__(self):
        """
        Create the main window.

        This constructor is called once when the application starts.
        """

        # Always initialize the parent class first.
        super().__init__()

        # Configure the window.
        self.setup_window()

        # Create the widgets that will make up the interface.
        self.create_widgets()

        # Arrange the widgets on the screen.
        self.create_layout()

    # ---------------------------------------------------------
    # Window Configuration
    # ---------------------------------------------------------

    def setup_window(self):
        """
        Configure the appearance and basic properties
        of the main window.
        """

        # Window title shown in the title bar.
        self.setWindowTitle("Slash")

        # Initial size of the window.
        #
        # Users can still resize it afterwards.
        self.resize(1400, 850)

        # Prevent the window from becoming too small.
        self.setMinimumSize(1000, 600)

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def create_widgets(self):
        """
        Create the widgets used by the interface.
        """

        # QMainWindow does NOT directly use layouts.
        # Instead, it requires a central widget that will contain our layouts.
        self.central_widget = QWidget()

        # Tell QMainWindow to use this widget as the center of the application.
        self.setCentralWidget(self.central_widget)

        # Create the main UI panels.
        self.sidebar = Sidebar()
        self.editor = CodeEditor()
        self.chat_panel = AIChatPanel()
        self.terminal = TerminalPanel()

    # ---------------------------------------------------------
    # Layout Creation
    # ---------------------------------------------------------

    def create_layout(self):
        """
        Arrange the widgets inside the central widget.

        Later this layout will contain:
            Activity Bar
            Sidebar
            Editor
            AI Chat
        """

        top_splitter = QSplitter(Qt.Horizontal)
        top_splitter.addWidget(self.sidebar)
        top_splitter.addWidget(self.editor)
        top_splitter.addWidget(self.chat_panel)
        top_splitter.setHandleWidth(6)
        top_splitter.setChildrenCollapsible(False)
        top_splitter.setSizes([250, 900, 300])

        bottom_splitter = QSplitter(Qt.Vertical)
        bottom_splitter.addWidget(top_splitter)
        bottom_splitter.addWidget(self.terminal)
        bottom_splitter.setHandleWidth(6)
        bottom_splitter.setChildrenCollapsible(False)
        bottom_splitter.setSizes([650, 200])

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.addWidget(bottom_splitter)

        self.central_widget.setLayout(self.main_layout)