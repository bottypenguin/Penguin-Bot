########################################################################################################################
# DISCORD
########################################################################################################################
DEBUG_MODE = False
SERVER_DEBUG_CHANNEL_ID = 806307634000166922 #log
SERVER_BUG_CHANNEL_ID = 808499006510596166 #bug reporting
SERVER_DISCORD_ID = 760481068959662081
SERVER_DISCORD_NAME = "RS Club"
SERVER_DISCORD_ICON = "https://cdn.discordapp.com/icons/760481068959662081/12ed9c2aa500b992332a630dac7d101d.png?size=128"
BOT_DISCORD_ICON = SERVER_DISCORD_ICON
RS_ICON = '<:redstar:807239811068329985>'

# CHANNEL IDs
SERVER_RS_CHANNEL_ID = 806307789147602994 if DEBUG_MODE is False else SERVER_DEBUG_CHANNEL_ID

RS_CHANNELS = {
'rs4': 807270877011116113,
'rs5': 807270800583163975,
'rs6': 760481958928187442,
'rs7': 760481915622260767,
'rs8': 760481821531701309,
'rs9': 760481766179340288,
'rs10': 760481703071973388,
'rs11': 760481388440453190
}


########################################################################################################################
# TIME CONSTANTS (in sec)
########################################################################################################################
TIME_BOT_AFK_TASK_RATE = 50
TIME_BOT_Q_TASK_RATE = 30

TIME_SPAM_BRAKE = 0.1
TIME_AFK_WARN = 60 * 30  # afk warning as ping; afk_flag set in checker task after warning!
TIME_AFK_KICK = 60 * 35  # kick if warning ignored. must be bigger than TIME_AFK_WARN!
TIME_Q_REPOST = 60 * 15
TIME_Q_REPOST_COOLDOWN = 0
MSG_DELETION_DELAY = 0.1
MSG_DISPLAY_TIME = 15
INFO_DISPLAY_TIME = 60 * 5
PING_COOLDOWN = 60 * 5  # time that has to pass before ping_all_role can be mentioned again

SERVER_MEMBER_ROLE = 'rs'
SERVER_MEMBER_ROLE_ID = 760976687068217375

SERVER_MEMBER_ROLES = ['rs']
SERVER_ALLY_ROLES = ['rs']

SERVER_RS_ROLE_ID = SERVER_MEMBER_ROLE

# COMMAND ALIASES

help_aliases = ['h', 'H', 'Help']

# RS
rs_help_aliases = ['rsh']
rs_aliases = ['rsc', 'Rs', 'rS', 'RS', 'RSC', 'Rsc']
rs_stats_aliases = []
rs_rules_aliases = ['r', 'rsr', 'rsrule', 'rule', 'rules']
display_queue_aliases = ['q', 'Q', 'queue', 'Queue']
enter_queue_aliases = ['i', 'I', 'in', 'In', 'IN', 'iN', 'join', 'Join']
leave_queue_aliases = ['o', 'O', 'out', 'Out', 'OUT']
start_queue_aliases = ['s', 'S', 'Start']
clear_queue_aliases = ['c', 'C', 'Clear']

# APPEARANCE

EMBED_COLOR = 0xff6600
EMBED_QUEUE_COLOR = 0x2f3136

# rs
RS0_EMOJI = "0️⃣"
RS0_ROLE = "rs0"
RS1_EMOJI = "1️⃣"
RS1_ROLE = "rs1"
RS2_EMOJI = "2️⃣"
RS2_ROLE = "rs2"
RS3_EMOJI = "3️⃣"
RS3_ROLE = "rs3"
RS4_EMOJI = "4️⃣"
RS4_ROLE = "rs4"
RS5_EMOJI = "5️⃣"
RS5_ROLE = "rs5"
RS6_EMOJI = "6️⃣"
RS6_ROLE = "rs6"
RS7_EMOJI = "7️⃣"
RS7_ROLE = "rs7"
RS8_EMOJI = "8️⃣"
RS8_ROLE = "rs8"
RS9_EMOJI = "9️⃣"
RS9_ROLE = "rs9"
RS10_EMOJI = "🔟"
RS10_ROLE = "rs10"
RS11_EMOJI = "<:eleven:760869824036601939>"
RS11_EMOJI_ID = 760869824036601939
RS11_ROLE = "rs11"

# dialogues
JOIN_EMOJI = "🆕"
LEAVE_EMOJI = "❎"
START_EMOJI = "▶"
CONFIRM_EMOJI = "✅"
CANCEL_EMOJI = "❎"
GO_BACK_EMOJI = "🔙"
DOWN_EMOJI = "⬇" 

PING_THRESHOLDS = [1, 2, 3] # ping at these queue sizes only
SUPPORTED_RS_LEVELS = range(8, 12)      # rs4:11
MAX_RS_NOTE_LENGTH = 50

# TEXTS 

RULES_CHANNEL_ID = 805568314998784002
RULES_MESSAGE_ID = 805569774822096916
RULES_MESSAGE_ID_FR = 805569774822096916

TEXT_EMPTY_QUEUE = 'Start a new queue by typing `!in` or reacting below!\n' \
                                'Questions? `!help`, Hide/Restore channel: `!rs`\n' \
                                f'Bugs or Ideas? Please report them in '

TEXT_RULES_EN = f'Don’t be a…\n' \
           f'**`D`**oes not communicate.\n' \
           f'**`I`**s unaware of teammates\' builds and strategies.\n' \
           f'**`C`**lears without focusing planet sectors.\n' \
           f'**`K`**ills teammates with thoughtless play.'
TEXT_RULES = TEXT_RULES_EN

# @zofia: careful with mobile version of discord!
# @BenSmith30: I think this is exactly what fits on mobile... No?
#TEXT_FOOTER_TEXT = '___________________________________________________\n' \
#+ DOWN_EMOJI +'Join.Unirse.Вступать.加入 Quit.Dejar.Уехать.退出'+ LEAVE_EMOJI
TEXT_FOOTER_TEXT = '\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f'