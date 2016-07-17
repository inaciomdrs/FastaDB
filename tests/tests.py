# TODO - Simple tests for checking the code verasity
# TODO - Make the tests run on Jenkins environment

# Importing FastaDB in Python 3
if sys.version_info >= (3, 0):
	sys.path += ['../FastaDB/']
	from fdb import FastaDB
# Importing FastaDB in Python 2
else:
	from FastaDB import FastaDB


def Test_FDB_Parsing():
	print("Instantiating a FastaDB object...")
	fasta_db = FastaDB()
	print("Defining input file name...")
	filename = "../FastaDB/test2.fasta"
	username = "inacio_medeiros"
	print("Invoking FDB parsing...")
	parsed_fdb_structure = fasta_db.ImportFasta(filename, username)
	print("Saving in file...")
	content = json.dumps(parsed_fdb_structure)
	fdb_file_name = filename+".fdb"
	fdb_file = open(fdb_file_name, "w")
	fdb_file.write(content)


if __name__ == "__main__":
	Test_FDB_Parsing()
