import math

from pyrogram.types import InlineKeyboardButton

from AnonXMusic.utils.formatters


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons



    buttons = [
        [
            InlineKeyboardButton(text="ᎡᎬՏႮᎷᎬ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ᏢᎪႮՏᎬ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="ᎬŃᎠ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [InlineKeyboardButton("𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙", url=f"https://t.me/Mvhmed")],
        [InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ⚡️", url=f"https://t.me/Gor_Genabot?startgroup=True")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="ᎡᎬՏႮᎷᎬ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ᏢᎪႮՏᎬ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="ᎬŃᎠ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton("𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙", url=f"https://t.me/Mvhmed")],
        [InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ⚡️", url=f"https://t.me/Gor_Genabot?startgroup=True")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
