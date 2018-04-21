from Bio import SeqIO

cands = open('/home/reverend_casy/Downloads/candidates.txt', 'r')
r, rr = cands.readlines(), []
for item in r:
    item = item.replace('> ','')
    item = item.replace('\n', '')
    rr.append(item)
my_list = []
file = SeqIO.parse('/home/reverend_casy/Downloads/narrowed.fa', 'fasta')
for record in file:
    if record.id in rr:
        my_list.append(record)
SeqIO.write(my_list,'/home/reverend_casy/Downloads/candidates_seqs.fasta', 'fasta')