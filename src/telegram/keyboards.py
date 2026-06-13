from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard(is_superuser: bool = False) -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="📝 Add Transaction")],
        [
            KeyboardButton(text="📊 Report"),
            KeyboardButton(text="⚖️ Balance"),
        ],
    ]

    if is_superuser:
        buttons.append([KeyboardButton(text="⚙️ Settings")])

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
    )
