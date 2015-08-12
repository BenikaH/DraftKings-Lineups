from general import db
from general.file_container import InFiles
import csv


class Game(dict):
    def __init__(self, info):
        super(Game, self).__init__(info)

    def save(self):
        database = db.DB()

        q = 'REPLACE INTO games ({}) VALUES ({})'.format(','.join(self.keys()), ','.join(['%s']*len(self)))
        database.query(q, self.values())
        database.finish()


class Entry(dict):
    POS_CONV = {'P': 'pitcher_', 'C': 'catcher', '1B': 'first_base',
                '2B': 'second_base', '3B': 'third_base', 'SS': 'shortstop',
                'OF': 'outfield_'}

    def __init__(self, record, game_id):
        super(Entry, self).__init__()
        self['game_id'] = game_id
        self['username'] = record['EntryName'].split('(')[0].strip()
        self['points'] = record['Points']

        self.set_positions(record['Lineup'])

    def set_positions(self, lineup):
        pitcher = 1
        outfielder = 1

        for player in lineup.split(','):
            pos, name = [x.strip('( ') for x in player.split(')')]
            k = Entry.POS_CONV[pos]

            if pos == 'P':
                k += str(pitcher)
                pitcher += 1
            elif pos == 'OF':
                k += str(outfielder)
                outfielder += 1

            self[k] = name

    def save(self):
        database = db.DB()

        q = 'INSERT INTO entries ({}) VALUES ({})'.format(','.join(self.keys()), ','.join(['%s']*len(self)))
        database.query(q, self.values())
        database.finish()


def game_info(results):
    """
    The controller for the tourney_info window.
    Will enter the submitted information into the database
    given from the info window.
    :param results:
        A dictionary of tournament summary information passed
        by the tournament info window.
    :return:
    """
    in_files = InFiles()
    fname = in_files.path + in_files.get_fname(results['id'])

    with open(fname, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            rec = Entry(line, results['id'])
            rec.save()
            entries = reader.line_num

    res = results
    res['entries'] = entries - 1
    game = Game(res)
    game.save()