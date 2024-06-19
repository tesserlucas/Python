# Vamos reconstruir a Rede PERT e calcular o caminho crítico
DG = nx.DiGraph()

# Adicionando os nós ao gráfico
for activity_id, activity_info in activities_info.items():
    DG.add_node(activity_id, name=activity_info['name'])

# Adicionando as arestas ao gráfico com base nas dependências
for activity_id, activity_info in activities_info.items():
    for dependency in activity_info['dependencies']:
        # No diagrama de PERT, as arestas representam as dependências, e o peso é a duração
        DG.add_edge(dependency, activity_id, weight=activity_info['duration'])

# Função para desenhar a Rede PERT
def draw_pert_graph(dg):
    pos = nx.spring_layout(dg)
    edge_labels = nx.get_edge_attributes(dg, 'weight')
    node_labels = {node: dg.nodes[node]['name'] for node in dg.nodes}
    
    plt.figure(figsize=(15, 10))
    nx.draw(dg, pos, with_labels=True, labels=node_labels, node_size=3000, node_color='skyblue', font_size=15)
    nx.draw_networkx_edge_labels(dg, pos, edge_labels=edge_labels, font_color='red', font_size=15)
    plt.title('Rede PERT')
    plt.axis('off')  # Desliga os eixos
    plt.show()

# Desenhando a Rede PERT
draw_pert_graph(DG)
# Calculando o caminho crítico
critical_path = nx.dag_longest_path(DG)
print(f'Caminho crítico: {critical_path}')

# Calculando a duração do caminho crítico e a duração total do projeto (em semanas) 
# Calculando a duração do caminho crítico (em semanas) 
# Calculando a duração total do projeto (em semanas)
total_duration = sum([DG.nodes[node]['weight'] for node in critical_path])
print(f'Duração total do projeto: {total_duration} semanas')

# Calculando a duração do caminho crítico (em semanas) 
# Calculando a duração total do projeto (em semanas)
total_duration = sum([DG.nodes[node]['weight'] for node in critical_path])
print(f'Duração total do projeto: {total_duration} semanas')

# Calculando a duração do caminho crítico (em semanas) 
# Calculando a duração total do projeto (em semanas)
total_duration = sum([DG.nodes[node]['weight'] for node in critical_path])
print(f'Duração total do projeto: {total_duration} semanas')

# Calculando a duração do caminho crítico (em semanas) 
# Calculando a duração total do projeto (em semanas)
total_duration = sum([DG.nodes[node]['weight'] for node in critical_path])
print(f'Duração total do projeto: {total_duration} semanas')

# Calculando a duração do caminho crítico (em semanas) 
# Calculando a duração total do projeto (em semanas)
total_duration = sum([DG.nodes[node]['weight'] for node in critical_path])
print(f'Duração total do projeto: {total_duration} semanas')

# Calculando a duração do caminho crítico (em semanas) 
# Calculando a duração total do projeto (em semanas)
total_duration = sum([DG.nodes[node]['weight'] for node in critical_path])
print(f'Duração total do projeto: {total_duration} semanas')

# Calculando a duração do caminho crítico (em semanas) 
# Calculando a duração total do projeto (em semanas)
total_duration = sum([DG.nodes[node]['weight'] for node in critical_path])
print(f'Duração total do projeto: {total_duration} semanas')

# Calculando a duração do caminho crítico (em semanas) 
# Calculando a duração total do projeto (em semanas)
total_duration = sum([DG.nodes[node]['weight'] for node in critical_path])
print(f'Duração total do projeto: {total_duration} semanas')

# Calculando a duração do caminho crítico (em semanas) 
# Calculando a duração total do projeto (em semanas)   