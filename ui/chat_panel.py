"""
This module contains the AIChatPanel class.

The AIChatPanel provides the interface for interacting with the
AI Coding Assistant.

Responsibilities:
    • Display the conversation.
    • Receive user prompts.
    • Display AI responses.

This class is ONLY responsible for the user interface.

It should NOT:
    • Call AI models.
    • Load model files.
    • Build prompts.
    • Manage conversation memory.

Those responsibilities belong to the ai package.
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QTextBrowser,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class AIChatPanel(QWidget):
    """
    AI Assistant panel.

    This widget provides a chat interface similar to
    ChatGPT, Claude, Cursor, or Copilot Chat.

    It contains:

        • Conversation history
        • Prompt input
        • Send button

    Future versions may also include:

        • Stop Generation
        • Attach File
        • Model Selector
        • New Chat
        • Clear Conversation
    """

    def __init__(self):
        """Initialize the chat panel."""

        super().__init__()

        self.setup_panel()
        self.create_widgets()
        self.create_layout()

    # ---------------------------------------------------------
    # Panel Configuration
    # ---------------------------------------------------------

    def setup_panel(self):
        """
        Configure the appearance of the chat panel.
        """

        # Fixed width keeps the layout balanced.
        # Later, this can become resizable with a splitter.
        self.setFixedWidth(350)

        self.setStyleSheet("""
            QWidget {
                background-color: #252526;
                color: #D4D4D4;
            }

            QLabel {
                font-size: 11pt;
                font-weight: bold;
                padding: 8px;
            }

            QTextBrowser {
                background-color: #1E1E1E;
                border: none;
                padding: 10px;
            }

            QTextEdit {
                background-color: #1E1E1E;
                border: 1px solid #3C3C3C;
                padding: 8px;
            }

            QPushButton {
                background-color: #007ACC;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
            }

            QPushButton:hover {
                background-color: #1493FF;
            }

            QPushButton:pressed {
                background-color: #005A9E;
            }
        """)

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def create_widgets(self):
        """
        Create all widgets used by the chat panel.
        """

        # Panel title.
        self.title_label = QLabel("AI ASSISTANT")

        # Displays the conversation.
        #
        # QTextBrowser is perfect because it supports
        # formatted text while remaining read-only.
        self.chat_history = QTextBrowser()

        self.chat_history.setFont(QFont("Segoe UI", 10))

        self.chat_history.setPlaceholderText(
            "Start a conversation with your AI assistant..."
        )

        # Prompt input.
        #
        # QTextEdit is used instead of QLineEdit because
        # prompts can span multiple lines.
        self.prompt_input = QTextEdit()

        self.prompt_input.setPlaceholderText(
            "Ask anything about your project..."
        )

        self.prompt_input.setFixedHeight(90)

        # Send button.
        #
        # Later this will be connected to the AI agent.
        self.send_button = QPushButton("Send")

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def create_layout(self):
        """
        Arrange all widgets.
        """

        # Horizontal layout for the prompt area.
        input_layout = QHBoxLayout()

        input_layout.addWidget(self.prompt_input)
        input_layout.addWidget(self.send_button)

        # Main vertical layout.
        self.layout = QVBoxLayout()

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.chat_history)
        self.layout.addLayout(input_layout)

        self.setLayout(self.layout)

    # ---------------------------------------------------------
    # Public Methods
    # ---------------------------------------------------------

    def add_user_message(self, message: str):
        """
        Display a user message.
        """

        self.chat_history.append(
            f"<b>You:</b><br>{message}<br><br>"
        )

    def add_ai_message(self, message: str):
        """
        Display an AI response.
        """

        self.chat_history.append(
            f"<b>AI:</b><br>{message}<br><br>"
        )

    def get_prompt(self) -> str:
        """
        Return the current prompt entered by the user.
        """

        return self.prompt_input.toPlainText()

    def clear_prompt(self):
        """
        Clear the prompt input box.
        """

        self.prompt_input.clear()

    def clear_chat(self):
        """
        Remove the entire conversation.
        """

        self.chat_history.clear()