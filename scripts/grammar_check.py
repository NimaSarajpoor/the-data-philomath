import language_tool_python
import subprocess
import os

tool = language_tool_python.LanguageTool('en-US')

# Find changed markdown files in this PR
base_ref = os.environ.get("GITHUB_BASE_REF")
head_ref = os.environ.get("GITHUB_HEAD_REF")

# Fallback: if running locally, compare against main
if not base_ref:
    base_ref = "origin/main"
if not head_ref:
    head_ref = "HEAD"

diff_cmd = ["git", "diff", "--name-only", f"{base_ref}...{head_ref}", "--", "posts/*.md"]
changed_files = subprocess.check_output(diff_cmd, text=True).splitlines()

if not changed_files:
    print("✅ No changed markdown files to check.")
    exit(0)

for md_file in changed_files:
    with open(md_file, "r") as f:
        text = f.read()

    matches = tool.check(text)
    if matches:
        print(f"--- Issues in {md_file} ---")
        for m in matches[:10]:  # limit to 10 per file
            print(f"Line {m.contextOffset}: {m.message} (suggestion: {', '.join(m.replacements[:3])})")