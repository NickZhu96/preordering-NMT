import jsonlines

ord1 = open('./train.human.ja','r',encoding='utf-8').readlines()
pre1 = open('./train.pre.ja','r',encoding='utf-8').readlines()

ord2 = open('./valid.human.ja','r',encoding='utf-8').readlines()
pre2 = open('./valid.pre.ja','r',encoding='utf-8').readlines()

ord3 = open('./test.human.ja','r',encoding='utf-8').readlines()
pre3 = open('./test.pre.ja','r',encoding='utf-8').readlines()


with jsonlines.open('./jsonl/train_mbart.jsonl', mode='w') as writer:
    for i in range(len(ord1)):
        #writer.write({ 'translation': { 'ord': ord[i], 'pre': pre[i] } })
        writer.write({ 'translation': { 'ja': ord1[i], 'en': pre1[i] } })

with jsonlines.open('./jsonl/valid_mbart.jsonl', mode='w') as writer:
    for i in range(len(ord2)):
        #writer.write({ 'translation': { 'ord': ord[i], 'pre': pre[i] } })
        writer.write({ 'translation': { 'ja': ord2[i], 'en': pre2[i] } })

with jsonlines.open('./jsonl/test_mbart.jsonl', mode='w') as writer:
    for i in range(len(ord3)):
        #writer.write({ 'translation': { 'ord': ord[i], 'pre': pre[i] } })
        writer.write({ 'translation': { 'ja': ord3[i], 'en': pre3[i] } })

