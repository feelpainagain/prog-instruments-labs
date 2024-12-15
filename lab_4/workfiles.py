import json

from log import logger


def read_text(path: str):
    """The function of reading text from file
    Args:
      path: path to the file
    Returns:
      text from the file
    """
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            text = f.read().lower()
        return text
    except FileNotFoundError:
        logger.info("File not found")
        return "File not found"
    except Exception as e:
        logger.info("Error reading file")
        return f"Error reading file: {str(e)}"


def write_text(path: str, text: str):
    """The function of writing information to file
    Args:
      path: path to the file
      text: written text
    """
    try:
        with open(path, 'w', encoding='UTF-8') as f:
            f.write(text)
    except FileNotFoundError:
        logger.info("File not found")
    except Exception as e:
        logger.info(f"Error writing to file: {str(e)}.")
