emails = ["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"]
# . is ignored
# + anything after is removed untill @ is reached
for i in emails:
    left = "".join(i.rsplit("+")[:1])
    right = "".join(i.rsplit("+",1)[1:])
    if len(right) == 0:
        domain = "@"+ "".join(left.rsplit("@",1)[1:])
        left = "".join(i.rsplit("@")[:1])
        left = left.replace('.',"")
        fmail = left+domain
        remails.append(fmail)
    else:
        domain = "@"+ "".join(right.rsplit("@",1)[1:])
        left = left.replace('.',"")
        fmail = left+domain
        remails.append(fmail)
print(len(set(remails)))

