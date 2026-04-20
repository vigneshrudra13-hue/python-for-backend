from fromfunc import ko


class playerexception(Exception):
    pass


class playerstats:
    def __init__(self, Name, ovrgames, kills):
        self.name = Name
        self.tgames = ovrgames
        self.kills = kills
        if self.tgames <= 0:
            raise ValueError("Total games must be > 0")
        self.kd = self.kills / self.tgames

    def report(self):
        print(f"Hey {self.name}! you've played {self.tgames} games and have a k/d ratio of {self.kd:.3f}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="A greeting message and optional player stats")
    parser.add_argument("-n", "--name", metavar="Name", required=True, help="Name of the person to greet")
    parser.add_argument("-l", "--lang", metavar="language", required=True, choices=["English", "Spanish", "German"], help="language to greet")
    parser.add_argument("-s", "--stats", action="store_true", help="Collect player stats after greeting; requires --games and --kills")
    parser.add_argument("--games", type=int, help="Total games played (required with --stats)")
    parser.add_argument("--kills", type=int, help="Total kills (required with --stats)")

    args = parser.parse_args()
    ko(args.name, args.lang)

    if args.stats:
        if args.games is None or args.kills is None:
            parser.error("--stats requires --games and --kills")
        try:
            stats = playerstats(args.name, args.games, args.kills)
        except Exception as e:
            parser.error(f"Invalid stats: {e}")
        else:
            stats.report()




