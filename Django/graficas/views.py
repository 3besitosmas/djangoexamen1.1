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
            'datos': [5, 15, 10, 20, 25]
        },
        {
            'etiquetas': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
            'datos': [5, 15, 10, 20, 25]
        },
        {
            'etiquetas': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
            'datos': [268, 156, 250, 20, 25]
        }
    ]

def graficas_view(request):
    """
    Render the graphs view with prepared data.
    Args:
        request: HTTP request object.
    Returns:
        Rendered HTML template with graph data.
    """
    graph_data = get_graph_data()
    return render (request, 'graficas/graficas.html', {
        'grafica1': graph_data[0],
        'grafica2': graph_data[1],
        'grafica3': graph_data[2],
})