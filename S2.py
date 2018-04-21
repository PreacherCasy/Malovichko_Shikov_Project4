from Bio import SeqIO

my_list = []
file = SeqIO.parse('/home/reverend_casy/Downloads/augustus.whole.txt.aa', 'fasta')
for record in file:
    if record.seq[0] == 'M':
        my_list.append(record)

SeqIO.write(my_list,'/home/reverend_casy/Downloads/narrowed.fa', 'fasta')