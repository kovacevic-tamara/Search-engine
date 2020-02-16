#broj pojavljivanja traženih reči na njoj,
#broj linkova iz drugih stranica na pronađenu stranicu i
#broj traženih reči u stranicama koje sadrže link na traženu stranicu

#u result set imam br pojavljivanja
#u incoming imam linkove stranica koje dolaze
#u pretrazim te koje dolaze i izbrojim u resultSetu tom

#resultSet={"aa.html":6,"bb.html",4}
from stablo import kreiraj_graf, izbor


def rang(resultSet):
    for res in resultSet: #uzmes aa
        br_poj=resultSet[res]
        #print(izbor().g)

       # br_link=len(g._ingoing)


