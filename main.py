import sys
import urllib.request
import json
import os

def get_emojis(token, guild_id):
    req = urllib.request.Request(
        f"https://discord.com/api/v9/guilds/{guild_id}/emojis",
        headers={"Authorization": token}
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

if __name__ == "__main__":
    token = sys.argv[1]
    guild_id = sys.argv[2]
    emojis = get_emojis(token, guild_id)
    os.makedirs("emojis", exist_ok=True)
    for e in emojis:
        ext = "gif" if e.get("animated") else "png"
        url = f"https://cdn.discordapp.com/emojis/{e['id']}.{ext}"
        urllib.request.urlretrieve(url, f"emojis/{e['name']}.{ext}")
        print(f"downloaded {e['name']}")
    print(f"done, {len(emojis)} emojis")
