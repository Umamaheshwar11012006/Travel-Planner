from flask import Flask, render_template, request, jsonify
from graph import Graph

app = Flask(__name__)
graph = Graph()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_city', methods=['POST'])
def add_city():
    city = request.form.get('city')
    graph.add_vertex(city)
    return jsonify({'result': f'City {city} added'})

@app.route('/add_route', methods=['POST'])
def add_route():
    from_city = request.form.get('from')
    to_city = request.form.get('to')
    distance = float(request.form.get('distance'))
    graph.add_edge(from_city, to_city, distance)
    return jsonify({'result': f'Route added from {from_city} to {to_city} with distance {distance}'})

@app.route('/shortest_path', methods=['POST'])
def shortest_path():
    source = request.form.get('source')
    destination = request.form.get('destination')
    path, distance = graph.dijkstra(source, destination)
    if distance == float('inf'):
        return jsonify({'path': [], 'distance': 'No path found'})
    else:
        return jsonify({'path': path, 'distance': distance})

if __name__ == '__main__':
    app.run(debug=True)
