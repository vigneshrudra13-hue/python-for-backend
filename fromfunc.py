def ko(name,lang):
    greeting = {
        "English":"Hello","Spanish":"Hola","German":"Hallo"
    }
    msg = f"{greeting[lang]} {name}"
    print(msg)
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description="A greeting message"
    )
    parser.add_argument(
        "-n","--name",metavar="Name",
        required=True,help="Name of the person to greet "
    )
    parser.add_argument(
        "-l","--lang", metavar="language",
        required=True,choices=["English","Spanish","German"],
        help="language to greet"
    )
    args = parser.parse_args()
    ko(args.name,args.lang)
    
