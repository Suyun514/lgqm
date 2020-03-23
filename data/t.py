from lxml import etree


def wiki2md(aid, author):
    f = open(aid + '.html', 'r', encoding='UTF-8')
    s = etree.HTML(f.read())

    s = s[0][0]

    t = '---\naid: ' + aid + '\nzid: %d\ntitle: ' + aid + '.%04d-%s\nauthor: ' + author + '\n---\n\n'

    zid = 1
    for n in s:
        if n.tag == "h2":
            f = open("output/" + aid + "/%04d.md" % zid, "w", encoding='UTF-8')
            f.write(t % (zid, zid, n[0].text))
            zid = zid + 1
        else:
            if n.text is not None:
                f.write(n.text)
                f.write("\n")


wiki2md("2004", "社会主义螺丝刀")