import os
import sys


class Files(object):
    def __init__(self):
        self.path = sys.path[0]  # Remove old when finished with new dir location

    def get_fname(self, id_):
        """Gets the file name for the given ID and also checks if it exists"""
        for f in self.list_files():
            check_id = f.split('-')[2].strip('.csv')
            if check_id == id_:
                return f

        print 'File for id - {} does not exist'.format(id_)
        raise SystemExit

    def list_files(self):
        return [f for f in os.listdir(self.path) if f.endswith('.csv')]

    def list_ids(self):
        return [f.split('-')[2].strip('.csv') for f in self.list_files()]


class InFiles(Files):
    def __init__(self):
        super(InFiles, self).__init__()
        self.path += '/in_files/'

    def del_file(self, id_):
        """
        Remove the file after its been loaded to DB
        """
        fname = self.get_fname(id_)
        os.remove(self.path + fname)

    def transfer_file(self, id_):
        """
        This method transfers the file from the import directory
        to an output directory that would hold the files.  I don't think the
        old files need to be accessed after they are in DB so adding
        method to delete the file instead.
        """
        fname = self.get_fname(id_)
        source = self.path + fname
        dest = OutFiles().path + fname
        os.rename(source, dest)


class OutFiles(Files):
    def __init__(self):
        super(OutFiles, self).__init__()
        self.path += '/out_files/'