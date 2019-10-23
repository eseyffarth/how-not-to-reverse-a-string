# 19/20: Exploit the 3rd dimension

import os

def create_pdf(word, snippet_path, outpath):
    # I stored some tex boilerplate stuff in separate files to avoid
    # clogging up this beautiful python code
    with open(snippet_path.format(1), "r", encoding="utf8") as sn1file:
        sn1 = sn1file.read()
    with open(snippet_path.format(2), "r", encoding="utf8") as sn2file:
        sn2 = sn2file.read()    
    with open(snippet_path.format(3), "r", encoding="utf8") as sn3file:
        sn3 = sn3file.read()
    with open(snippet_path.format(4), "r", encoding="utf8") as sn4file:
        sn4 = sn4file.read()

    # OK, and some boilerplate is defined here
    node_boilerplate_1 = "\\node[rectangle, draw=black, very thick, inner sep=8pt, minimum size=3\\baselineskip] ({}) at (0, 0) {{\\Large\\textbf{{{}}}}};"
    node_boilerplate_2 = "\\node[rectangle, draw=black, very thick, inner sep=8pt, minimum size=3\\baselineskip] ({}) at ({}, 0) {{\\Large\\textbf{{{}}}}};"

    with open(outpath, "w", encoding="utf8") as outfile:
        print(sn1, file=outfile)
        # draw first node of the word
        print(node_boilerplate_1.format(word[0], word[0]), 
              file=outfile)
        # draw all the remaining nodes
        for i in range(1, len(word)):
            print(node_boilerplate_2.format(word[i], i*2, word[i]), 
                  file=outfile)

        print(sn2, file=outfile)
        # draw first index node
        print(node_boilerplate_1.format(1, 1), file=outfile)
        # draw all the remaining index nodes
        for i in range(1, len(word)):
            print(node_boilerplate_2.format(i+1, i*2, i+1), 
                  file=outfile)

        print(sn3, file=outfile)
        # draw first index node
        print(node_boilerplate_1.format(1, 1), file=outfile)
        # draw all the remaining index nodes
        for i in range(1, len(word)):
            print(node_boilerplate_2.format(i+1, i*2, i+1), 
                  file=outfile)

        print(sn4, file=outfile)
    os.system("pdflatex {}".format(outpath))

os.chdir("./data")
word = input("Which word do you want to reverse? > ")
create_pdf(word, 
           "./_19_tex_snippets/{}.txt", 
           "./_19_tex_reverse.tex")
os.chdir("..")