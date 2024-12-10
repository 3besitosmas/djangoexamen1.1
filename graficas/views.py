from django.shortcuts import render

def get_graph_data():
    """
    Helper function to return sample data for graphs.
    Returns:
        A dictionary with sample graph data.
    """
    return [
        {
            'etiquetas': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
            'datos': [5, 15, 10, 20, 250]
        },
        {
            'etiquetas': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
            'datos': [5, 15, 10, 30, 25]
        },
        {
            'etiquetas': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
            'datos': [268, 156, 250, 20, 25]
        }
    ]
def graficas_view(request):
    graph_data = get_graph_data()
    print("Graph Data:", graph_data)  # Para verificar que los datos son correctos
    return render(request, 'graficas/Grafica.html', {
        'grafica1': graph_data[0],
        'grafica2': graph_data[1],
        'grafica3': graph_data[2],
    })
