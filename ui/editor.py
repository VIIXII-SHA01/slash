"""
This module contains the CodeEditor class.

The CodeEditor is responsible for displaying and editing source code.

For now, this class provides the basic functionality of a text editor.
Later we will extend it with features such as:

    • Line numbers
    • Syntax highlighting
    • Auto indentation
    • Bracket matching
    • Auto completion
    • Current line highlighting
    • Find & Replace
    • Code folding

By keeping this class focused on editing text, it becomes much easier
to maintain and extend.
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPlainTextEdit


class CodeEditor(QPlainTextEdit):
    """
    A custom code editor.

    QPlainTextEdit is preferred over QTextEdit for source code because:

    • It is optimized for plain text.
    • It performs much better with large files.
    • It uses less memory.
    • Most professional code editors use a plain text model.

    This class will eventually become the heart of the IDE.
    """

    def __init__(self):
        """Initialize the code editor."""

        # Initialize the parent class first.
        super().__init__()

        # Configure the editor.
        self.setup_editor()

    # ---------------------------------------------------------
    # Editor Configuration
    # ---------------------------------------------------------

    def setup_editor(self):
        """
        Configure the appearance and behavior of the editor.
        """

        # ---------------------------------------------
        # Font
        # ---------------------------------------------
        #
        # Monospaced fonts are essential for programming.
        # Every character occupies the same width,
        # making code easier to read.
        #
        # Consolas is available on Windows.
        # On Linux or macOS, Qt will automatically use
        # a suitable fallback if it's unavailable.
        font = QFont("Consolas", 11)
        self.setFont(font)

        # ---------------------------------------------
        # Tabs
        # ---------------------------------------------
        #
        # Make the Tab key insert four spaces worth of width.
        # This only affects the visual width of a tab character.
        self.setTabStopDistance(40)

        # ---------------------------------------------
        # Line Wrapping
        # ---------------------------------------------
        #
        # Code editors generally do NOT wrap long lines.
        # Instead, users scroll horizontally.
        self.setLineWrapMode(QPlainTextEdit.NoWrap)

        # ---------------------------------------------
        # Cursor Width
        # ---------------------------------------------
        #
        # Make the text cursor slightly thicker so it's
        # easier to see.
        self.setCursorWidth(2)

        # ---------------------------------------------
        # Placeholder Text
        # ---------------------------------------------
        #
        # Display a helpful message when no file is open.
        self.setPlaceholderText(
            "Open a file or start typing..."
        )

        # ---------------------------------------------
        # Style Sheet
        # ---------------------------------------------
        #
        # Apply a VS Code-inspired dark appearance.
        #
        # We'll eventually move this into a dedicated
        # theme manager, but keeping it here is fine
        # while we're building the layout.
        self.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1E1E1E;
                color: #D4D4D4;

                border: none;

                selection-background-color: #264F78;
                selection-color: white;

                padding: 10px;

                font-size: 11pt;
            }
        """)

    # ---------------------------------------------------------
    # Public Methods
    # ---------------------------------------------------------

    def clear_editor(self):
        """
        Clear all text from the editor.
        """

        self.clear()

    def set_code(self, text: str):
        """
        Replace the current document with new code.

        Parameters
        ----------
        text : str
            The source code to display.
        """

        self.setPlainText(text)

    def get_code(self) -> str:
        """
        Return the entire contents of the editor.

        Returns
        -------
        str
            The current source code.
        """

        return self.toPlainText()