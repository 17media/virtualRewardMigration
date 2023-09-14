import csv
from datetime import datetime, timezone

import requests

from command import Command, _save_to_file


class CreateCommand(Command):
    def __init__(self, token: str, url: str):
        self.token = token
        self.url = url
        self.source = "./data/text_color_style_settings_tt.csv"

    def process(self):
        en_display_name = "Mystery Comment Text Color"
        ar_display_name = "Mystery Comment Text Color"
        tc_display_name = "神秘的留言文字顏色"
        cn_display_name = "神秘的留言文字顏色"
        jp_display_name = "ミステリーコメント文字色"

        headers = {"content-type": "text/plain", "AccessToken": self.token}
        fail_style_ids = []
        with open(self.source, "r") as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                start_time = datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
                style_id = row["Style ID"].rstrip()
                color_code = row["Color Code"].rstrip()
                command_raw = [
                    "!commentTextColor",
                    "create",
                    f"{style_id}",
                    f"{color_code}",
                    f"{en_display_name}",
                    f"{ar_display_name}",
                    f"{tc_display_name}",
                    f"{cn_display_name}",
                    f"{jp_display_name}",
                    f"{start_time}",
                ]
                body = "\n".join(command_raw)
                resp = requests.post(self.url, headers=headers, data=body.encode())
                if resp.status_code != 200 or "danger" in resp.text:
                    # style_id,err_msg
                    fail_style_ids.append(
                        f"{style_id},{resp.json()},{resp.status_code}"
                    )
                else:
                    print(style_id)

        _save_to_file(fail_style_ids, "textColor_create")


class SendRewardCommand(Command):
    def __init__(self, token: str, url: str):
        self.source = "./data/text_color_send_reward.csv"
        self.token = token
        self.url = url

    def process(self):
        headers = {"content-type": "text/plain", "AccessToken": self.token}
        fail_style_ids = []
        with open(self.source, "r") as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                color_code = row["Color Code"].rstrip()
                # text-color-000000
                style_id = f"text-color-{color_code[1:]}"
                user_id = row["User ID"].rstrip()
                start_time = datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
                end_time = (
                    f"\n{row['End Date'].rstrip()}"
                    if len(row["End Date"].rstrip()) > 0
                    else ""
                )
                command_raw = [
                    "!commentTextColor sendUsers",
                    f"{style_id}",
                    f"{start_time} {end_time}",
                    "---",
                    f"{user_id}",
                ]

                body = "\n".join(command_raw)
                resp = requests.post(self.url, headers=headers, data=body.encode())
                if resp.status_code != 200 or "danger" in resp.text:
                    print(f'[Create FAIL]: {style_id}, {resp.text}')
                    # csv: style_id,err_msg
                    fail_style_ids.append(
                        f"{style_id}, {user_id},{resp.json()},{resp.status_code}"
                    )
                else:
                    print(f'[Create Success] {style_id}, {user_id}')
        _save_to_file(fail_style_ids, "textColor_send_reward")
