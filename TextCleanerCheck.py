import string, os, glob, re
import cleaner

chap1 = '1-introduction'
chap2 = '2-time-domain-analysisand-z-transform'
chap3 = '3-frequency-domain-analysis'
chap4 = '4-infinite-impulse-response-filters'
chap5 = '5-finite-impulse-response-filters'
chap6 = '6-filter-realizations'
chap7 = '7-quantized-filter-analysis'
chap8 = '8-hardware-design-using-dsp-chips'
chap9 = '9-matlab-primer'

chap_list = [chap1, chap2, chap3, chap4, chap5, chap6, chap7, chap8,chap9]
#chap_list = [chap7]
linecounter_1 = 0
linecounter_2 = 0
emptyline_1 = 0
emptyline_2 = 0
token_counter_1 = 0
token_counter_2 = 0
shortline_counter_1 = 0
shortline_counter_2 = 0
longline_counter_1 = 0
longline_counter_2 = 0

for chap in chap_list:

    inputpath='/Users/Zhenghao/Desktop/URECA/Text cleaning related/Demo/corpus/DSP_books/raw_introduction-to-digital-signal-processing-exported/'+chap+'/'
    inputpath_cleaned='/Users/Zhenghao/Desktop/URECA/Text cleaning related/Demo/output/'+chap+'/'

    os.chdir(inputpath)
    for afile in glob.glob("*.txt"):
        inputfile=open(afile,'r',encoding='utf-8')
#        print('reading '+afile)
        for line in inputfile :
            linecounter_1 += 1
            if line=="\n":
                emptyline_1 += 1
            token_counter_1 += len(line.split())
            if len(line.split()) <= 10:
                shortline_counter_1 += 1
            if len(line.split()) >= 15:
                longline_counter_1 += 1
        inputfile.close()
            
    os.chdir(inputpath_cleaned)
    for afile in glob.glob("*.txt"):
        inputfile=open(afile,'r', encoding='utf-8')
#        print('reading '+afile)
        for line in inputfile:
            linecounter_2 += 1
            if line=="\n":
                emptyline_2 += 1
            token_counter_2 += len(line.split())
            if len(line.split()) <= 10:
                shortline_counter_2 += 1
            if len(line.split()) >= 15:
                longline_counter_2 += 1
        inputfile.close()
            
print('There are {} lines in raw file, {} empty lines'.format(linecounter_1, emptyline_1))
print('There are {} lines in cleaned file, {} empty lines'.format(linecounter_2, emptyline_2))
print('Average {} words in a line in raw file.'.format(token_counter_1/linecounter_1))
print('Average {} words in a line in cleaned file.'.format(token_counter_2/linecounter_2))
print('There are {} lines with less than 10 tokens in raw, {} lines in cleaned file.'.format(shortline_counter_1, shortline_counter_2))
print('There are {} lines with more than 15 tokens in raw, {} lines in cleaned file.'.format(longline_counter_1, longline_counter_2))

