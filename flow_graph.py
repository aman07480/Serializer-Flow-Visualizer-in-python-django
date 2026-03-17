def build_flow_graph(logs):
    """
    Convert flow logs into graph format
    """

    nodes = []
    edges = []

    for index, log in enumerate(logs):

        node = {
            "id": index,
            "label": log["step"],
            "status": log.get("status", "INFO")
        }

        nodes.append(node)

        if index > 0:
            edges.append({
                "from": index - 1,
                "to": index
            })

    return {
        "nodes": nodes,
        "edges": edges
    }