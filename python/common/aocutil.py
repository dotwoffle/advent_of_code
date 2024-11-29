def split_input_groups(challenge_input: list[str], delimiter_line: str = "") -> list[list[str]]:
    """
    Splits the challenge input into groups of lines using a specific line of text as a delimiter.
    Parameters:
        `challenge_input`: The lines of the challenge input file.
        `delimiter_line`: The contents of the lines to search for when splitting groups of lines. The delimiter lines
        will not be included in the groups. Defaults to an empty string, which is the result of a line only containing
        "\n" after being stripped.
    Returns:
        The groups of lines as separated by the given delimiter.
    """

    input_groups = []
    current_group = []

    for line in challenge_input:
        if line == delimiter_line and len(current_group) != 0:
            input_groups.append(current_group)
            current_group = []
        elif line != delimiter_line:
            current_group.append(line)

    if len(current_group) != 0:
        input_groups.append(current_group)

    return input_groups