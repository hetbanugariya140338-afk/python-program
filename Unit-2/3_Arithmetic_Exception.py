import logging


logging.basicConfig(level=logging.ERROR)

def make_error():
    try:

        result = 10 / 0
    except ZeroDivisionError as error:

        logging.error("Wait! You tried to divide by zero.")
        print(f"Log captured: {error}")

make_error()