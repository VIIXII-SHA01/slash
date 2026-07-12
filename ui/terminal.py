"""
This module contains the TerminalPanel class.

The TerminalPanel is responsible for displaying an integrated
terminal inside the IDE.

Responsibilities:
    • Display terminal output.
    • Receive user commands.
    • Show command history.

Responsibilities that DO NOT belong here:
    • Running Python scripts
    • Managing processes
    • Handling Git commands
    • Building projects

Those tasks will later be handled by QProcess or another
process manager.
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPlainTextEdit,
    QLineEdit,
    QVBoxLayout,
)


class TerminalPanel(QWidget):
    """
    Integrated terminal panel.

    This widget provides a simple terminal interface similar
    to the terminal found in VS Code.

    For now it is only a visual component.

    Later it will communicate with:
        • PowerShell (Windows)
        • CMD (Windows)
        • Bash (Linux)
        • Zsh (macOS)

    using QProcess.
    """

    def __init__(self):
        """Initialize the terminal panel."""

        super().__init__()

        self.setup_terminal()
        self.create_widgets()
        self.create_layout()

    # ---------------------------------------------------------
    # Terminal Configuration
    # ---------------------------------------------------------

    def setup_terminal(self):
        """
        Configure the appearance of the terminal panel.
        """

        # The terminal will usually be displayed
        # at the bottom of the IDE.
        self.setMinimumHeight(180)

        self.setStyleSheet("""
            QWidget {
                background-color: #1E1E1E;
                color: #D4D4D4;
            }

            QLabel {
                font-size: 10pt;
                font-weight: bold;
                padding: 8px;
            }

            QPlainTextEdit {
                background-color: #181818;
                border: none;
                color: #D4D4D4;
                padding: 8px;
            }

            QLineEdit {
                background-color: #252526;
                border: 1px solid #3C3C3C;
                padding: 6px;
                color: white;
            }
        """)

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def create_widgets(self):
        """
        Create the widgets used by the terminal.
        """

        # Terminal title.
        self.title_label = QLabel("TERMINAL")

        # Displays terminal output.
        #
        # QPlainTextEdit is used because terminal output
        # is plain text and can become very large.
        self.output = QPlainTextEdit()

        # Users should not edit previous output.
        self.output.setReadOnly(True)

        # A monospace font is important for terminal output.
        font = QFont("Consolas", 10)
        self.output.setFont(font)

        # Placeholder text.
        self.output.setPlaceholderText(
            "Terminal output will appear here..."
        )

        # Command input.
        #
        # Later, pressing Enter will send the command
        # to a QProcess.
        self.command_input = QLineEdit()

        self.command_input.setPlaceholderText(
            "Enter a command..."
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def create_layout(self):
        """
        Arrange the terminal widgets vertically.
        """

        self.layout = QVBoxLayout()

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(5)

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.output)
        self.layout.addWidget(self.command_input)

        self.setLayout(self.layout)

    # ---------------------------------------------------------
    # Public Methods
    # ---------------------------------------------------------

    def append_output(self, text: str):
        """
        Add text to the terminal output.

        Parameters
        ----------
        text : str
            The text to display.
        """

        self.output.appendPlainText(text)

    def clear_terminal(self):
        """
        Remove all terminal output.
        """

        self.output.clear()

    def get_command(self) -> str:
        """
        Return the current command entered by the user.

        Returns
        -------
        str
            The command in the input field.
        """

        return self.command_input.text()

    def clear_command(self):
        """
        Clear the command input field.
        """

        self.command_input.clear()