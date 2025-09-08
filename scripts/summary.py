import argparse
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.

def get_summary(text):
    """
    Summarizes the input text using a generative AI model.

    Parameters
    ----------
    text : str
        The text to be summarized.
    
    Returns
    -------
    out : str
        The summarized text.
    """
    client = genai.Client()

    prompt = (
        "Summarize the following text in a concise manner. "
        + "Focus on the main points and avoid unnecessary details."
        + "This is going to be used a post for LinkedIn."
    )
    response = client.models.generate_content(
        model="gemini-2.5-pro", contents=f"{prompt}\n\ntext: {text}"
    )
    
    return response.text


def summarize_file(fpath):
    """
    Reads a file, summarizes its content, and prints the summary.
    This currently supports .md and .txt files only.

    Parameters
    ----------
    fpath : str
        The path to the file to be summarized.

    Returns
    -------
    out : str
        The summary of the file's content.
    """
    eligible_formats = ['.md', '.txt']
    if not any(fpath.endswith(ext) for ext in eligible_formats):
        msg = f"Unsupported file format. Supported formats are: {eligible_formats}"
        raise ValueError(msg)

    with open(fpath, 'r') as f:
        text = f.read()
    
    return get_summary(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A script to process a file from a given path.",
    )

    parser.add_argument(
        'filepath',
        type=str,
        help="The path to the file to be processed."
    )

    args = parser.parse_args()
    fpath = args.filepath
    summary_text = summarize_file(fpath)

    print("Summary: \n", summary_text)