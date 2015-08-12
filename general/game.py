from secondary_windows.following import FollowingWin
from collections import defaultdict
from secondary_windows.set_username import NameWin
import timeit

"""

"""


class Game:
    """
    Gives various info about a specific game.
    """
    POSITIONS = ('P', 'P', 'C', '1B', '2B', '3B', 'SS', 'OF', 'OF', 'OF')

    def __init__(self, model, game_id):
        self.model = model
        self.game_id = game_id

        # Gets a list of the players followed from static method in FollowingWin class.
        self.following = set([x.lower() for x in FollowingWin.load_players()])

        self.setup()

    def format_selected(self, lineup_dict, filter_=None):
        """
        Formats the selected lineups from dictionary form to a list of lists
        that can be used by the count_players method.
        :param filter_:
            For future use, can feed a list of players that you want to
            see and it will filter out the players not given.
        :return:
            A list of lineup lists.
        """
        if filter_:
            filtered_dict = {username: lineup_dict[username]
                             for username in filter_}
        else:
            filtered_dict = lineup_dict

        return [lineup for player in filtered_dict.values() for lineup in player]

    def get_all_ownership(self):
        """
        Gets the ownership percentage of all the players.  This method is
        to encapsulate the other methods needed to do this so only one call to a
        method is needed by an outside call.
        :return:
            A dictionary of ownerships by position.
        """
        ownership = self.ownership_percent(self.all_counts)
        return ownership

    def get_following_ownership(self):
        """
        Does the same as get_all_ownership but only gets the ownership from the players
        you are following.
        :return:
            A dictionary of ownerships by position.
        """

        team_list = self.format_selected(self.following_lineups)
        counts = self.update_following(team_list)
        ownership = self.ownership_percent(counts)
        return ownership

    def get_player_ownership(self):
        pass

    def ownership_percent(self, count_dict):
        """
        Converts a dictionary of player counts into a dictionary of player ownership
        by position.
        :return:
        """
        num_entries = sum([sum(v.values()) for v in count_dict.values()]) / len(Game.POSITIONS)
        percents = {pos: {} for pos in set(Game.POSITIONS)}
        for k, v in count_dict.items():
            ownership = (sum(v.values()) / float(num_entries)) * 100
            for pos in v.keys():
                percents[pos][k] = round(ownership, 1)

        return percents

    def setup(self):
        """
        Loads entries from the database and makes a list of all teams
        and a dictionary for the followed players.

        This was designed with the thought of how long it takes to laod all
        the entries of a given tournament.  Because I don't want a long load time
        each time a new tournament is selected, I designed this method to only pass
        through the entries of the tournament once for all the users and do several
        operations though out, which will sacrifice the look and modularity of the
        code a bit.
        :return:
        """
        entries = self.model.query("SELECT * FROM entries WHERE game_id = %s", (self.game_id,))

        # Use default dict for cleaner code and to boost performace a litte.

        self.all_counts = defaultdict(dict)
        self.following_lineups = defaultdict(list)
        self.my_players = []

        my_name = NameWin.get_cur_name().lower()

        for lineup in entries:
            # lineup[1] = username, lineup[3:] = team of username
            for n, player in enumerate(lineup[3:]):
                position = Game.POSITIONS[n]
                self.all_counts[player][position] = self.all_counts[player].get(position, 0) + 1

            username = lineup[1].lower()
            if username in self.following:
                self.following_lineups[username].append(lineup[3:])
            elif username == my_name:
                self.my_players.append(lineup[3:])


    def update_following(self, lineups):
        """
        A method to recount the lineups of the followed players.
        Used when modifying which usernames are shown.
        :return:
        """
        counts = defaultdict(dict)

        for team in lineups:
            for n, player in enumerate(team):
                position = Game.POSITIONS[n]
                counts[player][position] = counts[player].get(position, 0) + 1

        return counts