import time
import os


def get_elapsed_time_in_str(start: int) -> str:
    """Calculate elapsed time and build a string with value to return"""
    current_time = int(round(time.time()))
    elapsed_time = current_time - start
    minutes = int(round(elapsed_time / 60))
    seconds = elapsed_time % 60
    elapsed_str = f"{minutes:02}:{seconds:02}"
    return elapsed_str


def get_remaining_time_in_str(i: int, len: int, start: int) -> str:
    """Calculate remaining time and build a string with value to return"""
    current_time = int(round(time.time()))
    elapsed_time = current_time - start
    remaining_time = elapsed_time * (len - i) / i
    remaining_time = int(round(remaining_time))
    minutes = int(round(remaining_time / 60))
    seconds = remaining_time % 60
    remaining_str = f"{minutes:02}:{seconds:02}"
    return remaining_str


def get_elapsed_and_remaining_time(i: int, len: int, start: int) -> str:
    """Call get_elapsed_time  and get_remaining_time
        to build a string to return"""
    elapsed_str = get_elapsed_time_in_str(start)
    remaining_str = "00:00"
    if i > 0:
        remaining_str = get_remaining_time_in_str(i, len, start)
    elapsed_and_remaining_str = f"[{elapsed_str}<{remaining_str}, "
    return elapsed_and_remaining_str


def get_iter_per_sec(i: int, start: int) -> str:
    """Calculate iteration per second and build a
        string with value to return"""
    current_time = time.time()
    elapsed_time = current_time - start
    iter_per_sec = i / elapsed_time
    it_per_sec_str = f"{iter_per_sec:.2f}it/s]"
    return it_per_sec_str


def make_progress_bar(i: int, len: int, start: int):
    """
    Calculate elapsed and remaining time
    Calculate iteration per second
    Calculate the len of progresse bar and blank
            compared to the size of terminal
    Assemble all the elements of the front bar of the print
    """
    terminal_width = os.get_terminal_size().columns
    bar_len = terminal_width - 39
    elapsed_and_remaining_str = get_elapsed_and_remaining_time(i, len, start)
    it_per_sec_str = get_iter_per_sec(i, start)
    block = "\u2588"
    space = " "
    progress = min(100, int((i / len) * 100))
    bar_block = block * int((progress / 100) * bar_len)
    blank = space * (bar_len - int(progress * bar_len / 100))
    bar = (
        str(progress)
        + "%"
        + "|"
        + bar_block
        + blank
        + "|"
        + str(i)
        + "/"
        + str(len)
        + " "
        + elapsed_and_remaining_str
        + it_per_sec_str
    )

    print("\r" + bar, end="", flush=True)


def ft_tqdm(lst: range) -> None:
    """Print a progress bar as the original tqdm"""
    start_time = int(round(time.time()))

    for i in range(0, len(lst) + 1):
        if i % 10 == 0 or i == len(lst):
            make_progress_bar(i, len(lst), start_time)
        yield
