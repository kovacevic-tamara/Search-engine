def rang(resultSet,graph):
    rank = {}

    for res in resultSet.keys():
        br=resultSet[res]
        incom=graph.incoming_edges(res)
        br_inc_reci=0
        br_inc=0

        for i in incom:
            if i in resultSet.keys():
                 br_inc_reci+=(resultSet[i])
                 br_inc+=2
            else:
                br_inc+=1
        br_inc=len(incom)
        rank[res]=br+round(0.8*br_inc)+round(0.6*br_inc_reci)

    return rank
