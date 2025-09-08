import language_tool_python
import glob

tool = language_tool_python.LanguageTool('en-US')

output = []
for md_file in glob.glob("posts/*.md"):
    with open(md_file, "r") as f:
        text = f.read()

    matches = tool.check(text)
    if matches:
        output.append(f"--- Issues in {md_file} ---")
        for m in matches[:10]:  # limit to 10 per file
            output.append(
                f"Line {m.contextOffset}: {m.message} "
                f"(suggestion: {', '.join(m.replacements[:3])})"
            )

if output:
    print("\n".join(output))
else:
    print("✅ No major grammar issues found.")