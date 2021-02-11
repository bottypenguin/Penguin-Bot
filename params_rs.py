###################################################
# DISCORD                                         #
###################################################
DEBUG_MODE = True
SERVER_DEBUG_CHANNEL_ID = 809062902967435274 #log
SERVER_BUG_CHANNEL_ID = 809062936416878622 #bug reporting
SERVER_DISCORD_ID = 382153815073488898
SERVER_DISCORD_NAME = "Penguin RS Hub"
SERVER_DISCORD_ICON = "https://cdn.discordapp.com/app-icons/808651447788240947/8015244e63042f89330c2a692d6e9e28.png?size=256"

BOT_DISCORD_ICON = SERVER_DISCORD_ICON
RS_ICON = '<:StarRedStar:512096841056124960>'

# CHANNEL IDs
SERVER_RS_CHANNEL_ID = 809062936416878622

###################################################
# TIME CONSTANTS (in sec)                         #
###################################################
TIME_BOT_AFK_TASK_RATE = 50
TIME_BOT_Q_TASK_RATE = 30

TIME_SPAM_BRAKE = 10
TIME_AFK_WARN = 60 * 10  # afk warning as ping; afk_flag set in checker task after warning!
TIME_AFK_KICK = 60 * 15  # kick if warning ignored. must be bigger than TIME_AFK_WARN!
TIME_Q_REPOST = 60
TIME_Q_REPOST_COOLDOWN = 1
MSG_DELETION_DELAY = 7
RULES_DELETION_DELAY = 60 * 3
MSG_DISPLAY_TIME = 3
INFO_DISPLAY_TIME = 60 * 5
PING_COOLDOWN = 60 * 5  # time that has to pass before ping_all_role can be mentioned again

###################################################
# ROLES                                           #
###################################################
SUPPORTED_RS_LEVELS_MIN = 8
SUPPORTED_RS_LEVELS_MAX = 10

SUPPORTED_RS_LEVELS = range(SUPPORTED_RS_LEVELS_MIN, SUPPORTED_RS_LEVELS_MAX + 1)

SERVER_MEMBER_ROLE = 'rs'
SERVER_MEMBER_ROLE_ID = 760976687068217375
SERVER_RS_ROLE_ID = SERVER_MEMBER_ROLE_ID

SERVER_MODERATOR_ROLE = 'interim officer'
SERVER_MODERATOR_ROLE_ID = 771906991140503574

SERVER_ADMIN_ROLES = 'admin'
SERVER_ADMIN_ROLE_ID = 418727225471270913

SERVER_MEMBER_ROLES = ['rs-access']
SERVER_ALLY_ROLES = ['rs-access']
SERVER_MODERATOR_ROLES = ['interim officer', 'Officer']
SERVER_ADMIN_ROLES = ['admin','Executive']

RS4_ROLE = 'RS4'
RS5_ROLE = 'RS5'
RS6_ROLE = 'RS6'
RS7_ROLE = 'RS7'
RS8_ROLE = 'RS8'
RS9_ROLE = 'RS9'
RS10_ROLE = 'RS10'
RS11_ROLE = 'RS11'

RS_ROLES = [RS6_ROLE, RS7_ROLE, RS8_ROLE, RS9_ROLE, RS10_ROLE]

RESTRICTING_ROLES =  ['no4','no5','no6','no7','no8','no9','no10','no11'] # for players who can't make it in given RS level

SERVER_PING_ROLES = ['rs4','rs5','rs6','rs7','rs8','rs9','rs10','rs11'] # 3/4 4/4
SERVER_SOFT_PING_ROLES = ['rs4s','rs5s','rs6s','rs7s','rs8s','rs9s','rs10s','rs11s'] # 3/4 4/4
SERVER_SOFT_NO_ROLES = ['rs4n','rs5n','rs6n','rs7n','rs8n','rs9n','rs10n','rs11n'] # 3/4 4/4


###################################################
# COMMAND ALIASES                                 #
###################################################
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
rs_clean_aliases = []

###################################################
# APPEARANCE                                      #
###################################################
EMBED_COLOR = 0xff6600
EMBED_QUEUE_COLOR = 0x2f3136

# rs emojis
RS0_EMOJI = "0️⃣"
RS1_EMOJI = "1️⃣"
RS2_EMOJI = "2️⃣"
RS3_EMOJI = "3️⃣"
RS4_EMOJI = "4️⃣"
RS5_EMOJI = "5️⃣"
RS6_EMOJI = "6️⃣"
RS7_EMOJI = "7️⃣"
RS8_EMOJI = "8️⃣"
RS9_EMOJI = "9️⃣"
RS10_EMOJI = "🔟"
RS11_EMOJI = "<:eleven:760869824036601939>"
RS11_EMOJI_ID = 760869824036601939

RS_EMOJIS =  [RS6_EMOJI, RS7_EMOJI, RS8_EMOJI, RS9_EMOJI, RS10_EMOJI]

# dialogues
JOIN_EMOJI = "🆕"
LEAVE_EMOJI = "❎"
START_EMOJI = "▶"
CONFIRM_EMOJI = "✅"
CANCEL_EMOJI = "❎"
GO_BACK_EMOJI = "🔙"
DOWN_EMOJI = "⬇" 

PING_THRESHOLDS = [1, 2, 3] # ping at these queue sizes only

MAX_RS_NOTE_LENGTH = 50

MAX_RS_NOTE_LENGTH = 50

MAX_RS_NOTE_LENGTH = 50

MAX_RS_NOTE_LENGTH = 50

# TEXTS 

RULES_CHANNEL_ID = 525599595812880384
RULES_MESSAGE_ID = 574195487171805333
RULES_MESSAGE_ID2 = 574195496835350528
RULES_MESSAGE_ID_FR = 805569774822096916

TEXT_EMPTY_QUEUE = 'Start a new queue by typing `!in` or reacting below!\n' \
                                'Questions? `!help`, Hide/Restore channel: `!rs`\n' \
                                f'Bugs or Ideas? Please report them in '

TEXT_RULES_TITLE = 'RS Rules'

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
TEXT_FOOTER_TEXT = '\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f' #this is a stupid Zofia's hack to keep the minimal width od embedd sensible
