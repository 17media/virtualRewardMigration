import argparse
from command import Command, background_color, text_color

url_map = {
    "stag": "https://stag-slackbot.17app.co/command",
    "prod": "https://slackbot.17app.co/command",
}
command_map = {
    "backgroundColor_create": background_color.CreateCommand,
    "backgroundColor_send": background_color.SendRewardCommand,
    "textColor_create": text_color.CreateCommand,
    "textColor_send": text_color.SendRewardCommand,
}


def get_parser():
    p = argparse.ArgumentParser()
    p.add_argument("--accessToken", type=str, required=True)
    p.add_argument("-e", "--env", type=str, default="stag")
    p.add_argument("-t", "--type", type=str, required=True)
    p.add_argument("-a", "--action", type=str)
    return p


def get_command(command_type: str, action: str) -> Command:
    key = f"{command_type}_{action}"
    return command_map[key]


def main():
    parser = get_parser()
    args = parser.parse_args()
    command = get_command(args.type, args.action)
    c = command(args.accessToken, url_map[args.env])
    c.process()


if __name__ == "__main__":
    main()
