from langchain.tools import Tool
from datetime import datetime

def save_meeting_summary(data: str, filename: str = "meeting_summary.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Meeting Summary ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Meeting summary successfully saved to {filename}"

save_tool = Tool(
    name="save_meeting_summary_to_file",
    func=save_meeting_summary,
    description="Saves the structured meeting summary and action items to a text file.",
)