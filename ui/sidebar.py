"""
This module contains the Sidebar class.

The Sidebar is responsible for displaying secondary panels,
such as:

    • Explorer
    • Search
    • AI Files
    • Project Structure

Think of the Sidebar as the navigation area of the IDE.

NOTE:
The Sidebar does NOT perform file operations.
Its responsibility is only to display information.

File loading, searching, and project management belong
to classes inside the project package.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QListWidget,
)


class Sidebar(QWidget):
    """
    Sidebar panel.

    This widget occupies the left side of the IDE
    (next to the Activity Bar).

    Initially, it contains a simple Explorer.
    Later it can be expanded to include:

        • Search
        • Git
        • AI History
        • Symbols
        • Outline
    """

    def __init__(self):
        """Initialize the sidebar."""

        super().__init__()

        self.setup_sidebar()
        self.create_widgets()
        self.create_layout()

    # ---------------------------------------------------------
    # Sidebar Configuration
    # ---------------------------------------------------------

    def setup_sidebar(self):
        """
        Configure the appearance of the sidebar.
        """

        # A fixed width keeps the layout predictable.
        # Users can resize it later using a splitter.
        self.setFixedWidth(250)

        # Apply a VS Code-inspired dark theme.
        self.setStyleSheet("""
            QWidget {
                background-color: #252526;
                color: #CCCCCC;
            }

            QLabel {
                font-size: 11pt;
                font-weight: bold;
                padding-left: 10px;
                padding-top: 10px;
            }

            QListWidget {
                border: none;
                background-color: transparent;
                padding: 5px;
            }

            QListWidget::item {
                padding: 6px;
                border-radius: 4px;
            }

            QListWidget::item:selected {
                background-color: #37373D;
            }

            QListWidget::item:hover {
                background-color: #2A2D2E;
            }
        """)

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def create_widgets(self):
        """
        Create all widgets used by the sidebar.
        """

        # Sidebar title.
        self.title_label = QLabel("EXPLORER")

        # Simple file list.
        #
        # Later this will become a QFileSystemModel
        # displayed in a QTreeView.
        self.file_list = QListWidget()

        # Temporary placeholder items.
        self.file_list.addItems([
            "main.py",
            "ui/",
            "ai/",
            "project/",
            "assets/"
        ])

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def create_layout(self):
        """
        Arrange the widgets vertically.
        """

        self.layout = QVBoxLayout()

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(8)

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.file_list)

        self.setLayout(self.layout)