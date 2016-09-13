import string, os, glob, time
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

# for i in range(0,19):
start_time = time.time()
for chap in chap_list:

    inputpath='/Users/Zhenghao/Desktop/URECA/Text cleaning related/Demo/corpus/DSP_books/raw_introduction-to-digital-signal-processing-exported/'+chap+'/'
    outputpath='/Users/Zhenghao/Desktop/URECA/Text cleaning related/Demo/output/'+chap+'/'

    if not os.path.exists(outputpath):
        os.makedirs(oSutputpath)

    os.chdir(inputpath)
    for afile in glob.glob("*.txt"):
            
            outputfile=open(outputpath+afile,'w+',encoding='utf-8')
            inputfile=open(afile,'r',encoding='utf-8')
            print('reading '+afile)
            for line in inputfile :
                    line = cleaner.string_validation(line)
                    line = cleaner.remove_formula(line)
                    line = cleaner.remove_inlineformula(line)
                    line = cleaner.remove_inlinefunction(line)
                    line = cleaner.join_brokenwords(line)
                    line = cleaner.replace_known(line)
                    outputfile.write(line)
            file_str = cleaner.merge_placeholder(outputfile)
            outputfile.seek(0)
            outputfile.truncate()
            outputfile.write(file_str)
            outputfile.close()
            inputfile.close()
stop_time = time.time()
print("-------- %s seconds ---------" % (stop_time - start_time))
# total_time += stop_time - start_time
# print('Average time: {}'.format(total_time/20))
