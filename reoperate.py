import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input',help='path to input file')
    parser.add_argument('-o','--output',help='path to output file')
    args = parser.parse_args()
    return args

if __name__=='__main__':
    args = parse_args()
    text = open(args.input,'r').readlines()
    with open(args.output,'w') as new:
        for i in range(len(text)):
            text_=text[i].split()
            temp = ''
            for j in range(len(text_)):
                if text_[j][-1]==',':
                    temp+=text_[j][:-1] + ' ' + ','
                elif text_[j][-1]=='.':
                    temp+=text_[j][:-1] + ' ' + '.'
                elif text_[j][-2:]=='\'s':
                    temp+=text_[j][:-2] + ' ' + '\'s'
                elif text_[j][-3:]=='n\'t':
                    temp+=text_[j][:-3] + ' ' + 'n\'t'
                else:
                    temp +=text_[j]
                temp+=' '
            temp+='\n'
            new.write(temp)

