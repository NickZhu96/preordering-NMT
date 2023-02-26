def data_loader(txt):
    context = open(txt,'r',encoding='utf-8')
    lines = context.readlines()
    return lines

import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--src',help='path to source file')
    parser.add_argument('-t','--target',help='path to target file')
    parser.add_argument('-a','--alignment',help='target-src alignment')
    parser.add_argument('-o','--output',help='path to preordered output file')
    args = parser.parse_args()
    return args

if __name__=='__main__':
    #en是tgt，ja是src
    args = parse_args()

    en_lines = data_loader(args.target)
    ja_lines = data_loader(args.src)
    align_lines = data_loader(args.alignment)
    ans_all = []
    src_dic = []
    unaligned_token = []
    unaligned_token_list = {}
    with open(args.output,'w',encoding='utf-8') as final:
        for en_line,ja_line,align_line in zip(en_lines,ja_lines,align_lines):
            en_line = en_line.split()
            ja_line = ja_line.split()
            align_line = align_line.split()
            ans = []
            dic = {}
            if not align_line:
                ans_all.append(ja_line)
                continue
            for align in align_line:
                align = align.split('-')
                if align[0] not in dic:
                    dic[align[0]] = [align[1]]
                else:
                    dic[align[0]].append(align[1])
            for i in range(len(en_line)):
                if str(i) in dic:
                    for ja_token_num in dic[str(i)]:
                        ans.append(ja_line[int(ja_token_num)])

            for i in range(1,10):
                if i > len(ans):
                    break
                j=0
                while j < len(ans)-i:
                    if j+i+i > len(ans):
                        break
                    if ans[j:j+i] == ans[j+i:j+i+i]:
                        #for temp in ans[j+i:j+i+i]:
                            #ans.remove(temp)
                        for k in range(i):
                            ans.pop(j+i)
                    else:
                        j+=1

            ans_all.append(ans)
            #for ja_token in ja_line:
             #   if ja_token not in src_dic:
              #      src_dic.append(ja_token)
        for i in ans_all:
            final.write(' '.join(i) + '\n')








