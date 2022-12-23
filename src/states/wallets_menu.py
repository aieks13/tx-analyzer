from aiogram.dispatcher.filters.state import StatesGroup, State


class WalletsMenu(StatesGroup):
    main = State()
    management = State()


class AddWalletAddress(StatesGroup):
    input_address = State()
    set_label = State()
