from aiogram.fsm.state import (
    StatesGroup,
    State,
)


class PremiumState(StatesGroup):

    waiting_details = State()