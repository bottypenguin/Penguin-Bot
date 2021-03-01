###################################################
# DISCORD                                         #
###################################################
DEBUG_MODE = False
SPLIT_CHANNELS = False

SERVER_DEBUG_CHANNEL_ID = 809062902967435274 #log
SERVER_BUG_CHANNEL_ID = 809062936416878622 #bug reporting
SERVER_DISCORD_ID = 382153815073488898
SERVER_DISCORD_NAME = ''
SERVER_DISCORD_ICON = 'https://cdn.discordapp.com/avatars/808651447788240947/c63129c514d7cf1d1b6528969fcb06e6.png?size=1024'

BOT_DISCORD_ICON = SERVER_DISCORD_ICON

QUEUE_EMBED_ICON = ''
QUEUE_EMBED_TITLE = ''

BOT_DISCORD_ICON = SERVER_DISCORD_ICON
RS_ICON = '<:StarRedStar:512096841056124960>'

# CHANNEL IDs
SERVER_RS_CHANNEL_ID = 508782999093903373 #809062936416878622

###################################################
# TIME CONSTANTS (in sec)                         #
###################################################
TIME_BOT_AFK_TASK_RATE = 50
TIME_BOT_Q_TASK_RATE = 30

TIME_SPAM_BRAKE = 1
TIME_AFK_WARN = 60 * 10  # afk warning as ping; afk_flag set in checker task after warning!
TIME_AFK_KICK = 60 * 15  # kick if warning ignored. must be bigger than TIME_AFK_WARN!
TIME_Q_REPOST = 3
TIME_Q_REPOST_COOLDOWN = 1.2
MSG_DELETION_DELAY = 7
RULES_DELETION_DELAY = 60 * 3
HELP_DELETION_DELAY = 30
MSG_DISPLAY_TIME = 3
INFO_DISPLAY_TIME = 60 * 3 # An Empty Embedd, Meet Where
PING_COOLDOWN = 60 * 5  # time that has to pass before ping_all_role can be mentioned again

###################################################
# ROLES                                           #
###################################################
SUPPORTED_RS_LEVELS_MIN = 6
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

RS_ROLES = [RS4_ROLE, RS5_ROLE, RS6_ROLE, RS7_ROLE, RS8_ROLE, RS9_ROLE, RS10_ROLE, RS11_ROLE]

RESTRICTING_ROLES =  ['no4','no5','no6','no7','no8','no9','no10','no11'] # for players who can't make it in given RS level

SERVER_PING_ROLES = ['rs4','rs5','rs6','rs7','rs8','rs9','rs10','rs11'] # 1/4 2/4 3/4 4/4
SERVER_SOFT_PING_ROLES = SERVER_PING_ROLES
# ['rs4s','rs5s','rs6s','rs7s','rs8s','rs9s','rs10s','rs11s'] # 3/4 4/4
SERVER_SOFT_NO_ROLES = SERVER_PING_ROLES
# ['rs4n','rs5n','rs6n','rs7n','rs8n','rs9n','rs10n','rs11n'] # 4/4

OLD_STARS = {'RS6' : 214, 'RS7' : 320, 'RS8' : 1409, 'RS9' : 3131, 'RS10' : 10}

###################################################
# COMMAND ALIASES                                 #
###################################################
help_aliases = ['h', 'H', 'Help']

# RS
rs_help_aliases = ['rsh']
rs_aliases = ['rsc', 'Rs', 'rS', 'RS', 'RSC', 'Rsc']
rs_stats_aliases = ['st', 't']
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
EMBED_COLOR = 0x43b581
QUEUE_EMBED_COLOR = 0x2f3136

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
RS11_EMOJI = "⏸️"
# RS11_EMOJI = "<:eleven:760869824036601939>"
# RS11_EMOJI_ID = 760869824036601939

RS_EMOJIS =  [RS4_EMOJI, RS5_EMOJI, RS6_EMOJI, RS7_EMOJI, RS8_EMOJI, RS9_EMOJI, RS10_EMOJI, RS11_EMOJI]

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

TEXT_RULES_FORMAT = 'Text'
TEXT_RULES_TITLE = 'RS QUEUE ACCESS, TERMS OF SERVICE'

TEXT_RULES_EN = f"**1.Dont Grief** \
I think this goes without saying, when running RS runs with us, you shouldn't be doing it with the intent to disrupt anyones gameplay. \
\n\
2.**Cooperate With Everyone** \
This should be obvious as well. The game is designed to reward teamwork. To ensure the smoothest run possible, you must communicate with other players - members of the Penguin Horde or not. This means that: \n\
•You will ping planet sectors before engaging them, wait and listen for any concerns other players may express. Also, pay attention to the chat at all times. \
•Make sure you and your team pick planets centralised, that are accessible to everyone, and have enough artifacts to be worthwhile (unless you decide on otherwise). \
•If you have anything to suggest during the run, say it! This is about teamwork after all, and you are part of the team. \n\
•Try not to abandon the run, unless forced to of course by any unforeseen circumstances. \
3. **This service is for in-corp RS runs** \
This means that you will have to join a corporation of the Penguin Horde, that will be agreed upon by the member users. This rules do not apply to club runs hosted by Penguin Horde.\
\n\
4. **Be civil at all times** \
If you come to any disagreements with anyone during your RS run, before it or after it, please be civil. Anything can be solved with mature discussion. \
\n\
5. **If you break any of the above terms** \
Really, it depends on the severity of your action. There may not even be a warning, or you may even loose access to this service or get banned from the server overall. Know that you have absolutely nothing to worry about if all you plan on is getting some arts and enjoying a RS run with some good company. \
\n\
Now, i know some of you may have skipped down here to just find the command that will give you access without reading the above conditions. Please read them, so we dont have any misunderstandings. \n\
Anyways, use !agree to get access to the RS queue. \
If at any point you wish to no longer have access, use !leave. We are happy you are choosing to run Red Stars with us!"
TEXT_RULES = TEXT_RULES_EN

TEXT_NOROLESET = "you didn't select the"
TEXT_MEET_WERE = ''

# @zofia: careful with mobile version of discord!
# @BenSmith30: I think this is exactly what fits on mobile... No?
#+ DOWN_EMOJI +'Join.Unirse.Вступать.加入 Quit.Dejar.Уехать.退出'+ LEAVE_EMOJI

TEXT_FOOTER_TEXT = '\u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800 \u2800   \u2800' # Zofia' magic works on mobile and pc
