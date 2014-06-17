__author__ = 'proline'

import datetime
import py_execution_time

# Extract the sequence line from fastq files
# Getting a timestamp to append to the output filename
def getTime():
	return datetime.datetime.now()

time = getTime()
filename_timestamp = time.strftime("%m%d%y_%H%M_")
fastqseq_output = filename_timestamp + "fastq_seq.txt"

# Extracting the sequence line, which is the second line in a set of four lines in the fastq file.
fastq_sequence = open(fastqseq_output, 'w')
fastq_file = raw_input('Enter fastq file name: ')

def get_sequence_fastq():
	with open(fastq_file, 'r') as fastq_input:
		line_count = 0
		for eachline in fastq_input:
			if line_count == 1:
				sequence = str.strip(eachline)
				fastq_sequence.write(sequence + "\n")
				#print sequence
			line_count += 1
			if line_count == 4:
				line_count = 0
	fastq_sequence.close()

seq = get_sequence_fastq()