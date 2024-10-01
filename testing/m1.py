def do_stuff(num):
    try:
        if num:
            return int(num)+5
        else:
            return "please enter a num"
    except ValueError as err:
        return err
