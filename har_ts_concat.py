
import json
import sys
import base64
import re

def main():
    if len(sys.argv) < 2: 
        return
    har_filename = sys.argv[1]
    output_file = open(har_filename + ".ts", 'wb')
    har_file = open(har_filename, encoding='utf8')
    har = json.load(har_file)
    if "log" not in har: return
    har = har["log"]
    har_file.close()
    if "entries" not in har: return
    for entry in har["entries"]:
        request = entry["request"]
        url = request["url"]
        if not url.endswith(".ts"): 
            continue
        match = re.search('\/([^\/]*\.ts)$', url)
        if match is None: 
            continue
        name = match.group(1)
        print(name)
        response = entry["response"]
        if response["status"] != 200: continue
        if "content" not in response: continue
        content = response["content"]
        if "text" not in content: continue
        text = content["text"]
        decoded = base64.b64decode(text)
        output_file.write(decoded)

    output_file.close()

if __name__ == "__main__":
    main()
