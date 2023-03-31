import openai
import readline
import os

print("                                                                                                                                                ")
print("        CCCCCCCCCCCCChhhhhhh                                       tttt                 GGGGGGGGGGGGGPPPPPPPPPPPPPPPPP   TTTTTTTTTTTTTTTTTTTTTTT")
print("     CCC::::::::::::Ch:::::h                                    ttt:::t              GGG::::::::::::GP::::::::::::::::P  T:::::::::::::::::::::T")
print("   CC:::::::::::::::Ch:::::h                                    t:::::t            GG:::::::::::::::GP::::::PPPPPP:::::P T:::::::::::::::::::::T")
print("  C:::::CCCCCCCC::::Ch:::::h                                    t:::::t           G:::::GGGGGGGG::::GPP:::::P     P:::::PT:::::TT:::::::TT:::::T")
print(" C:::::C       CCCCCC h::::h hhhhh         aaaaaaaaaaaaa  ttttttt:::::tttttt    G:::::G       GGGGGG  P::::P     P:::::PTTTTTT  T:::::T  TTTTTT")
print("C:::::C               h::::hh:::::hhh      a::::::::::::a t:::::::::::::::::t   G:::::G                P::::P     P:::::P        T:::::T        ")
print("C:::::C               h::::::::::::::hh    aaaaaaaaa:::::at:::::::::::::::::t   G:::::G                P::::PPPPPP:::::P         T:::::T        ")
print("C:::::C               h:::::::hhh::::::h            a::::atttttt:::::::tttttt   G:::::G    GGGGGGGGGG  P:::::::::::::PP          T:::::T        ")
print("C:::::C               h::::::h   h::::::h    aaaaaaa:::::a      t:::::t         G:::::G    G::::::::G  P::::PPPPPPPPP            T:::::T        ")
print("C:::::C               h:::::h     h:::::h  aa::::::::::::a      t:::::t         G:::::G    GGGGG::::G  P::::P                    T:::::T        ")
print("C:::::C               h:::::h     h:::::h a::::aaaa::::::a      t:::::t         G:::::G        G::::G  P::::P                    T:::::T        ")
print(" C:::::C       CCCCCC h:::::h     h:::::ha::::a    a:::::a      t:::::t    ttttttG:::::G       G::::G  P::::P                    T:::::T        ")
print("  C:::::CCCCCCCC::::C h:::::h     h:::::ha::::a    a:::::a      t::::::tttt:::::t G:::::GGGGGGGG::::GPP::::::PP                TT:::::::TT      ")
print("   CC:::::::::::::::C h:::::h     h:::::ha:::::aaaa::::::a      tt::::::::::::::t  GG:::::::::::::::GP::::::::P                T:::::::::T      ")
print("     CCC::::::::::::C h:::::h     h:::::h a::::::::::aa:::a       tt:::::::::::tt    GGG::::::GGG:::GP::::::::P                T:::::::::T      ")
print("        CCCCCCCCCCCCC hhhhhhh     hhhhhhh  aaaaaaaaaa  aaaa         ttttttttttt         GGGGGG   GGGGPPPPPPPPPP                TTTTTTTTTTT      ")
print("                                                                                                                                                ")


openai.api_key = os.environ["OPENAI_API_KEY"]
model_engine = "text-davinci-002"

# Get the username
username = os.environ.get("USER")

# ANSI escape codes for gold and blue colors
GOLD = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# Define chat history file
chat_history_file = "chat_history.txt"

# Load chat history if it exists, or start with empty list
if os.path.exists(chat_history_file):
    with open(chat_history_file, "r") as f:
        chat_history = f.readlines()
else:
    chat_history = []

def get_response(prompt):
    context = "".join(chat_history)
    response = openai.Completion.create(
        engine=model_engine,
        prompt=context + f"\n{BLUE}{username}:{RESET} {prompt}\n{GOLD}ChatGPT:",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7
    )
    message = response.choices[0].text
    return message.strip()

while True:
    try:
        prompt = input(BLUE + username + ": " + RESET)
        response = get_response(prompt)
        print()
        chat_history.append(f"{BLUE}{username}:{RESET} {prompt}\n{GOLD}ChatGPT: {RESET}{response}\n")
        with open(chat_history_file, "w") as f:
            f.writelines(chat_history)
        print(GOLD + "ChatGPT: " + RESET + response)
        print()
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
