# FASTADB - A DATABASE FOR YOUR FASTA FILES

from Bio.SeqIO import parse
from fdb_registers import FDBRegister
import json


class FastaDB():
    def __init__(self):
        self.filename = ""

    def DB(self, filename):
        """
        Function for loading the database file
        :param: filename
        """
        try:
            self.filename = filename
            file = open(filename, "r+")
        except:
            self.filename = filename
            file = open(filename, "w")

        return file

    def generate_fdb_file_header(self):
        dict_header = {}
        dict_header['FastaDB'] = 'GENOME.FDB'
        return dict_header

    def mount_fdb_file(self, fdb_registers):
        if fdb_registers is None:
            return None

        dict_header = self.generate_fdb_file_header()
        fdb_file_dicts = [dict_header]

        index = 1
        for register in fdb_registers:
            new_dict = {}
            new_dict["gene"+str(index)] = register.build_dictionary()
            fdb_file_dicts.append(new_dict)
            index = index + 1

        return json.dumps(fdb_file_dicts)

    def FastaToFDB(self, fastafile):
        fdb_registers = []
        content = open(fastafile)

        sequences = parse(content, 'fasta')

        for sequence in sequences:
            fdb_register = FDBRegister()
            fdb_register.filename = fastafile
            fdb_register.description = sequence.id
            fdb_register.gene = str(sequence.seq)

            fdb_registers.append(fdb_register)

        content.close()

        return self.mount_fdb_file(fdb_registers)

    def ImportFasta(self, fastafile):
        try:
            return FastaDB().FastaToFDB(fastafile)
        except ValueError:
            return ValueError

